def move_zeros(array):
    returnarr = []
    zeroes = []
    for i in array:
        if i != 0:
            returnarr.append(i)
        else:
            zeroes.append(0)
    returnarr.extend(zeroes)
    return returnarr
