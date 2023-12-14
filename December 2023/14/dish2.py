def cycle_data(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'O':
                k = i
                while i > 0 and data[i-1][j] == '.':
                    data[i-1][j] = 'O'
                    data[i][j] = '.'
                    i -= 1
                i = k

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'O':
                k = j
                while j > 0 and data[i][j-1] == '.':
                    data[i][j-1] = 'O'
                    data[i][j] = '.'
                    j -= 1
                j = k

    for i in range(len(data)-1, -1, -1):
        for j in range(len(data[0])):
            if data[i][j] == 'O':
                k = i
                while i < len(data)-1 and data[i+1][j] == '.':
                    data[i+1][j] = 'O'
                    data[i][j] = '.'
                    i += 1
                i = k

    for i in range(len(data)):
        for j in range(len(data[0])-1, -1, -1):
            if data[i][j] == 'O':
                k = j
                while j < len(data[0])-1 and data[i][j+1] == '.':
                    data[i][j+1] = 'O'
                    data[i][j] = '.'
                    j += 1
                j = k

    return data

def solution2(data):
    # By 2000, there likely emerges a pattern already which repeats every n cycles. Extend this pattern to 1000000000.
    for k in range(1, 2000): 
        data = cycle_data(data)
        count = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == 'O':
                    count += len(data) - i

        print("i:", k, " count:", count)
    
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

    solution2(data)