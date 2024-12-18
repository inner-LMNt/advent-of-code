from collections import defaultdict

def solve(stones):
    stones = defaultdict(int, {stone: 1 for stone in stones})
    def even_length(a):
        return len(a) % 2 == 0
    
    def split(a):
        first, second = a[:len(a) // 2], a[len(a) // 2:]
        i = 0
        while i < len(second) and second[i] == '0':
            i += 1
        second = second[i:]
        if second == '':
            second = '0'
        return first, second
    
    for _ in range(75):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            if stone == '0':
                new_stones['1'] += count
            elif even_length(stone):
                first, second = split(stone)
                new_stones[first] += count
                new_stones[second] += count
            else:
                new_stones[str(int(stone) * 2024)] += count
        stones = new_stones

    return sum(stones.values())
            
if __name__ == '__main__':
    file = 'pluto.txt'
    input = None
    with open(file, 'r') as file:
        for line in file:
            input = line.strip().split()

    print(solve(input))