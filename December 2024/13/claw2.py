def solve(games):
    total = 0

    for i in range(len(games)//4 + 1):
        A = games[i*4]
        B = games[i*4+1]
        p = games[i*4+2]

        A = A.split(': ')[1]
        Ax, Ay = A.split(', ')
        Ax, Ay = int(Ax.split('+')[1]), int(Ay.split('+')[1])
        B = B.split(': ')[1]
        Bx, By = B.split(', ')
        Bx, By = int(Bx.split('+')[1]), int(By.split('+')[1])
        
        p = p.split(': ')[1]
        pX, pY = p.split(', ')
        pX, pY = int(pX.split('=')[1]), int(pY.split('=')[1])
        pX, pY = pX + 10_000_000_000_000, pY + 10_000_000_000_000

        # i * Ax + j * Bx = pX
        # i * Ay + j * By = pY

        ## Rearrange the first equation for i
        # i = (pX - j * Bx) / Ax
        
        ## Then, plug i into the second equation to solve for j
        # (pX - j * Bx) / Ax * Ay + j * By = pY
        # (pX * Ay - j * Bx * Ay) / Ax + j * By = pY
        # pX * Ay - j * Bx * Ay + j * By * Ax = pY * Ax
        # - j * Bx * Ay + j * By * Ax = pY * Ax - pX * Ay
        # j * (By * Ax - Bx * Ay) = pY * Ax - pX * Ay
        # j = (pY * Ax - pX * Ay) / (By * Ax - Bx * Ay)

        bot = By * Ax - Bx * Ay
        if bot == 0:
            continue

        j = (pY * Ax - pX * Ay)
        if j % bot != 0:
            continue
        j //= bot
        
        i = (pX - j * Bx)
        if i % Ax != 0:
            continue
        i //= Ax

        total += (i * 3 + j)

    return int(total)
                
            
if __name__ == '__main__':
    file = 'claw.txt'
    input = []
    with open(file, 'r') as file:
        for line in file:
            input.append(line.strip())

    print(solve(input))