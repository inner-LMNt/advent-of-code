def process(rules, part):
    state = 'in'
    
    while True:
        rule = rules[state]
        
        for cmd in rule.split(','):
            applies = True
            result = cmd
            
            if ':' in cmd:
                condition, result = cmd.split(':')
                var = condition[0]
                operation = condition[1]
                n = int(condition[2:])
                
                if operation == '>':
                    applies = part[var] > n
                else:
                    applies = part[var] < n
            
            if applies:
                if result == 'A':
                    return True
                if result == 'R':
                    return False
                state = result
                break

def solution1(parts, rules):
    total = 0

    for part_str in parts:
        part = {_.split('=')[0]: int(_.split('=')[1]) for _ in part_str[1:-1].split(',')}

        if process(rules, part):
            total += part['x'] + part['m'] + part['a'] + part['s']

    print(total)

if __name__ == "__main__":
    data = []
    with open('aplenty.txt', 'r') as file:
        data = file.read().strip()
    rules, parts = data.split('\n\n')
    
    rule_dict = {}
    for rule in rules.split('\n'):
        name, end = rule.split('{')
        rule_dict[name] = end[:-1]

    solution1(parts.split('\n'), rule_dict)

