### Inefficient dp solution, you can just solve with math instead lol (which you need in pt. 2)

def solve(games):
    total = 0

    for i in range(len(games)//4 + 1):
        A = games[i*4]
        B = games[i*4+1]
        prize = games[i*4+2]

        A = A.split(': ')[1]
        Ax, Ay = A.split(', ')
        Ax, Ay = int(Ax.split('+')[1]), int(Ay.split('+')[1])
        B = B.split(': ')[1]
        Bx, By = B.split(', ')
        Bx, By = int(Bx.split('+')[1]), int(By.split('+')[1])
        
        prize = prize.split(': ')[1]
        prizeX, prizeY = prize.split(', ')
        prizeX, prizeY = int(prizeX.split('=')[1]), int(prizeY.split('=')[1])

        dp = [[-1 for _ in range(prizeY+1)] for _ in range(prizeX+1)]
        dp[0][0] = 0

        x, y = Bx, By
        b_tokens = 1
        locations = [(0, 0, 0)]
        while x <= prizeX and y <= prizeY:
            dp[x][y] = b_tokens
            locations.append((x, y, b_tokens))
            b_tokens += 1
            x, y = x+Bx, y+By
        
        for l in locations:
            a_tokens = 0
            x, y, b = l
            while x <= prizeX and y <= prizeY:
                if dp[x][y] == -1:
                    dp[x][y] = a_tokens + b
                else:
                    dp[x][y] = min(dp[x][y], a_tokens + b)
                a_tokens += 3
                x, y = x+Ax, y+Ay

        if dp[prizeX][prizeY] != -1:
            total += dp[prizeX][prizeY]

    return total
                
            
if __name__ == '__main__':
    file = 'claw.txt'
    input = []
    with open(file, 'r') as file:
        for line in file:
            input.append(line.strip())

    print(solve(input))