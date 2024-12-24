def solve():
    A, B, C = 64751475, 0, 0
    program = '2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0'
    program = program.split(',')
    program = [int(x) for x in program]
    out = []
    pc = 0

    while True:
        if pc >= len(program):
            break
        instr = program[pc]
        operand = program[pc + 1]
        
        if instr == 0:
            if 0 <= operand <= 3:
                A = A // (2 ** operand)
            elif operand == 4:
                A = A // (2 ** A)
            elif operand == 5:
                A = A // (2 ** B)
            elif operand == 6:
                A = A // (2 ** C)

        elif instr == 1:
            B = B ^ operand

        elif instr == 2:
            if 0 <= operand <= 3:
                B = operand
            elif operand == 4:
                B = A % 8
            elif operand == 5:
                B = B % 8
            elif operand == 6:
                B = C % 8

        elif instr == 3:
            if A != 0:
                pc = operand
                continue

        elif instr == 4:
            B = B ^ C

        elif instr == 5:
            if 0 <= operand <= 3:
                out.append(operand)
            elif operand == 4:
                out.append(A % 8)
            elif operand == 5:
                out.append(B % 8)
            elif operand == 6:
                out.append(C % 8)

        elif instr == 6:
            if 0 <= operand <= 3:
                B = A // (2 ** operand)
            elif operand == 4:
                B = A // (2 ** A)
            elif operand == 5:
                B = A // (2 ** B)
            elif operand == 6:
                B = A // (2 ** C)

        elif instr == 7:
            if 0 <= operand <= 3:
                C = A // (2 ** operand)
            elif operand == 4:
                C = A // (2 ** A)
            elif operand == 5:
                C = A // (2 ** B)
            elif operand == 6:
                C = A // (2 ** C)

        pc += 2

    return ','.join([str(x) for x in out])


if __name__ == '__main__':
    print(solve())  # 3,1,4,3,1,7,1,6,3