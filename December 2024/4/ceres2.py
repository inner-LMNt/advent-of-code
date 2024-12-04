def solve(crossword):
    total = 0

    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            if crossword[i][j] == 'M':
                if i < len(crossword)-2 and j < len(crossword[i])-2:
                    if crossword[i+1][j+1] == 'A' and crossword[i+2][j+2] == 'S' and crossword[i+2][j] == 'M' and crossword[i][j+2] == 'S':
                        total += 1

                    if crossword[i+1][j+1] == 'A' and crossword[i+2][j+2] == 'S' and crossword[i+2][j] == 'S' and crossword[i][j+2] == 'M':
                        total += 1
            
            if crossword[i][j] == 'S':
                if i < len(crossword)-2 and j < len(crossword[i])-2:
                    if crossword[i+1][j+1] == 'A' and crossword[i+2][j+2] == 'M' and crossword[i+2][j] == 'S' and crossword[i][j+2] == 'M':
                        total += 1

                    if crossword[i+1][j+1] == 'A' and crossword[i+2][j+2] == 'M' and crossword[i+2][j] == 'M' and crossword[i][j+2] == 'S':
                        total += 1

    return total


if __name__ == '__main__':
    file = 'ceres.txt'
    input = []
    with open(file, 'r') as f:
        for line in f:
            input.append(line.strip())

    print(solve(input))