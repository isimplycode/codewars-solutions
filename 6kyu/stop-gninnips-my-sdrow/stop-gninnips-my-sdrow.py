def spin_words(sentence):
    sentence_array = sentence.split(" ");
    new_string = ""
    for i in sentence_array:
        if len(str(i)) >= 5:
            if new_string != "":
                new_string = new_string + " " + i[::-1]
            else:
                new_string = new_string + i[::-1]
        else:
            if new_string != "":
                new_string = new_string + " " + i
            else:
                new_string = new_string + i
    return new_string
