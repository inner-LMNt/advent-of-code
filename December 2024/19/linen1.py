def solve(data):
    colors = data[0].split(', ')
    
    result = 0
    for towel in data[2:]:
        dp = [False for _ in range(len(towel) + 1)]
        dp[0] = True

        for i in range(1, len(towel) + 1):
            for c in colors:
                if i >= len(c) and towel[i-len(c):i] == c and dp[i-len(c)]:
                    dp[i] = True
                    break
        
        if dp[-1]:
            result += 1

    return result
                
            
if __name__ == '__main__':
    file = 'linen.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))  # 255