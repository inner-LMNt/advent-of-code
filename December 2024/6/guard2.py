from collections import defaultdict

def solve(grid):
    pos, start = None, None
    d = (-1, 0)

    for i, line in enumerate(grid):
        if '^' in line:
            start = (i, line.index('^'))
            pos = start
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
    
    result = set()

    while True:
        next = (pos[0] + d[0], pos[1] + d[1])

        if valid(next[0], next[1]):
            if grid[next[0]][next[1]] == '#':
                d = turn_right(d)
            else:
                line = list(grid[next[0]])
                line[next[1]] = '#'
                grid[next[0]] = ''.join(line)

                temp_pos = start
                temp_d = (-1, 0)
                visited = set()
                
                while True:
                    visited.add((temp_pos, temp_d))
                    temp_next = (temp_pos[0] + temp_d[0], temp_pos[1] + temp_d[1])
                    if not valid(temp_next[0], temp_next[1]):
                        break
                    elif grid[temp_next[0]][temp_next[1]] == '#':
                        temp_d = turn_right(temp_d)
                    elif (temp_next, temp_d) in visited:
                        result.add(next)
                        break
                    else:
                        temp_pos = temp_next
                pos = next

                line = list(grid[next[0]])
                line[next[1]] = '.'
                grid[next[0]] = ''.join(line)

        else:
            break

    return len(result)


if __name__ == '__main__':
    file = 'guard.txt'
    input = []
    with open(file, 'r') as file:
        for line in file:
            input.append(line.strip())

    print(solve(input))