def solve(rules, updates):
    result = 0
    for u in updates:
        valid = True
        for i in range(len(u)):
            for j in range(i+1, len(u)):
                for r in rules:
                    if r[0] == u[j] and r[1] == u[i]:
                        valid = False
                        break
                if not valid:
                    break
            if not valid:
                break
        if valid:
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