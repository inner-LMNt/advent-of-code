# Surely there's an cleaner way, but I chose to explicitly deal with the direction on a case-by-case basis.

def solve(data):
    grid = data[:50]
    moves = ''.join(data[51:])

    for i in range(50):
        row = []
        for j in range(50):
            if grid[i][j] == '#':
                row = row + ['#'] * 2
            elif grid[i][j] == 'O':
                row = row + ['[', ']']
            elif grid[i][j] == '.':
                row = row + ['.'] * 2
            elif grid[i][j] == '@':
                row = row + ['@', '.']
        grid[i] = row

    x, y = 0, 0
    for i in range(50):
       for j in range(100):
           if grid[i][j] == '@':
               y, x = i, j
               break
    
    # Use dfs to see if the boxes can be pushed up, down, left, or right
    def check_push_up(row, col):
        c = grid[row][col]
        if c == '.':
            return True
        if c == '#':
            return False
        nonlocal seen
        seen.add((row, col))
        
        if c == '[':
            if (row, col + 1) not in seen:
                return check_push_up(row - 1, col) and check_push_up(row, col + 1)
            else:
                return check_push_up(row - 1, col)
        elif c == ']':
            if (row, col - 1) not in seen:
                return check_push_up(row - 1, col) and check_push_up(row, col - 1)
            else:
                return check_push_up(row - 1, col)
        
    def check_push_down(row, col):
        c = grid[row][col]
        if c == '.':
            return True
        if c == '#':
            return False
        nonlocal seen
        seen.add((row, col))
        
        if c == '[':
            if (row, col + 1) not in seen:
                return check_push_down(row + 1, col) and check_push_down(row, col + 1)
            else:
                return check_push_down(row + 1, col)
        elif c == ']':
            if (row, col - 1) not in seen:
                return check_push_down(row + 1, col) and check_push_down(row, col - 1)
            else:
                return check_push_down(row + 1, col)

    def check_push_left(row, col):
        c = grid[row][col]
        if c == '.':
            return True
        if c == '#':
            return False
        nonlocal seen
        seen.add((row, col))
        
        if c == '[':
            return check_push_left(row, col - 1)
        elif c == ']':
            seen.add((row, col - 1))
            return check_push_left(row, col - 2)

    def check_push_right(row, col):
        c = grid[row][col]
        if c == '.':
            return True
        if c == '#':
            return False
        nonlocal seen
        seen.add((row, col))
        
        if c == '[':
            seen.add((row, col + 1))
            return check_push_right(row, col + 2)
        elif c == ']':
            return check_push_right(row, col + 1)
            

    for m in moves:
        seen = set()
        if m == '^':
            c = grid[y - 1][x]
            if c == '.':
                grid[y][x] = '.'
                grid[y - 1][x] = '@'
                y -= 1

            elif c == '[' or c == ']':
                if check_push_up(y - 1, x):
                    for row, col in sorted(seen, key=lambda x: x[0]):
                        grid[row - 1][col] = grid[row][col]
                        grid[row][col] = '.'
                    grid[y][x] = '.'
                    grid[y - 1][x] = '@'
                    y -= 1

        elif m == 'v':
            c = grid[y + 1][x]
            if c == '.':
                grid[y][x] = '.'
                grid[y + 1][x] = '@'
                y += 1

            elif c == '[' or c == ']':
                if check_push_down(y + 1, x):
                    for row, col in sorted(seen, key=lambda x: x[0], reverse=True):
                        grid[row + 1][col] = grid[row][col]
                        grid[row][col] = '.'
                    grid[y][x] = '.'
                    grid[y + 1][x] = '@'
                    y += 1

        elif m == '<':
            c = grid[y][x - 1]
            if c == '.':
                grid[y][x] = '.'
                grid[y][x - 1] = '@'
                x -= 1

            elif c == '[' or c == ']':
                if check_push_left(y, x - 1):
                    for row, col in sorted(seen, key=lambda x: x[1]):
                        grid[row][col - 1] = grid[row][col]
                        grid[row][col] = '.'
                    grid[y][x] = '.'
                    grid[y][x - 1] = '@'
                    x -= 1

        elif m == '>':
            c = grid[y][x + 1]
            if c == '.':
                grid[y][x] = '.'
                grid[y][x + 1] = '@'
                x += 1

            elif c == '[' or c == ']':
                if check_push_right(y, x + 1):
                    for row, col in sorted(seen, key=lambda x: x[1], reverse=True):
                        grid[row][col + 1] = grid[row][col]
                        grid[row][col] = '.'
                    grid[y][x] = '.'
                    grid[y][x + 1] = '@'
                    x += 1

    for line in grid:
        print(''.join(line))

    total = 0
    for i in range(50):
        for j in range(100):
            if grid[i][j] == '[':
                total += 100 * i + j

    return total   


if __name__ == '__main__':
    file = 'robot.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))  # 1522215