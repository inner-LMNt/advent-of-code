def solution1(grid):
    queue = []

    for pos, tile in grid.items():
        if tile == "S":
            queue.append((pos, 0))

    tiles = {}
    visited = set()
    size = int(len(grid) ** 0.5)

    while queue:
        pos, dist = queue.pop(0)

        if dist == 65 or pos in visited:
            continue

        tiles[dist] = tiles.get(dist, 0) + 1
        visited.add(pos)

        for neighbor in (1, -1, 1j, -1j):
            n_pos = pos + neighbor

            if grid[complex(n_pos.real % size, n_pos.imag % size)] != "#":
                queue.append((n_pos, dist + 1))

    result = 0
    for distance, amount in tiles.items():
        if not distance % 2:
            result += amount

    print(result)



if __name__ == "__main__":
    file_path = "steps.txt"
    grid = {}

    with open(file_path, "r") as f:
        for y, row in enumerate(f.read().splitlines()):
            for x, tile in enumerate(row.strip()):
                grid[complex(x, y)] = tile

    solution1(grid)
