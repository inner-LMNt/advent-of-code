def solve(data):
    grid = [['.' for _ in range(71)] for _ in range(71)]

    for i in range(1024):
        x, y = data[i].split(',')
        x, y = int(x), int(y)

        grid[x][y] = '#'

    def bfs():
        queue = [(0, 0)]
        visited = set()
        visited.add((0, 0))

        while queue:
            x, y = queue.pop(0)

            if x == 70 and y == 70:
                return True

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < 71 and 0 <= ny < 71 and (nx, ny) not in visited and grid[nx][ny] == '.':
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return False

    for i in range(1024, len(data)):
        x, y = data[i].split(',')
        x, y = int(x), int(y)

        grid[x][y] = '#'

        if not bfs():
            return (x, y)


if __name__ == '__main__':
    file = 'ram.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))  # 41,26