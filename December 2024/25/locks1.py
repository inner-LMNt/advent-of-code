def solve(data):
    keys = []
    locks = []

    for a in data:
        a = a.split('\n')

        if a[0] == '.....':
            key = []
            for i in range(5):
                h = 0
                for j in range(7):
                    if a[j][i] == '#':
                        h += 1
                key.append(h)
            keys.append(key)

        else:
            lock = []
            for i in range(5):
                h = 0
                for j in range(7):
                    if a[j][i] == '#':
                        h += 1
                lock.append(h)
            locks.append(lock)

    works = 0

    for l in locks:
        for k in keys:
            if all([l[i] + k[i] <= 7 for i in range(5)]):
                works += 1
    
    return works
            
if __name__ == '__main__':
    file = 'locks.txt'
    data = []
    with open(file, 'r') as file:
        data = file.read().split('\n\n')

    print(solve(data))  # 24
