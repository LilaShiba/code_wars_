def unique_in_order(iterable):
    previous = None
    new_list = []
    for x in iterable:
        if x != previous:
            new_list.append(x)
        previous = x
    return new_list
