def steps_ZZZ(instructions, network):
    node = 'AAA'
    steps = 0

    while True:
        for instruction in instructions:
            if instruction == 'R':
                node = network[node][1]
            elif instruction == 'L':
                node = network[node][0]

            steps += 1

            if node == 'ZZZ':
                return steps

if __name__ == "__main__":
    file_path = "0.txt"
    with open(file_path, "r") as file:
        content = file.read().splitlines()

    instructions = content[0]
    networks = content[2:]

    network = {}
    for line in networks:
        parts = line.split('= ')
        if len(parts) == 2:
            node = parts[0].strip()
            connections_part = parts[1].strip().strip('()')
            if connections_part:
                connections = tuple(map(str.strip, connections_part.split(',')))
                network[node] = connections
            else:
                network[node] = ()

    steps = steps_ZZZ(instructions, network)

    print(f"Steps required to reach ZZZ: {steps}")