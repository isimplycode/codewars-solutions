def expanded_form(num):
    place = []
    for i in range(0, len(str(num)), 1):
        if int(str(num)[::-1][i]) != 0:
            place.append(str(int(str(num)[::-1][i]) * 10**i))
    returnstr = ""
    for i in range(len(place)-1, -1, -1):
        if i == 0:
            returnstr += place[i]
        else:
            returnstr += f"{place[i]} + "
    return returnstr
