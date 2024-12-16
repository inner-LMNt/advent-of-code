def solve(disk):
    mem = []
    id = 0

    free = False
    for c in list(disk):
        for _ in range(int(c)):
            if free:
                mem.append('.')
            else:
                mem.append(id)
        if not free:
            id += 1
        free = not free

    left, right = 0, len(mem) - 1

    while left < right:
        if mem[left] == '.':
            while right > left and mem[right] == '.':
                right -= 1
            if right == left:
                break
            mem[left], mem[right] = mem[right], mem[left]
        left += 1

    checksum = 0
    for i, v in enumerate(mem):
        if v == '.':
            break
        checksum += i * v

    return checksum


if __name__ == '__main__':
    file = 'fragment.txt'
    input = None
    with open(file, 'r') as file:
        for line in file:
            input = line.strip()

    print(solve(input))