def is_num(c):
    return '0' <= c <= '9'

def solve(line):
    n = len(line)
    mul_step = 0
    idx = 0
    num1, num2 = 0, 0
    total = 0
    do = True

    while idx < n:
        if idx < n-4 and line[idx:idx+4] == 'do()':
            do = True
            idx += 4
        if idx < n-7 and line[idx:idx+7] == "don't()":
            do = False
            idx += 7
        
        if idx == n:
            break

        if mul_step == 0:
            if idx < n-3 and line[idx:idx+3] == 'mul':
                mul_step = 1
                idx += 3
            else:
                idx += 1
        
        elif mul_step == 1:
            if line[idx] == '(':
                mul_step = 2
                idx += 1
            else:
                mul_step = 0
                idx += 1

        elif mul_step == 2:
            if not is_num(line[idx]):
                mul_step = 0
            tmp = ''
            while is_num(line[idx]):
                tmp += line[idx]
                idx += 1
            num1 = int(tmp)
            mul_step = 3

        elif mul_step == 3:
            if line[idx] == ',':
                mul_step = 4
                idx += 1
            else:
                mul_step = 0
                idx += 1

        elif mul_step == 4:
            if not is_num(line[idx]):
                mul_step = 0
            tmp = ''
            while is_num(line[idx]):
                tmp += line[idx]
                idx += 1
            num2 = int(tmp)
            mul_step = 5

        elif mul_step == 5:
            if line[idx] == ')':
                if do:
                    total += num1 * num2
                mul_step = 0
                idx += 1
            else:
                mul_step = 0
                idx += 1

    print(total)


if __name__ == '__main__':
    file = 'mull.txt'
    input = ''
    with open(file, 'r') as f:
        for line in f:
            input += line.strip()

    print(solve(input))