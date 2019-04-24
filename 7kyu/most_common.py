def most_frequent_item_count(collection):
    highest = 0
    for o_count in collection:
        i_highest = 0
        for i_count in collection:
            if i_count == o_count:
                i_highest += 1
        if i_highest > highest:
            highest = i_highest
    return highest
