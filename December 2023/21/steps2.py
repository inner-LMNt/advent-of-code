def walk(max_dist, grid):
    queue = []

    for pos, tile in grid.items():
        if tile == "S":
            queue.append((pos, 0))
            
    tiles = {}
    visited = set()
    size = int(len(grid) ** 0.5)

    while queue:
        pos, dist = queue.pop(0)

        if dist == max_dist + 1 or pos in visited:
            continue

        tiles[dist] = tiles.get(dist, 0) + 1
        visited.add(pos)

        for neighbor in (1, -1, 1j, -1j):
            n_pos = pos + neighbor

            if grid[complex(n_pos.real % size, n_pos.imag % size)] != "#":
                queue.append((n_pos, dist + 1))

    return tiles

def solution2(grid):
    size = (len(list(grid.keys()))) ** 0.5
    edge = size // 2
    target = (26501365 - edge) // size

    y = []
    for i in range(3):
        tiles = walk(edge + i*size, grid)

        temp = 0
        for distance, amount in tiles.items():
            if distance % 2 == (edge + i*size) % 2:
                temp += amount

        y.append(temp)

    a = (y[2] - (2 * y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]

    f = lambda n: a * n**2 + b * n + c

    print(f(target))


if __name__ == "__main__":
    file_path = "steps.txt"
    grid = {}

    with open(file_path, "r") as f:
        for y, row in enumerate(f.read().splitlines()):
            for x, tile in enumerate(row.strip()):
                grid[complex(x, y)] = tile

    solution2(grid)
