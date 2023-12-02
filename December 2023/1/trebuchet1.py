def concatenate_first_last(line):
    integers = [int(char) for char in line if char.isdigit()]
    if len(integers) >= 2:
        result = int(str(integers[0]) + str(integers[-1]))
        return result
    elif len(integers) == 1:
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
