def enclosed(grid, start_row, start_col, visited):
    def is_valid(row, col):
            return 0 <= row < rows and 0 <= col < cols
    
    rows = len(grid)
    cols = len(grid[0])
    stack = [(start_row, start_col)]

    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    valid = ["-7J", "|LJ", "-FL", "|F7"]
    Sdirections = []
    Sdirs = []
    for i in range(4):
        pos = directions[i]
        new_row = start_row + pos[0]
        new_col = start_col + pos[1]
        if is_valid(new_row, new_col) and grid[new_row][new_col] in valid[i]:
            Sdirections.append([new_row, new_col])
            Sdirs.append(i)

    Svalid = 3 in Sdirs

    while stack:
        row, col = stack.pop()

        if not is_valid(row, col) or visited[row][col] or grid[row][col] == '.':
            continue

        visited[row][col] = True
        current = grid[row][col]

        valid_neighbors = []
        if current == '|':
            valid_neighbors = [(row-1, col), (row+1, col)]
        elif current == '-':
            valid_neighbors = [(row, col-1), (row, col+1)]
        elif current == 'L':
            valid_neighbors = [(row-1, col), (row, col+1)]
        elif current == 'J':
            valid_neighbors = [(row-1, col), (row, col-1)]
        elif current == '7':
            valid_neighbors = [(row+1, col), (row, col-1)]
        elif current == 'F':
            valid_neighbors = [(row+1, col), (row, col+1)]
        elif current == 'S':
            valid_neighbors = Sdirections

        for neighbor_row, neighbor_col in valid_neighbors:
            stack.append((neighbor_row, neighbor_col))

    count = 0

    for i in range(height):
        encl = False
        for j in range(width):
            if visited[i][j]:
                if grid[i][j] in "|JL" or (grid[i][j]=="S" and Svalid): 
                    encl = not encl
            else:
                count += encl
    return count

if __name__ == '__main__':
    file_path = "tiles.txt"
    grid = []
	
    with open(file_path,"r") as file:
        for line in file:
            grid.append(list(line.strip()))

    start_row = 0
    start_col = 0
			
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if 'S' in grid[row][col]:
                start_row = row
                start_col = grid[row].index('S')
                break

    height = len(grid)
    width = len(grid[0])

    visited = [[False] * width for _ in range(height)]

    encl = enclosed(grid, start_row, start_col, visited)
    print("Enclosed: ", encl)
    
