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

    def generate_picture():
        picture = [['.' for _ in range(width)] for _ in range(height)]
        for robot in robots:
            picture[robot[1]][robot[0]] = '#'
        return picture

    seconds = 0
    while True:
        seconds += 1

        for robot in robots:
            robot[0] = (robot[0] + robot[2] + width) % width
            robot[1] = (robot[1] + robot[3] + height) % height

        picture = generate_picture()
        b = False
        for line in picture:
            if ''.join(line).find('##############') != -1:  # Assuming 14 consecutive #s will appear in christmas tree picture
                b = True
                for l in picture:
                    print(''.join(l))

        if b:
            break

    return seconds
                
            
if __name__ == '__main__':
    file = 'robot.txt'
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())

    print(solve(data))