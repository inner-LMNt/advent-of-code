from math import gcd

def solution2(input, rx):
    for name, module in input.items():
        for destination in module["destinations"]:
            if destination in input and input[destination]["type"] == "&":
                input[destination]["memory"][name] = 0

    lengths = {}
    visited = {name: 0 for name, module in input.items() if rx in module["destinations"]}
    count = 0

    while True:
        count += 1
        queue = [ ("broadcaster", x, 0) for x in input["broadcaster"]["destinations"] ]
        index = 0

        while index < len(queue):
            source, dest, pulse = queue[index]
            index += 1

            if dest not in input:
                continue

            module = input[dest]

            if module["name"] == rx and pulse == 1:
                visited[source] += 1

                if source not in lengths:
                    lengths[source] = count

                if all(visited.values()):
                    product = 1
                    for length in lengths.values():
                        product *= length // gcd(product, length)
                    print(product)
                    return

            if module["type"] == "%":
                if not pulse:
                    module["memory"] = not module["memory"]
                    out = 1 if module["memory"] else 0
                    for dest in module["destinations"]:
                        queue.append((module["name"], dest, out))
            else:
                module["memory"][source] = pulse

                out = 0
                for pulse in module["memory"].values():
                    if not pulse:
                        out = 1
                        break

                for dest in module["destinations"]:
                    queue.append((module["name"], dest, out))


if __name__ == "__main__":
    file_path = "pulse.txt"
    data = {}
    rx = None
    with open(file_path) as file:
        for line in file:
            name, dest = line.split("->")
            name = name.strip()

            if name == "broadcaster":
                module_type = "broadcaster"
            else:
                module_type = "%" if name[0] == "%" else "&"
                name = name[1:]

            dest = [x.strip() for x in dest.split(",")]

            if module_type == "%":
                memory = False
            else:
                memory = {}

            data[name] = {"name": name, "type": module_type, "destinations": dest, "memory": memory}

            if dest == ["rx"]:
                rx = name
        
    solution2(data, rx)