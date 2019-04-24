def cakes(recipe, available):

    if (len(recipe) > len(available)):
        return 0
    else:
        meow = {k: float(available[k])/recipe[k] for k in recipe.viewkeys() & available}
        print(meow)

        min_key = min(meow, key=meow.get)
        min_ans = meow[min_key]
        ans = min_ans//1
        return ans
