file_path = "seeds.txt"
seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
locations = []

with open(file_path, "r") as f:
    seeds = f.readline().split()
    seeds.pop(0)

    f.readline()
    f.readline()

    line = f.readline().split()
    while line[0].find('-') == -1:
        seed_to_soil.append(line)
        line = f.readline().split()
        if line == []:
            line = f.readline().split()

    line = f.readline().split()
    while line[0].find('-') == -1:
        soil_to_fertilizer.append(line)
        line = f.readline().split()
        if line == []:
            line = f.readline().split()

    line = f.readline().split()
    while line[0].find('-') == -1:
        fertilizer_to_water.append(line)
        line = f.readline().split()
        if line == []:
            line = f.readline().split()

    line = f.readline().split()
    while line[0].find('-') == -1:
        water_to_light.append(line)
        line = f.readline().split()
        if line == []:
            line = f.readline().split()

    line = f.readline().split()
    while line[0].find('-') == -1:
        light_to_temperature.append(line)
        line = f.readline().split()
        if line == []:
            line = f.readline().split()

    line = f.readline().split()
    while line[0].find('-') == -1:
        temperature_to_humidity.append(line)
        line = f.readline().split()
        if line == []:
            line = f.readline().split()

    line = f.readline().split()
    while line:
        humidity_to_location.append(line)
        line = f.readline().split()
        if line == []:
            line = f.readline().split()

    f.close()   
    
def update_seed(up_seed, map_list):
    for map in map_list:
        if up_seed >= int(map[1]) and up_seed < int(map[1]) + int(map[2]):
            return int(map[0]) + up_seed - int(map[1])
    return up_seed

for seed in seeds:
    up_seed = int(seed)
    up_seed = update_seed(up_seed, seed_to_soil)
    up_seed = update_seed(up_seed, soil_to_fertilizer)
    up_seed = update_seed(up_seed, fertilizer_to_water)
    up_seed = update_seed(up_seed, water_to_light)
    up_seed = update_seed(up_seed, light_to_temperature)
    up_seed = update_seed(up_seed, temperature_to_humidity)
    up_seed = update_seed(up_seed, humidity_to_location)

    locations.append(up_seed)

print("Locations: ", locations)
print("Min:", min(locations))