def solution1(input):
    directions = {'R': (1, 0), 'L': (-1, 0), 'D': (0, 1), 'U': (0, -1)}

    mvts = [line.split() for line in input]
    pos_x, pos_y = 0, 0
    vertices = [(pos_x, pos_y)]

    boundary = 0
    interior = 0

    for dir, steps, _ in mvts:
        x, y = directions[dir]
        n = int(steps)

        pos_x += x * n
        pos_y += y * n

        vertices.append((pos_x, pos_y))

        boundary += n

    p = perimeter(vertices)
    a = area(vertices)

    interior = picks_theorem(a, boundary, 0)

    total = boundary + interior
    print(total)

def perimeter(vertices):
    n = len(vertices)
    perimeter = 0

    for i in range(n - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i + 1]
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        perimeter += distance

    return perimeter

def area(vertices):
    # Shoelace formula
    n = len(vertices)
    a = 0

    for i in range(n - 1):
        a += vertices[i][0] * vertices[i + 1][1]
        a -= vertices[i + 1][0] * vertices[i][1]

    a = abs(a) / 2
    return a

def picks_theorem(a, boundary, interior):
    # Pick's theorem: area = interior + boundary / 2 - 1
    return a - (boundary / 2) + 1

if __name__ == "__main__":
    file_path = 'lagoon.txt'
    data = []
    with open(file_path) as file:
        data = file.read().splitlines()

    solution1(data)
