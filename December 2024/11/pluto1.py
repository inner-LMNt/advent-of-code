def solve(stones):
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
    
    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == '0':
                new_stones.append('1')
            elif even_length(stone):
                first, second = split(stone)
                new_stones.append(first)
                new_stones.append(second)
            else:
                new_stones.append(str(int(stone) * 2024))
        stones = new_stones

    return len(stones)
            
if __name__ == '__main__':
    file = 'pluto.txt'
    input = None
    with open(file, 'r') as file:
        for line in file:
            input = line.strip().split()

    print(solve(input))