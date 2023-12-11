def solution2():
    def empty_row(row):
        for i in range(len(row)):
            if row[i] == '#':
                return False
        return True
    
    def empty_col(col):
        for i in range(len(col)):
            if col[i] == '#':
                return False
        return True
    
    empty_rows = []
    for i in range(len(data)):
        if empty_row(data[i]):
            empty_rows.append(i)

    empty_cols = []
    for i in range(len(data[0])):
        col = [data[j][i] for j in range(len(data))]
        if empty_col(col):
            empty_cols.append(i)

    galaxies = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                galaxies.append((i, j))

    expansion = 999999 # Only change

    ans = 0

    for i, (row, col) in enumerate(galaxies):
        for j in range(i, len(galaxies)):
            row2, col2 = galaxies[j]
            distance = abs(row2 - row) + abs(col2 - col)

            for empty in empty_rows:
                if min(row, row2) <= empty <= max(row, row2):
                    distance += expansion

            for empty in empty_cols:
                if min(col, col2) <= empty <= max(col, col2):
                    distance += expansion

            ans += distance

    print(ans)



if __name__ == '__main__':
    file_path = 'galaxy.txt'

    data = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            data.append(line)

    solution2()