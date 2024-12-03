def is_num(c):
    return '0' <= c <= '9'

def solve(memory):
    for line in memory:
        n = len(line)
        step = 0
        idx = 0
        num1, num2 = 0, 0
        total = 0

        while idx < n:
            if step == 0:
                if idx < n-3 and line[idx:idx+3] == 'mul':
                    step = 1
                    idx += 3
                else:
                    idx += 1
            
            elif step == 1:
                if line[idx] == '(':
                    step = 2
                    idx += 1
                else:
                    step = 0
                    idx += 1

            elif step == 2:
                if not is_num(line[idx]):
                    step = 0
                tmp = ''
                while is_num(line[idx]):
                    tmp += line[idx]
                    idx += 1
                num1 = int(tmp)
                step = 3

            elif step == 3:
                if line[idx] == ',':
                    step = 4
                    idx += 1
                else:
                    step = 0
                    idx += 1

            elif step == 4:
                if not is_num(line[idx]):
                    step = 0
                tmp = ''
                while is_num(line[idx]):
                    tmp += line[idx]
                    idx += 1
                num2 = int(tmp)
                step = 5

            elif step == 5:
                if line[idx] == ')':
                    total += num1 * num2
                    step = 0
                    idx += 1
                else:
                    step = 0
                    idx += 1

        print(total)


if __name__ == '__main__':
    file = 'mull.txt'
    input = []
    with open(file, 'r') as f:
        for line in f:
            input.append(line.strip())

    print(solve(input))