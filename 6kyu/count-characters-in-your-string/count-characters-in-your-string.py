def count(string):
    hash = {}
    for i in string:
        if i in hash:
            hash[i] += 1
        else: 
            hash[i] = 1
    return hash
