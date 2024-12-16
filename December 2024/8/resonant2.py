from collections import defaultdict

def solve(grid):
    locations = defaultdict(list)
    result = set()

    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if not c == '.':
                locations[c].append((i, j))

    def valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    for v in locations.values():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                dy, dx = v[j][0] - v[i][0], v[j][1] - v[i][1]
                newpos1 = (v[i][0], v[i][1])
                newpos2 = (v[j][0], v[j][1])

                while valid(newpos1[0], newpos1[1]):
                    result.add(newpos1)
                    newpos1 = (newpos1[0] - dy, newpos1[1] - dx)
                while valid(newpos2[0], newpos2[1]):
                    result.add(newpos2)
                    newpos2 = (newpos2[0] + dy, newpos2[1] + dx)

    return len(result)


if __name__ == '__main__':
    file = 'resonant.txt'
    input = []
    with open(file, 'r') as file:
        for line in file:
            input.append(line.strip())

    print(solve(input))