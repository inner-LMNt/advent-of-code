def solution1(data):
    def binary_map(con):
        if con == '1':
            return '#'
        else:
            return '.'

    count = 0
    for line in data:
        broken = []
        broken_sum = 0
        nums = line[1].split(',')
        for num in nums:
            broken.append(int(num))

        broken_sum = sum(broken)

        qmarks = []
        for i in range(len(line[0])):
            if line[0][i] == '?':
                qmarks.append(i)

        for i in range(2 ** len(qmarks)):
            binary = bin(i)[2:].zfill(len(qmarks))
            new_line = line[0]

            for j in range(len(qmarks)):
                new_line = new_line[:qmarks[j]] + binary_map(binary[j]) + new_line[qmarks[j] + 1:]

            if new_line.count('#') == broken_sum:
                broken_index = 0
                broken_count = 0
                for i, char in enumerate(new_line):
                    if broken_index == len(broken):
                        break
                    if char == '.':
                        broken_count = 0
                    elif char == '#':
                        broken_count += 1
                        if broken[broken_index] == broken_count:
                            if i != len(new_line)-1:
                                if new_line[i+1] == '#':
                                    break
                            broken_index += 1
                            broken_count = 0
                
                if broken_index == len(broken):
                    count += 1

    print(count)

if __name__ == '__main__':
    file_path = 'onsen.txt'
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(line.split(' '))

    solution1(data)