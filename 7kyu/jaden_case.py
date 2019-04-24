def toJadenCase(s):
    jaden = ' '.join(s[0].upper() + s[1:] for s in s.split())
    return jaden
