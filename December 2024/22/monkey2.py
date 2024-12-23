from collections import defaultdict, deque

def solve(data):
    bananas = defaultdict(int)

    def process(num):
        added = set()
        prev = num % 10
        changes = deque()
        for _ in range(2000):
            num = (num ^ (num * 64)) % 16777216
            num = (num ^ (num // 32)) % 16777216
            num = (num ^ (num * 2048)) % 16777216
            changes.append(num % 10 - prev)
            if len(changes) == 4:
                if tuple(changes) not in added:
                    nonlocal bananas
                    bananas[tuple(changes)] += num % 10
                    added.add(tuple(changes))
                changes.popleft()
            prev = num % 10

    for line in data:
        process(int(line))

    return max(bananas.values())    
                
            
if __name__ == '__main__':
    file = 'monkey.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))  # 