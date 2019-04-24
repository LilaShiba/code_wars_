def getCount(inputStr):
    num_vowels = 0
    vowels = ["a", "e", "i", "o", "u"]
    # your code here
    for x in inputStr:
        if x in vowels:
            num_vowels += 1
    return num_vowels
