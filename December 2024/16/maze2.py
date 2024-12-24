from collections import defaultdict

def solve(data):
    dim = len(data[0])
    data[1] = data[1][:dim-2] + '.' + data[1][dim-2:]

    tiles = set()
    path = []
    cost = 106512
    min_costs = defaultdict(int)

    stack = [[dim-2, 1, 0, cost, [(dim-2, 1)]]]  # y, x, direction, remaining cost, path
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    def makes_sense(i, j, k, c):  # Prune paths that are not optimal, e.g., two consecutive turns
        if (i, j, k) in min_costs and min_costs[(i, j, k)] > c:
            return False
        min_costs[(i, j, k)] = c
        return True
    
    while stack:
        i, j, k, c, path = stack.pop()
        if c < 0:
            continue
        if c == 0 and i == 1 and j == dim-2:
            tiles.update(path)
            continue

        for l in range(4):
            if l == k:
                ni, nj = i + di[l], j + dj[l]
                if data[ni][nj] == '.' and c - 1 >= 0 and makes_sense(ni, nj, l, c - 1):
                    stack.append([ni, nj, l, c - 1, path + [(ni, nj)]])
            elif abs(l - k) != 2:
                if c - 1000 >= 0 and makes_sense(i, j, l, c - 1000):
                    stack.append([i, j, l, c - 1000, path])

    return len(tiles)

            
if __name__ == '__main__':
    file = 'maze.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))  # 563
    