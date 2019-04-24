def anagrams(word, words):
    gold = []
    ans = []
    for x in word:
        gold.append(x)



    for x in words:
        if sorted(x) == sorted(gold):
            ans.append(x)

    return(ans)
