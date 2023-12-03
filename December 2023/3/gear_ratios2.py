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


def gear(array):
    sum = 0
    for i in range(len(array)):
        j = 0

        while j < len(array[0]):
            num = 0
            if array[i][j] == '*':
                print("Found * at", i, j)
                if array[i][j+1].isdigit():
                    num += 1
                if array[i][j-1].isdigit():
                    num += 1
                if array[i-1][j-1].isdigit() and not array[i-1][j].isdigit() and not array[i-1][j+1].isdigit():
                    num += 1
                if array[i-1][j-1].isdigit() and array[i-1][j].isdigit() and not array[i-1][j+1].isdigit():
                    num += 1
                if array[i-1][j-1].isdigit() and array[i-1][j].isdigit() and array[i-1][j+1].isdigit():
                    num += 1
                if not array[i-1][j-1].isdigit() and array[i-1][j].isdigit() and not array[i-1][j+1].isdigit():
                    num += 1
                if not array[i-1][j-1].isdigit() and array[i-1][j].isdigit() and array[i-1][j+1].isdigit():
                    num += 1
                if not array[i-1][j-1].isdigit() and not array[i-1][j].isdigit() and array[i-1][j+1].isdigit():
                    num += 1
                if array[i-1][j-1].isdigit() and not array[i-1][j].isdigit() and array[i-1][j+1].isdigit():
                    num += 2
                
                if array[i+1][j-1].isdigit() and not array[i+1][j].isdigit() and not array[i+1][j+1].isdigit():
                    num += 1
                if array[i+1][j-1].isdigit() and array[i+1][j].isdigit() and not array[i+1][j+1].isdigit():
                    num += 1
                if array[i+1][j-1].isdigit() and array[i+1][j].isdigit() and array[i+1][j+1].isdigit():
                    num += 1
                if not array[i+1][j-1].isdigit() and array[i+1][j].isdigit() and not array[i+1][j+1].isdigit():
                    num += 1
                if not array[i+1][j-1].isdigit() and array[i+1][j].isdigit() and array[i+1][j+1].isdigit():
                    num += 1
                if not array[i+1][j-1].isdigit() and not array[i+1][j].isdigit() and array[i+1][j+1].isdigit():
                    num += 1
                if array[i+1][j-1].isdigit() and not array[i+1][j].isdigit() and array[i+1][j+1].isdigit():
                    num += 2

            if (num != 2):
                j += 1
            else:
                nums = []
                if array[i][j+1].isdigit():
                    k = j+1
                    temp = []
                    while array[i][k].isdigit():
                        temp.append(array[i][k])
                        k += 1
                        if k >= len(array[0]):
                            break
                    nums.append(int(''.join(temp)))              
                    
                if array[i][j-1].isdigit():
                    k = j-1
                    temp = []
                    while array[i][k].isdigit():
                        temp.insert(0, array[i][k])
                        k -= 1
                        if k < 0:
                            break
                    nums.append(int(''.join(temp)))

                if array[i-1][j-1].isdigit() and not array[i-1][j].isdigit() and not array[i-1][j+1].isdigit():
                    k = j-1
                    temp = []
                    while array[i-1][k].isdigit():
                        temp.insert(0, array[i-1][k])
                        k -= 1
                    nums.append(int(''.join(temp)))

                if array[i-1][j-1].isdigit() and array[i-1][j].isdigit() and not array[i-1][j+1].isdigit():
                    k = j
                    temp = []
                    while array[i-1][k].isdigit():
                        temp.insert(0, array[i-1][k])
                        k -= 1
                    nums.append(int(''.join(temp)))

                if array[i-1][j-1].isdigit() and array[i-1][j].isdigit() and array[i-1][j+1].isdigit():
                    temp = [array[i-1][j-1], array[i-1][j], array[i-1][j+1]]
                    nums.append(int(''.join(temp)))

                if not array[i-1][j-1].isdigit() and array[i-1][j].isdigit() and not array[i-1][j+1].isdigit():
                    nums.append(int(array[i-1][j]))

                if not array[i-1][j-1].isdigit() and array[i-1][j].isdigit() and array[i-1][j+1].isdigit():
                    k = j
                    temp = []
                    while array[i-1][k].isdigit():
                        temp.append(array[i-1][k])
                        k += 1
                    nums.append(int(''.join(temp)))

                if not array[i-1][j-1].isdigit() and not array[i-1][j].isdigit() and array[i-1][j+1].isdigit():
                    k = j+1
                    temp = []
                    while array[i-1][k].isdigit():
                        temp.append(array[i-1][k])
                        k += 1
                    nums.append(int(''.join(temp)))

                if array[i-1][j-1].isdigit() and not array[i-1][j].isdigit() and array[i-1][j+1].isdigit():
                    k = j+1
                    temp = []
                    while array[i-1][k].isdigit():
                        temp.append(array[i-1][k])
                        k += 1
                    nums.append(int(''.join(temp)))

                    k = j-1
                    temp = []
                    while array[i-1][k].isdigit():
                        temp.insert(0, array[i-1][k])
                        k -= 1
                    nums.append(int(''.join(temp)))

                # bottom side
                if array[i+1][j-1].isdigit() and not array[i+1][j].isdigit() and not array[i+1][j+1].isdigit():
                    k = j-1
                    temp = []
                    while array[i+1][k].isdigit():
                        temp.insert(0, array[i+1][k])
                        k -= 1
                    nums.append(int(''.join(temp)))

                if array[i+1][j-1].isdigit() and array[i+1][j].isdigit() and not array[i+1][j+1].isdigit():
                    k = j
                    temp = []
                    while array[i+1][k].isdigit():
                        temp.insert(0, array[i+1][k])
                        k -= 1
                    nums.append(int(''.join(temp)))

                if array[i+1][j-1].isdigit() and array[i+1][j].isdigit() and array[i+1][j+1].isdigit():
                    temp = [array[i+1][j-1], array[i+1][j], array[i+1][j+1]]
                    nums.append(int(''.join(temp)))

                if not array[i+1][j-1].isdigit() and array[i+1][j].isdigit() and not array[i+1][j+1].isdigit():
                    nums.append(int(array[i+1][j]))

                if not array[i+1][j-1].isdigit() and array[i+1][j].isdigit() and array[i+1][j+1].isdigit():
                    k = j
                    temp = []
                    while array[i+1][k].isdigit():
                        temp.append(array[i+1][k])
                        k += 1
                    nums.append(int(''.join(temp)))

                if not array[i+1][j-1].isdigit() and not array[i+1][j].isdigit() and array[i+1][j+1].isdigit():
                    k = j+1
                    temp = []
                    while array[i+1][k].isdigit():
                        temp.append(array[i+1][k])
                        k += 1
                    nums.append(int(''.join(temp)))

                if array[i+1][j-1].isdigit() and not array[i+1][j].isdigit() and array[i+1][j+1].isdigit():
                    k = j+1
                    temp = []
                    while array[i+1][k].isdigit():
                        temp.append(array[i+1][k])
                        k += 1
                    nums.append(int(''.join(temp)))

                    k = j-1
                    temp = []
                    while array[i+1][k].isdigit():
                        temp.insert(0, array[i+1][k])
                        k -= 1
                    nums.append(int(''.join(temp)))

                sum += nums[0] * nums[1]
                print("Added", nums[0], "*", nums[1], "=", nums[0] * nums[1], "to sum:", sum)
                j += 1

    return sum            


def process_file(file_path):
    array = parse(file_path)
    return gear(array)

file_path = '0.txt'
result_sum = process_file(file_path)
print(f'Result: {result_sum}')