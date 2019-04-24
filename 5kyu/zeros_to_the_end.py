def move_zeros(array):
    ans = []
    count = 0
    for i in array:
        if (str(i) == "0" or str(i) == "0.0") and type(i) is not str:
            count += 1
        else:
            ans.append(i)
    zero_arr = [0 for i in range(count)]
    ans.extend(zero_arr)
    return ans
