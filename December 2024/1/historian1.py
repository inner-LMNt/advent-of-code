def solve(l1, l2):
    l1, l2 = sorted(l1), sorted(l2)
    total = 0

    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])

    return total

if __name__ == '__main__':
    file = 'historian.txt'
    l1, l2 = [], []

    with open(file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            l1.append(int(l.split()[0]))
            l2.append(int(l.split()[1]))

    print(solve(l1, l2))
        