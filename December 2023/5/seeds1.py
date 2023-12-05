file_path = "0.txt"
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

    print("seeds:", seeds)
    print("seed_to_soil:", seed_to_soil)
    print("soil_to_fertilizer:", soil_to_fertilizer)
    print("fertilizer_to_water:", fertilizer_to_water)
    print("water_to_light:", water_to_light)
    print("light_to_temperature:", light_to_temperature)
    print("temperature_to_humidity:", temperature_to_humidity)
    print("humidity_to_location:", humidity_to_location)
    


for seed in seeds:
    up_seed = int(seed)
    print("up_seed: ", up_seed)

    for map in seed_to_soil:
        if up_seed >= int(map[1]) and up_seed < int(map[1]) + int(map[2]):
            up_seed = int(map[0]) + up_seed - int(map[1])
            print("Map used:", map)
            break
    print("up_seed1: ", up_seed)
    
    for map in soil_to_fertilizer:
        if up_seed >= int(map[1]) and up_seed < int(map[1]) + int(map[2]):
            up_seed = int(map[0]) + up_seed - int(map[1])
            print("Map used:", map)
            break
    print("up_seed2: ", up_seed)

    for map in fertilizer_to_water:
        if up_seed >= int(map[1]) and up_seed < int(map[1]) + int(map[2]):
            up_seed = int(map[0]) + up_seed - int(map[1])
            print("Map used:", map)
            break
    print("up_seed3: ", up_seed)

    for map in water_to_light:
        if up_seed >= int(map[1]) and up_seed < int(map[1]) + int(map[2]):
            up_seed = int(map[0]) + up_seed - int(map[1])
            print("Map used:", map)
            break
    print("up_seed4: ", up_seed)

    for map in light_to_temperature:
        if up_seed >= int(map[1]) and up_seed < int(map[1]) + int(map[2]):
            up_seed = int(map[0]) + up_seed - int(map[1])
            print("Map used:", map)
            break
    print("up_seed5: ", up_seed)

    for map in temperature_to_humidity:
        if up_seed >= int(map[1]) and up_seed < int(map[1]) + int(map[2]):
            up_seed = int(map[0]) + up_seed - int(map[1])
            print("Map used:", map)
            break
    print("up_seed6: ", up_seed)

    for map in humidity_to_location:
        if up_seed >= int(map[1]) and up_seed < int(map[1]) + int(map[2]):
            up_seed = int(map[0]) + up_seed - int(map[1])
            print("Map used:", map)
            break
    print("Final up_seed: ", up_seed)

    locations.append(up_seed)

print("Locations: ", locations)
print("Min:", min(locations))