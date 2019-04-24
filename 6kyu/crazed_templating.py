def letter_pattern(w):
    if len(w) == 1:
        return w[0]
    else:
        ans = []
        i = 0
        while i < len(w[0]):
            sample = w[0][i]

            j = 1
            c = 1

            while j < len(w):
                if sample != w[j][i]:
                    c = 0
                    ans.append('*')
                    break
                j += 1

            if c:
                ans.append(sample)

            i += 1
        return ''.join(ans)
