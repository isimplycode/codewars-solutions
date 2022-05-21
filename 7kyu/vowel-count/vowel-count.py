def get_count(sentence):
    returnvalue = 0;
    for i in sentence:
        if i in "aeiou":
            returnvalue += 1
    return returnvalue
