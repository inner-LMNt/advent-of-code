file_path = 'scratchcards.txt'

def process_file(file_path):
    total_score = 0

    for line in open(file_path, 'r'):
        line = line[:-1]
        score = 0
        parts = line.split(':')

        numbers = parts[1].split('|')
        winning_numbers = [x for x in numbers[0].split(' ') if x != '']
        your_numbers = [x for x in numbers[1].split(' ') if x != '']
        winning_set = set(winning_numbers)
        your_set = set(your_numbers)

        print("Winning numbers:", winning_numbers)
        print("Your numbers:", your_numbers)

        for num in winning_numbers:
            winning_set.add(num)
        for num in your_numbers:
            your_set.add(num)

        for num in your_set:
            if num in winning_set:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        total_score += score

    return total_score

print("Score:", process_file(file_path))