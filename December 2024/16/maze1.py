def solve(data):
    dim = len(data[0])
    data[1] = data[1][:dim-2] + '.' + data[1][dim-2:]

    # dp[i][j][k] = minimum cost to reach (i, j) with current direction k
    # 1 = east (0, 1), 2 = south (1, 0), 3 = west (0, -1), 4 = north (-1, 0)
    dp = [[[float('inf') for _ in range(4)] for _ in range(dim)] for _ in range(dim)]
    dp[dim-2][1][0] = 0

    # bfs to fill dp table
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = [(dim-2, 1, 0)]

    while q:
        i, j, k = q.pop(0)
        for l in range(4):
            if l == k:
                ni, nj = i + di[l], j + dj[l]
                if data[ni][nj] == '.' and dp[i][j][k] + 1 < dp[ni][nj][l]:
                    dp[ni][nj][l] = dp[i][j][k] + 1
                    q.append((ni, nj, l))
            elif abs(l - k) != 2:
                if dp[i][j][l] > dp[i][j][k] + 1000:
                    dp[i][j][l] = dp[i][j][k] + 1000
                    q.append((i, j, l))

    return min(dp[1][dim-2])

            
if __name__ == '__main__':
    file = 'maze.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))  # 106512
    