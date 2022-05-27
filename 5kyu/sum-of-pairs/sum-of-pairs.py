def sum_pairs(ints, s):
    map = {}
    for i in ints:
        if s-i in map:
            return [s-i, i]
        map[i] = 0
    return None
