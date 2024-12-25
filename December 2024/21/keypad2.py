def solve(sequence):
    numeric = {
        'A': (3, 2),
        '0': (3, 1),
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2)
    }

    # Precalculated optimal paths on directional keypad
    directional = {
        'AA': 'A',
        'A^': '<A',
        'A<': 'v<<A',
        'Av': '<vA',
        'A>': 'vA',

        '^A': '>A',
        '^^': 'A',
        '^<': 'v<A',
        '^v': 'vA',
        '^>': 'v>A',

        '<A': '>>^A',
        '<^': '>^A',
        '<<': 'A',
        '<v': '>A',
        '<>': '>>A',

        'vA': '^>A',
        'v^': '^A',
        'v<': '<A',
        'vv': 'A',
        'v>': '>A',

        '>A': '^A',
        '>^': '<^A',
        '><': '<<A',
        '>v': '<A',
        '>>': 'A',
    }

    def is_any_of(item, *args):
        for a in args:
            if item == a:
                return True
        return False

    def solve_num(start, end):
        y1, x1 = numeric[start]
        y2, x2 = numeric[end]

        y_mov, x_mov = y2 - y1, x2 - x1

        horz = '<' if x_mov < 0 else '>'
        vert = '^' if y_mov < 0 else 'v'

        possible = []

        if is_any_of((start, end), ('A', '1'), ('A', '4'), ('A', '7'), ('0', '1'), ('0', '4'), ('0', '7')):
            possible.append('^' * abs(y_mov) + '<' * abs(x_mov) + 'A')

        elif is_any_of((start, end), ('1', 'A'), ('4', 'A'), ('7', 'A'), ('1', '0'), ('4', '0'), ('7', '0')):
            possible.append('>' * abs(x_mov) + 'v' * abs(y_mov) + 'A')

        elif y_mov == 0 or x_mov == 0:
            temp_input = ''
            if y_mov == 0:
                temp_input += (horz * abs(x_mov))
            
            if x_mov == 0:
                temp_input += (vert * abs(y_mov))

            possible.append(temp_input + 'A')

        else:
            possible.append(vert * abs(y_mov) + horz * abs(x_mov) + 'A')
            possible.append(horz * abs(x_mov) + vert * abs(y_mov) + 'A')

        return possible
    
    memo = {}
    def solve_dir(seq, layer):
        if (seq, layer) in memo:
            return memo[seq, layer]
        if layer == 0:
            return len(seq)
        
        res = 0
        s = 'A' + seq
        for i in range(len(s) - 1):
            key_start, key_end = s[i], s[i + 1]
            res += solve_dir(directional[key_start + key_end], layer - 1)

        memo[seq, layer] = res
        return res
    
    result = 0
    multi = int(sequence[:3])
    sequence = 'A' + sequence

    for i in range(len(sequence) - 1):
        inputs = solve_num(sequence[i], sequence[i + 1])

        if len(inputs) == 1:
            result += solve_dir(inputs[0], 25)

        else:
            minimum = float('inf')
            for p in inputs:
                cost = solve_dir(p, 25)
                if cost < minimum:
                    minimum = cost
            result += minimum

    return result * multi

if __name__ == '__main__':
    file = 'keypad.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())
    
    print(sum([solve(x) for x in data]))  # 246810588779586
