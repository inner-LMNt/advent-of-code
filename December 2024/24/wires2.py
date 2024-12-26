def solve(data):
    state = {}

    data[0] = data[0].split('\n')

    xs, ys = [], []

    for line in data[0]:
        var, val = line.split(': ')
        state[var] = val
        if var[0] == 'x':
            xs.append(var)
        elif var[0] == 'y':
            ys.append(var)

    x_bin, y_bin = '', ''

    for x in sorted(xs, reverse=True):
        x_bin += state[x]

    for y in sorted(ys, reverse=True):
        y_bin += state[y]

    data[1] = data[1].split('\n')

    statements = []

    vars = set()

    for line in data[1]:
        if line:
            inputs, out = line.split(' -> ')
            a, op, b = inputs.split(' ')
            vars.add(a)
            vars.add(b)
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

    for v in vars:
        if v not in state:
            print(v)

    zs = []

    for k in state.keys():
        if k[0] == 'z':
            zs.append(k)

    z_bin = ''

    for z in sorted(zs, reverse=True):
        z_bin += str(state[z])

    xy = int(x_bin, 2) + int(y_bin, 2)
    xy = bin(xy)[2:]

        
    print(xy)       # 1001100100000001101000010001001101010101001000
    print(z_bin)    # 1001100011111001101000001111001011001101001000
    
    print(bin(int(xy, 2) - int(z_bin, 2))[2:])  # 1000000000000010000010001000000000

    # Problematic z outputs: z09, z13, z19, z33

    # After taking a look at tree_graph.png, I manually searched around these z nodes for the pairs to swap.
    # Each part of the graph is essentially a full adder circuit, just look around for any discrepancies.

    switch = []
    # z09: gws, nnt
    switch.append('gws')
    switch.append('nnt')

    # z13: npf, z13
    switch.append('npf')
    switch.append('z13')

    # z19: cph, z19
    switch.append('cph')
    switch.append('z19')

    # z33: hgj, z33
    switch.append('hgj')
    switch.append('z33')

    return ','.join(sorted(switch))


if __name__ == '__main__':
    file = 'wires.txt'
    data = []
    with open(file, 'r') as file:
        data = file.read().split('\n\n')

    print(solve(data))  # cph,gws,hgj,nnt,npf,z13,z19,z33