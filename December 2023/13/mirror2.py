def h_symmetry(pivot, grid):
    for i in range(len(grid)):
        if pivot - i - 1 >= 0 and pivot + i < len(grid):
            if grid[pivot - i - 1] != grid[pivot + i]:
                return 0
    return pivot
   
def h_blemish(pivot, grid):
    count = 0
    blem_i = 0
    blem_j = 0
    for i in range(len(grid)):
        if pivot - i - 1 >= 0 and pivot + i < len(grid):
            for j in range(len(grid[0])):
                if grid[pivot - i - 1][j] != grid[pivot + i][j]:
                    count += 1
                    blem_i = pivot - i - 1
                    blem_j = j

    if count == 1:
        return [blem_i, blem_j]
    else:
        return None
        
    
def v_symmetry(pivot, grid):
    for j in range(len(grid[0])):
        if pivot - j - 1>= 0 and pivot + j < len(grid[0]):
            for i in range(len(grid)):
                if grid[i][pivot - j - 1] != grid[i][pivot + j]:
                    return 0
    return pivot
    
def v_blemish(pivot, grid):
    count = 0
    blem_i = 0
    blem_j = 0
    for j in range(len(grid[0])):
        if pivot - j - 1>= 0 and pivot + j < len(grid[0]):
            for i in range(len(grid)):
                if grid[i][pivot - j - 1] != grid[i][pivot + j]:
                    count += 1
                    blem_i = i
                    blem_j = pivot - j - 1

    if count == 1:
        return [blem_i, blem_j]
    else:
        return None

def solution1(data):
    count = 0
    for grid in data:
        new_grid = grid.split('\n')

        blemish = []
        for i in range(len(new_grid)):
            if h_blemish(i, new_grid) != None:
                blemish.append(h_blemish(i, new_grid))
        for i in range(len(new_grid[0])):
            if v_blemish(i, new_grid) != None:
                if v_blemish(i, new_grid) not in blemish:
                    blemish.append(v_blemish(i, new_grid))

        new_new_grid = []
        for i in range(len(new_grid)):
            new_new_grid.append(new_grid[i])

        if len(blemish) == 1:
            if new_grid[blemish[0][0]][blemish[0][1]] == '#':
                new_new_grid[blemish[0][0]] = list(new_new_grid[blemish[0][0]])
                new_new_grid[blemish[0][0]][blemish[0][1]] = '.'
                new_new_grid[blemish[0][0]] = ''.join(new_new_grid[blemish[0][0]])
            else:
                new_new_grid[blemish[0][0]] = list(new_new_grid[blemish[0][0]])
                new_new_grid[blemish[0][0]][blemish[0][1]] = '#'
                new_new_grid[blemish[0][0]] = ''.join(new_new_grid[blemish[0][0]])
        else:
            pass

        for i in range(len(new_grid)):
            if h_symmetry(i, new_new_grid) != h_symmetry(i, new_grid):
                count += 100 * h_symmetry(i, new_new_grid)
        for i in range(len(new_grid[0])):
            if v_symmetry(i, new_new_grid) != v_symmetry(i, new_grid):
                count += 1 * v_symmetry(i, new_new_grid)

    print(count)

if __name__ == '__main__':
    file_path = 'mirror.txt'

    with open(file_path, 'r') as f:
        data = f.read().strip().split('\n\n')
    
    solution1(data)