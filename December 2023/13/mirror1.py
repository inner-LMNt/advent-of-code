def solution1(data):
    def h_symmetry(pivot, grid):
        for i in range(len(grid)):
            if pivot - i - 1 >= 0 and pivot + i < len(grid):
                if grid[pivot - i - 1] != grid[pivot + i]:
                    return 0
        return pivot
    
    def v_symmetry(pivot, grid):
        for j in range(len(grid[0])):
            if pivot - j - 1>= 0 and pivot + j < len(grid[0]):
                for i in range(len(grid)):
                    if grid[i][pivot - j - 1] != grid[i][pivot + j]:
                        return 0
        return pivot

    count = 0
    for grid in data:
        new_grid = grid.split('\n')
        for i in range(len(new_grid)):
            count += 100 * h_symmetry(i, new_grid)
        for i in range(len(new_grid[0])):
            count += 1 * v_symmetry(i, new_grid)

    print(count)

if __name__ == '__main__':
    file_path = 'mirror.txt'

    with open(file_path, 'r') as f:
        data = f.read().strip().split('\n\n')
    
    solution1(data)