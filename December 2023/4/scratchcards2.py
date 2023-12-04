file_path = 'scratchcards.txt'

def process_file_array(file_path):
    file = open(file_path, 'r')
    array = file.readlines()
    file.close()
    result = []

    for i in range(len(array)):
        array[i] = array[i][:-1]
        parts = array[i].split(':')

        numbers = parts[1].split('|')
        winning_numbers = [x for x in numbers[0].split(' ') if x != '']
        your_numbers = [x for x in numbers[1].split(' ') if x != '']
        result.append([winning_numbers, your_numbers])

    return result

def process_file(array):
    n = len(array)
    dp = [1 for _ in range(n)]

    for i in range(n):
        count = 0
        winning_set = set(array[i][0])
        for num in array[i][1]:
            if num in winning_set:
                count += 1
        for j in range(1, count+1):
            dp[i+j] += dp[i]

        print("Count:", count, "DP:", dp)
        print("Won", count * dp[i], "cards")

    return sum(dp)           
        

ans = process_file_array(file_path)
print("Result:", process_file(ans))