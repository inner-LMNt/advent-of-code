def parse_line(line):
    parts = line.strip().split(': ')
    game_id = int(parts[0].split()[1])
    subsets = [subset.split(', ') for subset in parts[1].split('; ')]
    
    return game_id, subsets

def calculate_min(game):
    max_red = max_green = max_blue = 0

    for subset in game:
        for cube in subset:
            count, color = cube.split()

            if color == 'red':
                max_red = max(max_red, int(count))
            elif color == 'green':
                max_green = max(max_green, int(count))
            elif color == 'blue':
                max_blue = max(max_blue, int(count))

    return [max_red, max_green, max_blue]

def find_power(filename):
    power = 0
    
    with open(filename, 'r') as file:
        for line in file:
            game_id, subsets = parse_line(line)
            
            mins = calculate_min(subsets)

            power += mins[0] * mins[1] * mins[2]

    
    return power

result = find_power('cube_conundrum.txt')

print("Sum of powers:", result)
