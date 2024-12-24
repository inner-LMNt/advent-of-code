def solve(data):
    dim = len(data)
    for i in range(dim):
        data[i] = list(data[i])

    sy, sx = 0, 0
    ey, ex = 0, 0

    for i in range(dim):
        for j in range(dim):
            if data[i][j] == 'S':
                sy, sx = i, j
            if data[i][j] == 'E':
                ey, ex = i, j

    def dfs():
        stack = [[sy, sx, []]]
        visited = set()
        while stack:
            y, x, path = stack.pop()
            if (y, x) in visited:
                continue
            visited.add((y, x))
            if y == ey and x == ex:
                return path
            for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < dim and 0 <= nx < dim and data[ny][nx] != '#':
                    stack.append([ny, nx, path + [(ny, nx)]])

    path = dfs()
    t = 1
    for y, x, in path:
        data[y][x] = t
        t += 1
    data[sy][sx] = 0
    path = [(sy, sx)] + path

    manhattan = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
    times = []
    
    for i, s in enumerate(path):
        for j in range(i + 1, len(path)):
            e = path[j]
            if manhattan(s, e) <= 20:
                times.append(data[e[0]][e[1]] - data[s[0]][s[1]] - manhattan(s, e))

    return len([x for x in times if x >= 100])

            
if __name__ == '__main__':
    file = 'race.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))  # 1005068
    