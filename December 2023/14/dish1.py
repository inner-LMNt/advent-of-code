def solution1(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'O':
                k = i
                while i > 0 and data[i-1][j] == '.':
                    data[i-1][j] = 'O'
                    data[i][j] = '.'
                    i -= 1
                i = k
    
    for line in data:
        print(''.join(line))

    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'O':
                count += len(data) - i

    print(count)

if __name__ == '__main__':
    file_path = 'dish.txt'
    data = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = list(line.strip())
            data.append(line)

    solution1(data)