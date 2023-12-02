def parse_line(line):
    parts = line.strip().split(': ')
    game_id = int(parts[0].split()[1])
    subsets = [subset.split(', ') for subset in parts[1].split('; ')]
    
    return game_id, subsets

def is_game_possible(game, red, green, blue):
    current_red = current_green = current_blue = 0

    for subset in game:
        for cube in subset:
            count, color = cube.split()

            if color == 'red':
                current_red = int(count)
            elif color == 'green':
                current_green = int(count)
            elif color == 'blue':
                current_blue = int(count)
            if current_red > red or current_green > green or current_blue > blue:
                return False

    return True

def find_possible_games(filename, red, green, blue):
    possible_games = []
    
    with open(filename, 'r') as file:
        for line in file:
            game_id, subsets = parse_line(line)
            
            print("Checking game", game_id)
            if is_game_possible(subsets, red, green, blue):
                possible_games.append(game_id)
                print("Game", game_id, "is possible")
    
    return possible_games

result = find_possible_games('cube_conundrum.txt', 12, 13, 14)

print("Sum of IDs of possible games:", sum(result))
