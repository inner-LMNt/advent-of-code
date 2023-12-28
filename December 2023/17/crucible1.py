from heapq import heappush, heappop

def add(grid, priority_queue, heat_loss, row, col, dr, dc, steps=1):
    new_row = row + dr
    new_col = col + dc

    if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row])):
        return

    heappush(priority_queue, (heat_loss + grid[new_row][new_col], new_row, new_col, dr, dc, steps))

def solution1(input):
    grid = [list(map(int, line.strip())) for line in input]
    visited = set()
    priority_queue = [(0, 0, 0, 0, 0, 0)]

    while priority_queue:
        heat_loss, row, col, dr, dc, steps = heappop(priority_queue)

        if row == len(grid) - 1 and col == len(grid[row]) - 1:
            print(heat_loss)
            break

        if (row, col, dr, dc, steps) in visited:
            continue

        visited.add((row, col, dr, dc, steps))

        if steps < 3 and (dr, dc) != (0, 0):
            add(grid, priority_queue, heat_loss, row, col, dr, dc, steps + 1)

        for new_dr, new_dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (new_dr, new_dc) != (dr, dc) and (new_dr, new_dc) != (-dr, -dc):
                add(grid, priority_queue, heat_loss, row, col, new_dr, new_dc)

if __name__ == "__main__":
    file_path = 'crucible.txt'
    data = []

    with open(file_path, 'r') as file:
        data = file.read().splitlines()

    solution1(data)
