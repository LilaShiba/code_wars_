def increment_string(strg):
    nums = []
    char = []
    ints = list('1234567890')
    # if no input
    if strg == '':
        return strg + '1'
    # seperate nums and chars in reverse order
    for x in reversed(strg):
        if x in ints:
            nums.append(x)
        else:
            break
    nums.reverse()
    print(nums)
    split_amount = abs((len(nums)- len(strg)))

    chars = strg[0:split_amount]
    chars = ''.join(chars)
    # if no nums
    if not nums:
        return chars + '1'
    # if no leading zero's
    elif nums[0] != '0':
        nums = int(''.join(nums)) + 1
        temp = str(nums)
        return chars + temp

    # if leading zero's
    else:
        before_len = len(nums)
        make_int = int(''.join(nums)) + 1
        after_len = len(str(make_int))
        print(before_len, after_len)
        loop_by = before_len - after_len
        if before_len == after_len:
            ans = ''
            for x in range(before_len):
                ans = '0' + ans
            return chars + ans + str(make_int)

        else:
            ans = ''
            for x in range(loop_by):
                ans = '0' + ans
            return chars + ans + str(make_int)
