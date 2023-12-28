def update(ch_index, greater_than, value, ranges):
    result = []

    for r in ranges:
        r = list(r)
        low, high = r[ch_index]
        if greater_than:
            low = max(low, value + 1)
        else:
            high = min(high, value - 1)
        if low <= high:
            r[ch_index] = (low, high)
            result.append(tuple(r))

    return result

def solution2(workflow):
    condition = workflow[0]

    if condition == "R":
        return []
    if condition == "A":
        return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
    if ":" not in condition:
        return solution2(workflow_dict[condition].split(","))
    
    condition = condition.split(":")
    greater_than = ">" in condition[0]
    less_than = "<" in condition[0]
    c = condition[0][0]
    value = int(condition[0][2:])

    true_branch = update('xmas'.index(c), greater_than, value, solution2([condition[1]]))

    false_branch = update('xmas'.index(c), less_than, value + 1 if greater_than else value - 1, solution2(workflow[1:]))

    return true_branch + false_branch

if __name__ == "__main__":
    file_path = 'aplenty.txt'
    input = []
    with open(file_path) as file:
        input = file.read().strip().split("\n\n")
    workflow, _ = input

    workflow_lines = workflow.split("\n")
    workflow_dict = {line.split("{")[0]: line.split("{")[1][:-1] for line in workflow_lines}

    result = 0
    for acceptance_range in solution2(workflow_dict["in"].split(",")):
        product = 1
        for low, high in acceptance_range:
            product *= (high - low + 1)
        result += product

    print(result)
