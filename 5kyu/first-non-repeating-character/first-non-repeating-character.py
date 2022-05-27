def first_non_repeating_letter(string):
    characters = {}
    first_instance = {}
    for i in range(0,len(string), 1):
        if string[i].lower() not in first_instance:
            first_instance[string[i].lower()] = i
        if string[i].lower() in characters:
            characters[string[i].lower()] += 1
        else:
            characters[string[i].lower()] = 1 
    for i in characters:
        if characters[i] == 1:
            return string[first_instance[i]]
    return ""
