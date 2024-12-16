def solve(grid):
    pos = None
    d = (-1, 0)

    for i, line in enumerate(grid):
        if '^' in line:
            pos = (i, line.index('^'))
            break

    def valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def turn_right(d):
        if d == (-1, 0):
            return (0, 1)
        if d == (0, 1):
            return (1, 0)
        if d == (1, 0):
            return (0, -1)
        if d == (0, -1):
            return (-1, 0)
    
    line = list(grid[pos[0]])
    line[pos[1]] = 'X'
    grid[pos[0]] = ''.join(line)

    while True:
        next = (pos[0] + d[0], pos[1] + d[1])

        if valid(next[0], next[1]):
            if grid[next[0]][next[1]] == '#':
                d = turn_right(d)
            else:
                line = list(grid[next[0]])
                line[next[1]] = 'X'
                grid[next[0]] = ''.join(line)
                pos = next
        else:
            break

    return sum([line.count('X') for line in grid])


if __name__ == '__main__':
    file = 'guard.txt'
    input = []
    with open(file, 'r') as file:
        for line in file:
            input.append(line.strip())

    print(solve(input))