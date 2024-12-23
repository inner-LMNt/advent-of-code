def solve(data):
    width, height = 101, 103

    robots = []

    for line in data:
        line = line.split(' ')
        x, y = line[0][2:].split(',')
        x, y = int(x), int(y)
        dx, dy = line[1][2:].split(',')
        dx, dy = int(dx), int(dy)

        robots.append([x, y, dx, dy])

    for _ in range(100):
        for robot in robots:
            robot[0] = (robot[0] + robot[2] + width) % width
            robot[1] = (robot[1] + robot[3] + height) % height

    def sum_quadrant(q):
        mid_w, mid_h = width // 2, height // 2
        if q == 1:
            return sum(1 for r in robots if r[0] < mid_w and r[1] < mid_h) 
        elif q == 2:
            return sum(1 for r in robots if r[0] > mid_w and r[1] < mid_h)
        elif q == 3:
            return sum(1 for r in robots if r[0] < mid_w and r[1] > mid_h)
        else:
            return sum(1 for r in robots if r[0] > mid_w and r[1] > mid_h)
    
    return sum_quadrant(1) * sum_quadrant(2) * sum_quadrant(3) * sum_quadrant(4)    
                
            
if __name__ == '__main__':
    file = 'robot.txt'
    input = []
    with open(file, 'r') as file:
        for line in file:
            input.append(line.strip())

    print(solve(input))  # 216772608