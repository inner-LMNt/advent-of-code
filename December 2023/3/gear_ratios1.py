def parse(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    m = len(lines)
    n = len(lines[0])-1 # -1 to remove \n

    array = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            array[i][j] = lines[i][j]

    return array

# not parts
def operate(array):
    total_sum = 0

    for i in range(len(array)):
        current_num = []
        j = 0
        start = 0
        end = 0
        while j < len(array[0]):
            if array[i][j].isdigit():
                start = j
                while j < len(array[0]) and array[i][j].isdigit():
                    current_num.append(array[i][j])
                    j += 1
                end = j - 1
                add = True
                
                if i == 0:
                    if start == 0: # Top left corner
                        for k in range(0, end+1):
                            if array[i+1][k] != '.':
                                add = False
                                break
                        if array[i][end+1] != '.' or array[i+1][end+1] != '.':
                            add = False

                    elif end == len(array[0]) - 1: # Top right corner
                        for k in range(start, end+1):
                            if array[i+1][k] != '.':
                                add = False
                                break
                        if array[i][start-1] != '.' or array[i+1][start-1] != '.':
                            add = False

                    else: # Top row, not corner
                        for k in range(start, end+1):
                            if array[i+1][k] != '.':
                                add = False
                                break
                        if array[i][start-1] != '.' or array[i+1][start-1] != '.':
                            add = False
                        if array[i][end+1] != '.' or array[i+1][end+1] != '.':
                            add = False

                if i != 0 and i != len(array)-1:
                    if start == 0: # Left column
                        for k in range(start, end+1):
                            if array[i+1][k] != '.' or array[i-1][k] != '.':
                                add = False
                                break
                        if array[i][end+1] != '.' or array[i+1][end+1] != '.' or array[i-1][end+1] != '.':
                            add = False
                    
                    elif end == len(array[0]) - 1: # Right column
                        for k in range(start, end+1):
                            if array[i+1][k] != '.' or array[i-1][k] != '.':
                                add = False
                                break
                        if array[i][start-1] != '.' or array[i+1][start-1] != '.' or array[i-1][start-1] != '.':
                            add = False

                    else: # Middle
                        for k in range(start, end+1):
                            if array[i+1][k] != '.' or array[i-1][k] != '.':
                                add = False
                                break
                        if array[i][start-1] != '.' or array[i+1][start-1] != '.' or array[i-1][start-1] != '.':
                            add = False
                        if array[i][end+1] != '.' or array[i+1][end+1] != '.' or array[i-1][end+1] != '.':
                            add = False

                if i == len(array)-1:
                    if start == 0: # Bottom left corner
                        for k in range(start, end+1):
                            if array[i-1][k] != '.':
                                add = False
                                break
                        if array[i][end+1] != '.' or array[i-1][end+1] != '.':
                            add = False
                    
                    elif end == len(array[0]) - 1: # Bottom right corner
                        for k in range(start, end+1):
                            if array[i-1][k] != '.':
                                add = False
                                break
                        if array[i][start-1] != '.' or array[i-1][start-1] != '.':
                            add = False

                    else: # Bottom row, not corner
                        for k in range(start, end+1):
                            if array[i-1][k] != '.':
                                add = False
                                break
                        if array[i][start-1] != '.' or array[i-1][start-1] != '.':
                            add = False
                        if array[i][end+1] != '.' or array[i-1][end+1] != '.':
                            add = False

                if add:
                    total_sum += int(''.join(current_num))
                    # print("Added:", int(''.join(current_num)), "to not parts")
                current_num = []
            else:
                j += 1

    return total_sum


# sum all numbers in the file
def sum(array):
    total_sum = 0

    for i in range(len(array)):
        current_num = []
        j = 0
        while j < len(array[0]):
            if array[i][j].isdigit():
                while j < len(array[0]) and array[i][j].isdigit():
                    current_num.append(array[i][j])
                    j += 1
                total_sum += int(''.join(current_num))
                current_num = []
            else:
                j += 1

    return total_sum


def process_file(file_path):
    array = parse(file_path)
    total_sum = sum(array)
    print("Total sum1:", total_sum)
    total_sum -= operate(array)
    print("Total sum2:", total_sum)
    return total_sum

file_path = '0.txt'
result_sum = process_file(file_path)
print(f'Result: {result_sum}')