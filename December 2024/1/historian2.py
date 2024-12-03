from collections import defaultdict

def solve(l1, l2):
    occ = defaultdict(int)
    for i in l2:
        occ[i] += 1
    
    total = 0
    for i in l1:
        total += i * occ[i]
        
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
        