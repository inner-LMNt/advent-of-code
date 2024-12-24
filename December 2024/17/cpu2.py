def solve():
    """
    Disassembling this program, it essentially loops with the following end states:
    A = A // 8
    B = (((A % 8) ^ 2) ^ (A // 32) ) ^ 3
    C = A // 32

    A is being shifted 3 bits to the right, and B is printed out.
    In the calculation of (A // 32), A is being shifted 5 bits to the right.
    This means that higher bits are only being used towards later outputs.
    We can use this fact to first shoehorn higher bits, then consider the lower bits.
    """

    program = '2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0'
    program = program.split(',')
    program = [int(x) for x in program]

    
    def run(A, B, C):
        out = []
        pc = 0
        while True:
            if pc >= len(program):
                break
            instr = program[pc]
            operand = program[pc + 1]
            
            if instr == 0:
                A = A // 8

            elif instr == 1:
                B = B ^ operand

            elif instr == 2:
                B = A % 8

            elif instr == 3:
                if A != 0:
                    pc = 0
                    continue

            elif instr == 4:
                B = B ^ C

            elif instr == 5:
                out.append(B % 8)

            elif instr == 7:
                C = A // (2 ** B)

            pc += 2

        return out
    
    A = 8 ** 15  # Minimum value for 16 outputs since 3 bits are consumed each loop
    power = 13  # Since a bit shift of 5 is used, start using 13 instead of 14 (5 < 6 == 2 3-bit shifts)
    n = 1
    result = []

    while result != program:
        A += 8 ** power
        result = run(A, 0, 0)
        if result[-n:] == program[-n:]:
            # Moving power down by 8 (3 bits) will no longer affect later outputs
            power = max(power - 1, 0)
            n += 1

    return A


if __name__ == '__main__':
    print(solve())  # 37221270076916