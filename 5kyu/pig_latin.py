def pig_it(text):
    new_text = text.split(' ')
    temp_array = []
    new_string = ''

    for x in new_text:
        new_string = x
        if x.isalpha():
            word = new_string[1:] + new_string[0] + "ay"
        else:
            word = x
        temp_array.append(word)
        new_string = []
    return(" ".join(temp_array))
