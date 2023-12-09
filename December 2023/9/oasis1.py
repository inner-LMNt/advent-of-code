def solution1(arr):
    temparr = arr.split(" ")
    n = len(temparr)
    result = int(temparr[n-1])

    while temparr.count("0") != len(temparr):
        for i in range(n-1):
            temparr[i] = str(int(temparr[i+1]) - int(temparr[i]))
        result += int(temparr[i])
        n -= 1
        temparr.pop()

    return result
    

if __name__ == '__main__':
    file = open("oasis.txt", "r")
    lines = []

    for line in file:
        lines.append(line.strip())

    result = 0
    for line in lines:
        result += solution1(line)
        
    print(result)
    