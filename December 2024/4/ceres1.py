def solve(crossword):
    total = 0

    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            if crossword[i][j] == 'X':
                # going up
                if i >= 3:
                    if crossword[i-1][j] == 'M' and crossword[i-2][j] == 'A' and crossword[i-3][j] == 'S':
                        total += 1
                        
                # going down
                if i <= len(crossword) - 4:
                    if crossword[i+1][j] == 'M' and crossword[i+2][j] == 'A' and crossword[i+3][j] == 'S':
                        total += 1

                # going left
                if j >= 3:
                    if crossword[i][j-1] == 'M' and crossword[i][j-2] == 'A' and crossword[i][j-3] == 'S':
                        total += 1

                # going right
                if j <= len(crossword[i]) - 4:
                    if crossword[i][j+1] == 'M' and crossword[i][j+2] == 'A' and crossword[i][j+3] == 'S':
                        total += 1

                # diagonal up right
                if i >= 3 and j <= len(crossword[i]) - 4:
                    if crossword[i-1][j+1] == 'M' and crossword[i-2][j+2] == 'A' and crossword[i-3][j+3] == 'S':
                        total += 1

                # diagonal down right
                if i <= len(crossword) - 4 and j <= len(crossword[i]) - 4:
                    if crossword[i+1][j+1] == 'M' and crossword[i+2][j+2] == 'A' and crossword[i+3][j+3] == 'S':
                        total += 1

                # diagonal up left
                if i >= 3 and j >= 3:
                    if crossword[i-1][j-1] == 'M' and crossword[i-2][j-2] == 'A' and crossword[i-3][j-3] == 'S':
                        total += 1

                # diagonal down left
                if i <= len(crossword) - 4 and j >= 3:
                    if crossword[i+1][j-1] == 'M' and crossword[i+2][j-2] == 'A' and crossword[i+3][j-3] == 'S':
                        total += 1

    return total


if __name__ == '__main__':
    file = 'ceres.txt'
    input = []
    with open(file, 'r') as f:
        for line in f:
            input.append(line.strip())

    print(solve(input))