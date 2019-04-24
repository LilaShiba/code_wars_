def freq_seq(s, sep):
    done = []
    for x in s:
        done.append(str(s.count(x)))
    return sep.join(done)
