def solution1(input):
    total = 0

    for line in input:
        count = 0
        for c in line:
            ascii = ord(c)
            count += ascii
            count = (count * 17) % 256
        total += count
        
    print(total)

if __name__ == '__main__':
    input = open('lens.txt', 'r').read()
    input = input.split(',')

    solution1(input)