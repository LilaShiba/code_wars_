def michael_pays(costs):
    if (costs < 5):
        return (round(costs,2))
    elif (costs <= 30):
        new_cost = costs *(2/3)
        return (round(new_cost,2))
    else:
        new_cost = costs - 10
        return(round(new_cost,2))
