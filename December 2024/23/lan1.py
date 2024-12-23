from collections import defaultdict

def solve(data):
    adj_list = defaultdict(list)

    for line in data:
        line = line.split('-')
        adj_list[line[0]].append(line[1])
        adj_list[line[1]].append(line[0])

    groups = set()

    for c in adj_list.keys():
        for c1 in adj_list[c]:
            for c2 in adj_list[c1]:
                for c3 in adj_list[c2]:
                    if c3 == c:
                        groups.add(frozenset(sorted([c, c1, c2])))

    return sum(1 for g in groups if any(c[0] == 't' for c in g))
                
            
if __name__ == '__main__':
    file = 'lan.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))