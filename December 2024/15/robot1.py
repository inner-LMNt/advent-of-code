def solve(data):
    grid = data[:50]
    moves = ''.join(data[51:])

    for i in range(50):
        grid[i] = list(grid[i])

    x, y = 0, 0
    for i in range(50):
       for j in range(50):
           if grid[i][j] == '@':
               y, x = i, j
               break 

    for m in moves:
        if m == '^':
            if grid[y - 1][x] == '.':
                grid[y][x] = '.'
                y -= 1
                grid[y][x] = '@'

            elif grid[y - 1][x] == 'O':
                boxes = 1
                while grid[y - 1 - boxes][x] == 'O':
                    boxes += 1
                if grid[y - 1 - boxes][x] == '.':
                    grid[y][x] = '.'
                    grid[y - 1][x] = '@'
                    grid[y - 1 - boxes][x] = 'O'
                    y -= 1

        elif m == 'v':
            if grid[y + 1][x] == '.':
                grid[y][x] = '.'
                y += 1
                grid[y][x] = '@'

            elif grid[y + 1][x] == 'O':
                boxes = 1
                while grid[y + 1 + boxes][x] == 'O':
                    boxes += 1
                if grid[y + 1 + boxes][x] == '.':
                    grid[y][x] = '.'
                    grid[y + 1][x] = '@'
                    grid[y + 1 + boxes][x] = 'O'
                    y += 1

        elif m == '<':
            if grid[y][x - 1] == '.':
                grid[y][x] = '.'
                x -= 1
                grid[y][x] = '@'

            elif grid[y][x - 1] == 'O':
                boxes = 1
                while grid[y][x - 1 - boxes] == 'O':
                    boxes += 1
                if grid[y][x - 1 - boxes] == '.':
                    grid[y][x] = '.'
                    grid[y][x - 1] = '@'
                    grid[y][x - 1 - boxes] = 'O'
                    x -= 1

        elif m == '>':
            if grid[y][x + 1] == '.':
                grid[y][x] = '.'
                x += 1
                grid[y][x] = '@'

            elif grid[y][x + 1] == 'O':
                boxes = 1
                while grid[y][x + 1 + boxes] == 'O':
                    boxes += 1
                if grid[y][x + 1 + boxes] == '.':
                    grid[y][x] = '.'
                    grid[y][x + 1] = '@'
                    grid[y][x + 1 + boxes] = 'O'
                    x += 1

    total = 0
    for i in range(50):
        for j in range(50):
            if grid[i][j] == 'O':
                total += 100 * i + j

    return total   


if __name__ == '__main__':
    file = 'robot.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))  # 1499739