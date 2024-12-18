def solve(trail):
    result = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    path = 0

    def valid(x, y):
        return 0 <= x < len(trail) and 0 <= y < len(trail[0])
    
    def dfs(x, y, current):
        if not valid(x, y):
            return

        if trail[x][y] == current:
            if current == '9':
                nonlocal path
                path += 1
                return
            
            for d in dirs:
                new_x, new_y = x + d[0], y + d[1]
                dfs(new_x, new_y, str(int(current) + 1))

    for i in range(len(trail)):
        for j in range(len(trail[0])):
            if trail[i][j] == '0':
                dfs(i, j, '0')
                result += path
                path = 0

    return result

            
if __name__ == '__main__':
    file = 'hoof.txt'
    input = []
    with open(file, 'r') as file:
        for line in file:
            input.append(list(line.strip()))

    print(solve(input))