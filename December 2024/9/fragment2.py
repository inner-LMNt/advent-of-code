from collections import defaultdict

def solve(disk):
    mem = []
    file_len = defaultdict(int)
    file_start = defaultdict(int)
    id = 0

    free = False
    for c in list(disk):
        for _ in range(int(c)):
            if free:
                mem.append('.')
            else:
                mem.append(id)
        if not free:
            file_len[id] = int(c)
            file_start[id] = len(mem) - int(c)
            id += 1
        free = not free

    for i in reversed(range(id)):
        vacant = 0
        vacant_start = -1
        for j in range(file_start[i]):
            if mem[j] == '.':
                if vacant == 0:
                    vacant_start = j
                vacant += 1
            else:
                vacant = 0

            if vacant == file_len[i]:
                for k in range(file_start[i], file_start[i] + file_len[i]):
                    mem[vacant_start + k - file_start[i]] = mem[k]
                    mem[k] = '.'
                break

    checksum = 0
    for i, v in enumerate(mem):
        if v == '.':
            continue
        checksum += i * v

    return checksum


if __name__ == '__main__':
    file = 'fragment.txt'
    input = None
    with open(file, 'r') as file:
        for line in file:
            input = line.strip()

    print(solve(input))