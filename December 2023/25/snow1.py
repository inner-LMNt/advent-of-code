def solution1(input):
    vertices = set(input)

    def count_neighbors(v):
        return len(input[v] - vertices)

    while sum(map(count_neighbors, vertices)) != 3:
        vertices.remove(max(vertices, key=count_neighbors))

    result = len(vertices) * len(set(input) - vertices)
    
    print(result)

if __name__ == "__main__":
    data = {}

    with open('snow.txt') as file:
        for line in file:
            vertices = line.replace(':', '').split()
            first, *rest = vertices
            for vertex in rest:
                data.setdefault(first, set()).add(vertex)
                data.setdefault(vertex, set()).add(first)
    
    solution1(data)
