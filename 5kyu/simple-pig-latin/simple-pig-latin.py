def pig_it(text):
    text = text.split(" ")
    res = ""
    for i in text:
        if i in ["!", ".", "?"]:
            res += " " + i
        elif res == "":
            res += i[1:len(i)] + i[0] + "ay"
        else:
            res += " " +i[1:len(i)] + i[0] + "ay"
    return res
