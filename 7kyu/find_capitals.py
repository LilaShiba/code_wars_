def capitals(word):
    cap = []
    for i in range(len(word)):
        if word[i].isupper():
            cap.append(i)
    return cap
    #your code here
