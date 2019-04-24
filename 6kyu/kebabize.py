def kebabize(s):
    new = list(s)
    new_list = []
    # take out caps and replace with - and lower case
    for i in new:
        if i.isupper():
            i = "-"+i.lower()
        new_list.append(i)
    # add it all together
    new_list = ''.join(new_list)
    # remove numbers
    done = ''.join(i for i in new_list if not i.isdigit())
    return done.strip('- ')
