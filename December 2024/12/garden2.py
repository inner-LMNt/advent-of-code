def solve(garden):
    visited = set()

    def valid(x, y):
        return 0 <= x < len(garden) and 0 <= y < len(garden[0])

    def dfs(x, y, p):
        result = []
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            result.append((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if valid(nx, ny) and (nx, ny) not in visited and garden[nx][ny] == p:
                    visited.add((nx, ny))
                    stack.append((nx, ny))
        return result

    def get_perimeter(region):
        result = 0
        for x, y in region:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if not valid(nx, ny) or garden[nx][ny] != garden[x][y]:
                    result += 1
        return result
    
    
    def shared_sides(region):
        result = 0
        for x, y in region:
            if (x + 1, y) in region: # check right adjacent
                for y2 in [y - 1, y + 1]: # top and bottom
                    if (x, y2) not in region and (x + 1, y2) not in region:
                        result += 1
            if (x, y + 1) in region: # check bottom adjacent
                for x2 in [x - 1, x + 1]: # left and right
                    if (x2, y) not in region and (x2, y + 1) not in region:
                        result += 1
        return result

    cost = 0
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i, j) not in visited:
                visited.add((i, j))
                plants = dfs(i, j, garden[i][j])
                area = len(plants)
                perimeter = get_perimeter(plants)
                cost += area * (perimeter - shared_sides(plants))

    return cost
                
            
if __name__ == '__main__':
    file = 'garden.txt'
    input = []
    with open(file, 'r') as file:
        for line in file:
            input.append(line.strip())

    print(solve(input))