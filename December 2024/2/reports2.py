import copy

def solve(reports):
    safe = 0

    for r in reports:
        r = r.split(' ')
        for i in range(len(r)):
            c = copy.deepcopy(r)
            c.pop(i)
            if valid(c):
                safe += 1
                break

    return safe

def valid(row):
    if int(row[1]) == int(row[0]):
        return False

    increasing = int(row[1]) > int(row[0])
    is_safe = True
    for i in range(1, len(row)):
        if increasing:
            if int(row[i]) <= int(row[i - 1]):
                is_safe = False
                break
            if not 1 <= int(row[i]) - int(row[i - 1]) <= 3:
                is_safe = False
                break
        else:
            if int(row[i]) >= int(row[i - 1]):
                is_safe = False
                break
            if not -3 <= int(row[i]) - int(row[i - 1]) <= -1:
                is_safe = False
                break

    return is_safe

if __name__ == '__main__':
    file = 'reports.txt'
    reports = []
    
    with open(file, 'r') as f:
        for line in f:
            reports.append(line.strip())

    print(solve(reports))