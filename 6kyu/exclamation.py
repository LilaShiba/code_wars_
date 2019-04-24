def balance(left, right):
    yas = 0
    wha = 0
    yas_r = 0
    wha_r = 0

    for x in left:
        if x == "!":
            yas = yas + 2
        else:
            wha = wha + 3
    left_weight = wha + yas
    print(left_weight)

    for x in right:
        if x == "!":
            yas_r = yas_r + 2
        else:
            wha_r = wha_r + 3
    right_weight = wha_r + yas_r

    if right_weight > left_weight:
        return "Right"
    elif right_weight < left_weight:
        return "Left"
    else:
        return "Balance"
