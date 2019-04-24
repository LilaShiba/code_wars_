def find_missing_letter(chars):
    x = 0
    while x < len(chars) - 1:
        if ord(chars[x+1]) - ord(chars[x]) > 1:
            return chr(ord(chars[x]) + 1)
        x += 1
