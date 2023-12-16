def solution2(input, x, y, dir):
    tracker = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
    stack = [(x, y, dir)]

    slash_set = set()

    while stack:
        row, col, direction = stack.pop()

        if direction == 'right':
            while col < len(input[0]):
                if input[row][col] == '.' or input[row][col] == '-':
                    tracker[row][col] = 1
                    col += 1
                elif input[row][col] == '|':
                    if tracker[row][col] == 1:
                        break
                    tracker[row][col] = 1
                    stack.append((row-1, col, 'up'))
                    stack.append((row+1, col, 'down'))
                    break
                elif input[row][col] == '/':
                    if (row, col, 'right', '/') in slash_set:
                        break
                    slash_set.add((row, col, 'right', '/'))
                    tracker[row][col] = 1
                    stack.append((row-1, col, 'up'))
                    break
                elif input[row][col] == '\\':
                    if (row, col, 'right', '\\') in slash_set:
                        break
                    slash_set.add((row, col, 'right', '\\'))
                    tracker[row][col] = 1
                    stack.append((row+1, col, 'down'))
                    break

        elif direction == 'up':
            while row >= 0:
                if input[row][col] == '.' or input[row][col] == '|':
                    tracker[row][col] = 1
                    row -= 1
                elif input[row][col] == '-':
                    if tracker[row][col] == 1:
                        break
                    tracker[row][col] = 1
                    stack.append((row, col+1, 'right'))
                    stack.append((row, col-1, 'left'))
                    break
                elif input[row][col] == '/':
                    if (row, col, 'up', '/') in slash_set:
                        break
                    slash_set.add((row, col, 'up', '/'))
                    tracker[row][col] = 1
                    stack.append((row, col+1, 'right'))
                    break
                elif input[row][col] == '\\':
                    if (row, col, 'up', '\\') in slash_set:
                        break
                    slash_set.add((row, col, 'up', '\\'))
                    tracker[row][col] = 1
                    stack.append((row, col-1, 'left'))
                    break

        elif direction == 'left':
            while col >= 0:
                if input[row][col] == '.' or input[row][col] == '-':
                    tracker[row][col] = 1
                    col -= 1
                elif input[row][col] == '|':
                    if tracker[row][col] == 1:
                        break
                    tracker[row][col] = 1
                    stack.append((row-1, col, 'up'))
                    stack.append((row+1, col, 'down'))
                    break
                elif input[row][col] == '/':
                    if (row, col, 'left', '/') in slash_set:
                        break
                    slash_set.add((row, col, 'left', '/'))
                    tracker[row][col] = 1
                    stack.append((row+1, col, 'down'))
                    break
                elif input[row][col] == '\\':
                    if (row, col, 'left', '\\') in slash_set:
                        break
                    slash_set.add((row, col, 'left', '\\'))
                    tracker[row][col] = 1
                    stack.append((row-1, col, 'up'))
                    break

        elif direction == 'down':
            while row < len(input):
                if input[row][col] == '.' or input[row][col] == '|':
                    tracker[row][col] = 1
                    row += 1
                elif input[row][col] == '-':
                    if tracker[row][col] == 1:
                        break
                    tracker[row][col] = 1
                    stack.append((row, col+1, 'right'))
                    stack.append((row, col-1, 'left'))
                    break
                elif input[row][col] == '/':
                    if (row, col, 'down', '/') in slash_set:
                        break
                    slash_set.add((row, col, 'down', '/'))
                    tracker[row][col] = 1
                    stack.append((row, col-1, 'left'))
                    break
                elif input[row][col] == '\\':
                    if (row, col, 'down', '\\') in slash_set:
                        break
                    slash_set.add((row, col, 'down', '\\'))
                    tracker[row][col] = 1
                    stack.append((row, col+1, 'right'))
                    break

    return (sum([sum(row) for row in tracker]))

if __name__ == '__main__':
    file_path = 'lava.txt'
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            data.append(list(line.strip()))

    result = 0

    for i in range(len(data)):
        result = max(result, solution2(data, i, 0, 'right'), solution2(data, i, len(data[0])-1, 'left'))

    for j in range(len(data[0])):
        result = max(result, solution2(data, 0, j, 'down'), solution2(data, len(data)-1, j, 'up'))

    print(result)

