def solve(data):
    def process(num):
        for _ in range(2000):
            num = (num ^ (num * 64)) % 16777216
            num = (num ^ (num // 32)) % 16777216
            num = (num ^ (num * 2048)) % 16777216
        return num

    return sum(process(int(line)) for line in data)
                
            
if __name__ == '__main__':
    file = 'monkey.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))  # 20506453102