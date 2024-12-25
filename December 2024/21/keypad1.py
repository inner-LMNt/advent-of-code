def solve(seq):
    numeric = {
        'A': (3, 2),
        '0': (3, 1),
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2)
    }

    directional = {
        '^': (0, 1),
        '<': (1, 0),
        'v': (1, 1),
        '>': (1, 2),
        'A': (0, 2)
    }

    def is_any_of(item, *args):
        for a in args:
            if item == a:
                return True
        return False

    def dfs_num(s, path, idx, p):
        if idx == len(s) - 1:
            p.append(''.join(path))
            return

        y1, x1 = numeric[s[idx]]
        y2, x2 = numeric[s[idx + 1]]

        y_mov = y2 - y1
        x_mov = x2 - x1

        horz = '<' if x_mov < 0 else '>'
        vert = '^' if y_mov < 0 else 'v'

        if is_any_of((s[idx], s[idx + 1]), ('A', '1'), ('A', '4'), ('A', '7'), ('0', '1'), ('0', '4'), ('0', '7')):
            path.append('^' * abs(y_mov) + '<' * abs(x_mov) + 'A')
            dfs_num(s, path, idx + 1, p)

        elif is_any_of((s[idx], s[idx + 1]), ('1', 'A'), ('4', 'A'), ('7', 'A'), ('1', '0'), ('4', '0'), ('7', '0')):
            path.append('>' * abs(x_mov) + 'v' * abs(y_mov) + 'A')
            dfs_num(s, path, idx + 1, p)

        elif y_mov == 0 or x_mov == 0:
            if y_mov == 0:
                path.append(horz * abs(x_mov))
            if x_mov == 0:
                path.append(vert * abs(y_mov))
            path.append('A')
            dfs_num(s, path, idx + 1, p)

        else:
            o_len = len(path)
            path.append(vert * abs(y_mov) + horz * abs(x_mov) + 'A')
            dfs_num(s, path, idx + 1, p)

            while len(path) > o_len:
                path.pop()

            path.append(horz * abs(x_mov) + vert * abs(y_mov) + 'A')
            dfs_num(s, path, idx + 1, p)

    def dfs_dir(s, path, idx, p):
        if idx == len(s) - 1:
            p.append(''.join(path))
            return

        y1, x1 = directional[s[idx]]
        y2, x2 = directional[s[idx + 1]]

        y_mov = y2 - y1
        x_mov = x2 - x1

        horz = '<' if x_mov < 0 else '>'
        vert = '^' if y_mov < 0 else 'v'

        if is_any_of((s[idx], s[idx + 1]), ('<', 'A'), ('<', '^')):
            path.append('>' * abs(x_mov) + '^' * abs(y_mov) + 'A')
            dfs_dir(s, path, idx + 1, p)

        elif is_any_of((s[idx], s[idx + 1]), ('A', '<'), ('^', '<')):
            path.append('v' * abs(y_mov) + '<' * abs(x_mov) + 'A')
            dfs_dir(s, path, idx + 1, p)

        elif y_mov == 0 or x_mov == 0:
            if y_mov == 0:
                path.append(horz * abs(x_mov))
            if x_mov == 0:
                path.append(vert * abs(y_mov))
            path.append('A')
            dfs_dir(s, path, idx + 1, p)

        else:
            o_len = len(path)
            path.append(vert * abs(y_mov) + horz * abs(x_mov) + 'A')
            dfs_dir(s, path, idx + 1, p)

            while len(path) > o_len:
                path.pop()

            path.append(horz * abs(x_mov) + vert * abs(y_mov) + 'A')
            dfs_dir(s, path, idx + 1, p)

    paths = []
    dfs_num('A' + seq, [], 0, paths)

    paths_1 = []
    for a in paths:
        dfs_dir('A' + a, [], 0, paths_1)

    paths = []
    for a in paths_1:
        dfs_dir('A' + a, [], 0, paths)

    return min([len(x) for x in paths]) * int(seq[:3])

if __name__ == '__main__':
    file = 'keypad.txt'
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append(line.strip())

    print(sum([solve(x) for x in data]))  # 203734
