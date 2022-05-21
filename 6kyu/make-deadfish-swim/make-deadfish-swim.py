def parse(data):
    num = 0
    arr = []
    for i in data:
        if i == "i":
            num += 1
        if i == "d":
            num -= 1
        if i == "s":
            num = num**2
        if i == "o":
            arr.append(num)
    return arr
