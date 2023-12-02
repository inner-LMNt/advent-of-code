def concatenate_first_last(line):
    integers = []
    for i in range(len(line)):
        if line[i].isdigit():
            integers.append(int(line[i]))
        if line[i] == 'o':
            if i >= 3 and line[i-1] == 'r' and line[i-2] == 'e' and line[i-3] == 'z':
                integers.append(0)
        if line[i] == 'e':
            if i >= 2 and line[i-1] == 'n' and line[i-2] == 'o':
                integers.append(1)
        if line[i] == 'o':
            if i >= 2 and line[i-1] == 'w' and line[i-2] == 't':
                integers.append(2)
        if line[i] == 'e':
            if i >= 4 and line[i-1] == 'e' and line[i-2] == 'r' and line[i-3] == 'h' and line[i-4] == 't':
                integers.append(3)
        if line[i] == 'r':
            if i >= 3 and line[i-1] == 'u' and line[i-2] == 'o' and line[i-3] == 'f':
                integers.append(4)
        if line[i] == 'e':
            if i >= 3 and line[i-1] == 'v' and line[i-2] == 'i' and line[i-3] == 'f':
                integers.append(5)
        if line[i] == 'x':
            if i >= 2 and line[i-1] == 'i' and line[i-2] == 's':
                integers.append(6)
        if line[i] == 'n':
            if i >= 4 and line[i-1] == 'e' and line[i-2] == 'v' and line[i-3] == 'e' and line[i-4] == 's':
                integers.append(7)
        if line[i] == 't':
            if i >= 4 and line[i-1] == 'h' and line[i-2] == 'g' and line[i-3] == 'i' and line[i-4] == 'e':
                integers.append(8)
        if line[i] == 'e':
            if i >= 3 and line[i-1] == 'n' and line[i-2] == 'i' and line[i-3] == 'n':
                integers.append(9)

    if len(integers) >= 2:
        result = int(str(integers[0]) + str(integers[-1]))
        print(f'Line: {line.strip()}, First Digit: {integers[0]}, Last Digit: {integers[-1]}')
        return result
    elif len(integers) == 1:
        print(f'Line: {line.strip()}, Only One Digit: {integers[0]}')
        return integers[0] * 11
    else:
        return 0

def process_file(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            result = concatenate_first_last(line)
            total_sum += result

    return total_sum

file_path = 'trebuchet.txt'
result_sum = process_file(file_path)
print(f'Total sum of concatenated first and last integers: {result_sum}')
