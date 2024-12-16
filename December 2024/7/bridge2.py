def solve(equations):
    result = set()

    def dfs(target, idx, running, n):
        nonlocal result
        if idx == len(n):
            if running == target:
                result.add(target)
            return
        
        if running > target:
            return

        dfs(target, idx + 1, running + int(n[idx]), n)
        dfs(target, idx + 1, running * int(n[idx]), n)
        dfs(target, idx + 1, int(str(running) + n[idx]), n)

    for e in equations:
        target = int(e.split(': ')[0])
        numbers = e.split(': ')[1].split(' ')

        dfs(target, 1, int(numbers[0]), numbers)

    return sum(result)


if __name__ == '__main__':
    file = 'bridge.txt'
    input = []
    with open(file, 'r') as file:
        for line in file:
            input.append(line.strip())

    print(solve(input))