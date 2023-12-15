def solution1(input):
    box_map = [[] for _ in range(256)]
    total = 0

    for line in input:
        hash = 0
        to_set = False

        for c in line:
            if c == '=':
                to_set = True
                break
            if c == '-':
                break
            ascii = ord(c)
            hash += ascii
            hash = (hash * 17) % 256
        
        not_replace = True
        if to_set:
            for i, box in enumerate(box_map[hash]):
                if box[:-1] == line[:-1]:
                    box_map[hash][i] = line
                    not_replace = False
                    break
            if not_replace:
                box_map[hash].append(line)
        else:
            for i, box in enumerate(box_map[hash]):
                if box[:-2] == line[:-1]:
                    box_map[hash].pop(i)
                    break

    for i, box in enumerate(box_map):
        for j, line in enumerate(box):
            total += (1 + j) * (1 + i) * int(line[-1])
            
        
        
    print(total)

if __name__ == '__main__':
    input = open('lens.txt', 'r').read()
    input = input.split(',')

    solution1(input)