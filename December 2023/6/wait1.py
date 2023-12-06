file_path = '0.txt'

times = []
distance = []

with open(file_path, 'r') as f:
    for line in f:
        if line.startswith('Time:'):
            times = [int(x) for x in line.split()[1:]]
        elif line.startswith('Distance:'):
            distance = [int(x) for x in line.split()[1:]]
        
total = 1

for i in range(len(times)):
    count = 0
    for time in range(times[i]+1):
        if (times[i]-time) * time > distance[i]:
            count += 1
    
    total *= count

print(total)