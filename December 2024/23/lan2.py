from collections import defaultdict

def solve(data):
    adj_list = defaultdict(list)

    for line in data:
        line = line.split('-')
        adj_list[line[0]].append(line[1])
        adj_list[line[1]].append(line[0])
    
    computers = set(adj_list.keys())
    groups = [set([c]) for c in computers]

    for g in groups:
        for c in computers:
            if all(c in adj_list[gc] for gc in g):
                g.add(c)

    max_group = max(groups, key=len)
    return ','.join(sorted(max_group))
                
            
if __name__ == '__main__':
    file = 'lan.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))  # am,bc,cz,dc,gy,hk,li,qf,th,tj,wf,xk,xo