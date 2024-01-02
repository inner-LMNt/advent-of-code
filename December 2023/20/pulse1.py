def solution1(input):
    for name, module in input.items():
        for dest in module["destinations"]:
            if dest in input and input[dest]["type"] == "&":
                input[dest]["memory"][name] = 0

    low = 0
    high = 0

    for _ in range(1000):
        low += 1
        queue = [ ("broadcaster", x, 0) for x in input["broadcaster"]["destinations"] ]
        index = 0

        while index < len(queue):
            src, dest, pulse = queue[index]
            index += 1

            if pulse == 0:
                low += 1
            else:
                high += 1

            if dest not in input:
                continue

            module = input[dest]

            if module["type"] == "%":
                if not pulse:
                    module["memory"] = not module["memory"]
                    out = 1 if module["memory"] else 0
                    for dest in module["destinations"]:
                        queue.append((module["name"], dest, out))
            else:
                module["memory"][src] = pulse

                out = 0
                for pulse in module["memory"].values():
                    if not pulse:
                        out = 1
                        break

                for dest in module["destinations"]:
                    queue.append((module["name"], dest, out))

    print(low * high)


if __name__ == "__main__":
    file_path = "pulse.txt"
    data = {}
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
        
    solution1(data)
