def count_ways(dots, blocks, dot_index, block_index, current, dp):    
    if (dot_index, block_index, current) in dp:
        return dp[(dot_index, block_index, current)]
    
    if dot_index == len(dots):
        if (block_index == len(blocks) and current == 0) or (block_index == len(blocks)-1 and blocks[block_index] == current):
            return 1
        else:
            return 0
    
    count = 0
    for c in ['#', '.']:
        if dots[dot_index] == c or dots[dot_index] == '?':
            if c == '#':
                count += count_ways(dots, blocks, dot_index+1, block_index, current+1, dp)
            elif c == '.' and current == 0:
                count += count_ways(dots, blocks, dot_index+1, block_index, 0, dp)
            elif block_index < len(blocks) and blocks[block_index] == current:
                count += count_ways(dots, blocks, dot_index+1, block_index+1, 0, dp)
    
    dp[(dot_index, block_index, current)] = count
    return count

def solution2(input):
    lines = input.split('\n')
    count = 0

    for line in lines:
        dots, blocks = line.split()
        dots = '?'.join([dots]*5)
        blocks = ','.join([blocks]*5)
        blocks = [int(x) for x in blocks.split(',')]
        dp = {}

        ways = count_ways(dots, blocks, 0, 0, 0, dp)
        count += ways

    print(count)

if __name__ == "__main__":
    file_path = 'onsen.txt'
    data = []
    with open(file_path, 'r') as file:
        data = file.read().strip()

    solution2(data)
