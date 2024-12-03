def solve(reports):
    safe = 0

    for r in reports:
        r = r.split(' ')
        if int(r[1]) == int(r[0]):
            continue

        increasing = int(r[1]) > int(r[0])
        is_safe = True
        for i in range(1, len(r)):
            if increasing:
                if int(r[i]) <= int(r[i - 1]):
                    is_safe = False
                    break
                if not 1 <= int(r[i]) - int(r[i - 1]) <= 3:
                    is_safe = False
                    break
            else:
                if int(r[i]) >= int(r[i - 1]):
                    is_safe = False
                    break
                if not -3 <= int(r[i]) - int(r[i - 1]) <= -1:
                    is_safe = False
                    break

        if is_safe:
            safe += 1

    return safe


if __name__ == '__main__':
    file = 'reports.txt'
    reports = []
    
    with open(file, 'r') as f:
        for line in f:
            reports.append(line.strip())

    print(solve(reports))