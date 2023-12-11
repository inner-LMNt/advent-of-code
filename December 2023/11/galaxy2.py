def solution(data):
    def empty_row(i):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                return False
        return True
    
    def empty_col(i):
        for line in data:
            if line[i] == '#':
                return False
        return True
    
    empty_rows = []
    empty_cols = []

    for i in range(len(data)):
        if empty_row(i):
            empty_rows.append(i)

    for i in range(len(data[0])):
        if empty_col(i):
            empty_cols.append(i)

    galaxies = []
    
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == '#':
                galaxies.append((i,j))

    expansion = 1
    count = 0

    for i, (row, col) in enumerate(galaxies):
        for j in range(i):
            new_row = galaxies[j][0]
            new_col = galaxies[j][1]
            distance = abs(row - new_row) + abs(col - new_col)

            for empty in empty_rows:
                if min(row, new_row) < empty < max(row, new_row):
                    distance += expansion
            
            for empty in empty_cols:
                if min(col, new_col) < empty < max(col, new_col):
                    distance += expansion
            
            count += distance

    print(count)

if __name__ == '__main__':
    file_path = 'galaxy.txt'

    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data.append(line.strip())
    
    solution(data)