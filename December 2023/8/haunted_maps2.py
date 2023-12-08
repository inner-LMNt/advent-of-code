import math

def steps(pos):
    sum = 0

    while True:
        if pos.endswith("Z"):
            break
        instruct = instructions[sum % len(instructions)]
        net = network[pos]
        net = net.replace("(", "").replace(")", "")
        nn = net.split(", ")
        if instruct == "L":
            pos = nn[0].strip()
        elif instruct == "R":
            pos = nn[1].strip()
        sum += 1

    return sum

if __name__ == "__main__":
    lines = []
    with open("haunted_maps.txt") as file:
        for line in file:
            lines.append(line.strip())

    instructions = lines[0]

    network = {}
    for line in lines[2:]:
        (a, b) = line.split(" = ")
        network[a] = b


    positions = [_ for _ in network if _.endswith("A")]

    stepsfor = [steps(pos) for pos in positions]

    print(math.lcm(*stepsfor))