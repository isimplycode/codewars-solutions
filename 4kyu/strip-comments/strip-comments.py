def strip_comments(strng, markers):
    x = strng.split("\n")
    arr = []
    for i in x:
        appendstr = ""
        for j in i:
            if j in markers:
                break
            appendstr += j
        arr.append(appendstr)
    newarr = []
    for i in arr:
        newarr.append(i.rstrip())
    return ("\n".join(newarr))
