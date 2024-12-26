def solve(data):
    state = {}

    data[0] = data[0].split('\n')

    for line in data[0]:
        var, val = line.split(': ')
        state[var] = val

    data[1] = data[1].split('\n')

    statements = []

    for line in data[1]:
        if line:
            inputs, out = line.split(' -> ')
            a, op, b = inputs.split(' ')
            statements.append((a, op, b, out))

    i = 0
    while statements:
        if i == len(statements):
            i = 0
        a, op, b, out = statements[i]

        if a in state and b in state:
            if op == 'AND':
                state[out] = int(state[a]) & int(state[b])
            elif op == 'OR':
                state[out] = int(state[a]) | int(state[b])
            elif op == 'XOR':
                state[out] = int(state[a]) ^ int(state[b])
            
            statements.pop(i)
        else:
            i += 1

    zs = []

    for k in state.keys():
        if k[0] == 'z':
            zs.append(k)

    binary = ''

    for z in sorted(zs, reverse=True):
        binary += str(state[z])

    return int(binary, 2)


if __name__ == '__main__':
    file = 'wires.txt'
    data = []
    with open(file, 'r') as file:
        data = file.read().split('\n\n')

    print(solve(data))  # 42049478636360