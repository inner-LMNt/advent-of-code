def intersect(line1, line2):
    lower = 2e14
    upper = 4e14
    
    slope1 = line1[3]/line1[2]
    slope2 = line2[3]/line2[2]

    if slope1 == slope2:
        return False

    y_int_1 = line1[1] - slope1 * line1[0]
    y_int_2 = line2[1] - slope2 * line2[0]

    x = (y_int_2 - y_int_1) / (slope1 - slope2)
    y = slope1 * x + y_int_1

    if lower <= x <= upper and lower <= y <= upper:
        if ((line1[3] > 0 and y > line1[1]) or (line1[3] < 0 and y < line1[1])) \
        and ((line2[3] > 0 and y > line2[1]) or (line2[3] < 0 and y < line2[1])):
            return True
    
    return False

def solution1(input):
    positions = []
    velocities = []

    for line in input:
        line = line.replace(' ', '')
        line = line.split('@')
        position = line[0].split(',')
        velocity = line[1].split(',')
        positions.append((int(position[0]), int(position[1])))
        velocities.append((int(velocity[0]), int(velocity[1])))

    count = 0
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            line1 = (positions[i][0], positions[i][1], velocities[i][0], velocities[i][1])
            line2 = (positions[j][0], positions[j][1], velocities[j][0], velocities[j][1])
            count += intersect(line1, line2)

    print(count)

if __name__ == "__main__":
    file_path = 'hail.txt'
    data = []
    with open(file_path) as file:
        data = file.read().splitlines()

    solution1(data)