file_path = 'cards.txt'

hands = dict()
mapping = {'T': ':', 'J': ';', 'Q': '<', 'K': '=', 'A': '>'}

for line in open(file_path):
    l = line.strip().split()
    for i in range(len(l[0])):
        if l[0][i] in mapping:
            l[0] = l[0][:i] + mapping[l[0][i]] + l[0][i+1:]
    hands[l[0]] = l[1]

high_cards = []
pairs = []
two_pairs = []
three_of_a_kinds = []
full_houses = []
four_of_a_kinds = []
five_of_a_kinds = []

def check_full_house(map):
    has_three = False
    has_pair = False

    for k in map:
        if map[k] == 3:
            has_three = True
        elif map[k] == 2:
            has_pair = True

    return has_three and has_pair

def check_two_pair(map):
    num_pairs = 0

    for k in map:
        if map[k] == 2:
            num_pairs += 1

    return num_pairs == 2


for hand in hands:
    map = dict()
    for char in hand:
        map[char] = 0
    for char in hand:
        map[char] += 1

    for k in map:
        if len(map) == 1:
            five_of_a_kinds.append(hand)
            break
        elif len(map) == 2:
            if ';' in map:
                if map[';'] == 1 or map[';'] == 4:
                    five_of_a_kinds.append(hand)
                    break
            four_of_a_kinds.append(hand)
            break
        elif check_full_house(map):
            if ';' in map:
                if map[';'] == 2 or map[';'] == 3:
                    five_of_a_kinds.append(hand)
                    break
            full_houses.append(hand)
            break
        elif map[k] == 3:
            if ';' in map:
                if map[';'] == 1 or map[';'] == 3:
                    four_of_a_kinds.append(hand)
                    break
            three_of_a_kinds.append(hand)
            break
        elif check_two_pair(map):
            if ';' in map:
                if map[';'] == 2:
                    four_of_a_kinds.append(hand)
                    break
                if map[';'] == 1:
                    full_houses.append(hand)
                    break
            two_pairs.append(hand)
            break
        elif map[k] == 2:
            if ';' in map:
                if map[';'] == 1 or map[';'] == 2:
                    three_of_a_kinds.append(hand)
                    break
            pairs.append(hand)
            break
        elif map[k] == 1:
            if len(map) == 5:
                if ';' in map:
                    if map[';'] == 1:
                        pairs.append(hand)
                        break
                high_cards.append(hand)
                break

    if hand in five_of_a_kinds:
        if hand in four_of_a_kinds:
            four_of_a_kinds.remove(hand)
        if hand in full_houses:
            full_houses.remove(hand)
        if hand in three_of_a_kinds:
            three_of_a_kinds.remove(hand)
        if hand in two_pairs:
            two_pairs.remove(hand)
        if hand in pairs:
            pairs.remove(hand)
        if hand in high_cards:
            high_cards.remove(hand)
    elif hand in four_of_a_kinds:
        if hand in full_houses:
            full_houses.remove(hand)
        if hand in three_of_a_kinds:
            three_of_a_kinds.remove(hand)
        if hand in two_pairs:
            two_pairs.remove(hand)
        if hand in pairs:
            pairs.remove(hand)
        if hand in high_cards:
            high_cards.remove(hand)
    elif hand in full_houses:
        if hand in three_of_a_kinds:
            three_of_a_kinds.remove(hand)
        if hand in two_pairs:
            two_pairs.remove(hand)
        if hand in pairs:
            pairs.remove(hand)
        if hand in high_cards:
            high_cards.remove(hand)
    elif hand in three_of_a_kinds:
        if hand in two_pairs:
            two_pairs.remove(hand)
        if hand in pairs:
            pairs.remove(hand)
        if hand in high_cards:
            high_cards.remove(hand)
    elif hand in two_pairs:
        if hand in pairs:
            pairs.remove(hand)
        if hand in high_cards:
            high_cards.remove(hand)
    elif hand in pairs:
        if hand in high_cards:
            high_cards.remove(hand)

high_cards = list(set(high_cards))
pairs = list(set(pairs))
two_pairs = list(set(two_pairs))
three_of_a_kinds = list(set(three_of_a_kinds))
full_houses = list(set(full_houses))
four_of_a_kinds = list(set(four_of_a_kinds))
five_of_a_kinds = list(set(five_of_a_kinds))

five_of_a_kinds.sort()
four_of_a_kinds.sort()
full_houses.sort()
three_of_a_kinds.sort()
two_pairs.sort()
pairs.sort()
high_cards.sort()


total_cards = high_cards + pairs + two_pairs + three_of_a_kinds + full_houses + four_of_a_kinds + five_of_a_kinds

res = 0

for i in range(len(total_cards)):
    res += int(hands[total_cards[i]]) * (i+1)

print("five_of_a_kinds: ", five_of_a_kinds)
print("four_of_a_kinds: ", four_of_a_kinds)
print("full_houses: ", full_houses)
print("three_of_a_kinds: ", three_of_a_kinds)
print("two_pairs: ", two_pairs)
print("pairs: ", pairs)
print("high_cards: ", high_cards)

print(res)
print(len(total_cards))