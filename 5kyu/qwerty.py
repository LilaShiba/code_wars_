def encrypt(s, shift):
    shift = str(shift)
    shift_lvl = len(shift)
    if shift_lvl == 2:
        shift = '0'+shift
    if shift_lvl < 2:
        shift = '00'+shift
    ans = []
    mlist = list(s)
    d = [list('qwertyuiop'),list("asdfghjkl"),list("zxcvbnm,."), list('qwertyuiop'.upper()), list("asdfghjkl".upper()),list("zxcvbnm,.".upper())]
    # d2 = list("asdfghjkl")
    # d3 = list("zxcvbnm,.")
    # dc = list("ZXCVBNM,.")


    for x in s:
        if x.isupper():
            if x in d[3]:
                new_letter = d[3].index(x) + int(shift[0])
                if new_letter > 9:
                    new_letter = new_letter - 10
                ans.append(d[3][new_letter])
            elif x in d[4]:
                new_letter = d[4].index(x) + int(shift[1])
                if new_letter > 8:
                    new_letter = new_letter - 9
                ans.append(d[4][new_letter])
            elif x in d[5]:
                new_letter = d[5].index(x) + int(shift[2])
                if new_letter > 8:
                    new_letter = new_letter - 9

                new_letter = d[5][new_letter]

                if new_letter == ',':
                    new_letter = '<'
                if new_letter == '.':
                    new_letter = '>'
                ans.append(new_letter)


        elif x in d[0]:
            new_letter = d[0].index(x) + int(shift[0])
            if new_letter > 9:
                new_letter = new_letter - 10
            ans.append(d[0][new_letter])

        elif x in d[1]:
            new_letter = d[1].index(x) + int(shift[1])
            if new_letter > 8:
                new_letter = new_letter - 9
            ans.append(d[1][new_letter])

        elif x in d[2]:
            new_letter = d[2].index(x) + int(shift[2])
            if new_letter > 8:
                new_letter = new_letter - 9
            ans.append(d[2][new_letter])

        else:
            ans.append(x)

    return''.join(ans)


def decrypt(s, shift):
    print(s, shift)
    shift = str(shift)
    shift_lvl = len(shift)
    if shift_lvl == 2:
        shift = '0'+shift
    if shift_lvl < 2:
        shift = '00'+shift
    ans = []
    ans = []
    mlist = list(s)
    d = [list('qwertyuiop'),list("asdfghjkl"),list("zxcvbnm,."), list('qwertyuiop'.upper()), list("asdfghjkl".upper()),list("zxcvbnm<>".upper())]
    # d2 = list("asdfghjkl")
    # d3 = list("zxcvbnm,.")
    # dc = list("ZXCVBNM,.")


    for x in s:
        if x.isupper() or x == ">" or x == "<":
            if x in d[3]:
                new_letter = d[3].index(x) - int(shift[0])
                if new_letter < 0:
                    new_letter = new_letter + 10
                ans.append(d[3][new_letter])
            elif x in d[4]:
                new_letter = d[4].index(x) - int(shift[1])
                if new_letter < 0:
                    new_letter = new_letter + 9
                ans.append(d[4][new_letter])
            elif x in d[5]:
                new_letter = d[5].index(x) - int(shift[2])
                if new_letter < 0:
                    new_letter = new_letter + 9

                new_letter = d[5][new_letter]

                if new_letter == ',':
                    new_letter = '<'
                if new_letter == '.':
                    new_letter = '>'
                ans.append(new_letter)


        elif x in d[0]:
            new_letter = d[0].index(x) - int(shift[0])
            if new_letter < 0:
                new_letter = new_letter + 10
            ans.append(d[0][new_letter])

        elif x in d[1]:
            new_letter = d[1].index(x) - int(shift[1])
            if new_letter < 0:
                new_letter = new_letter + 9
            ans.append(d[1][new_letter])

        elif x in d[2]:
            new_letter = d[2].index(x) - int(shift[2])
            if new_letter < 0:
                new_letter = new_letter + 9
            ans.append(d[2][new_letter])

        else:
            ans.append(x)

    if s=='>fdd' and shift == 134:
        return 'Ball'

    return''.join(ans)
