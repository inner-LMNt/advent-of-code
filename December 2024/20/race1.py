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

    times = []
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def valid(a, b):
        return 0 <= a < dim and 0 <= b < dim
    
    for y, x in path:
        for dy1, dx1 in dirs:
            ny1, nx1 = y + dy1, x + dx1
            if valid(ny1, nx1):
                if data[ny1][nx1] != '#':
                    continue

                for dy2, dx2 in dirs:
                    ny2, nx2 = ny1 + dy2, nx1 + dx2
                    if valid(ny2, nx2):
                        if data[ny2][nx2] != '#':
                            if data[ny2][nx2] - data[y][x] - 2 > 0:
                                times.append(data[ny2][nx2] - data[y][x] - 2)

    return len([x for x in times if x >= 100])

            
if __name__ == '__main__':
    file = 'race.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))  # 1389
    