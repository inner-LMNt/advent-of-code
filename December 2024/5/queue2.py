def solve(rules, updates):
    result = 0

    def is_valid(a):
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                for r in rules:
                    if r[0] == a[j] and r[1] == a[i]:
                        a[i], a[j] = a[j], a[i]
                        return False
        return True
    
    for u in updates:
        valid = is_valid(u)
        if not valid:
            while not valid:
                valid = is_valid(u)
            result += int(u[len(u)//2])

    return result


if __name__ == '__main__':
    file = 'queue.txt'
    rules = []
    updates = []
    with open(file, 'r') as file:
        f = file.read()
        for line in f.split('\n\n')[0].split('\n'):
            order = line.split('|')
            rules.append((order[0], order[1]))

        for line in f.split('\n\n')[1].split('\n'):
            if line:
                updates.append(line.split(','))

    print(solve(rules, updates))