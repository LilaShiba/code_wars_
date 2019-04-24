def pos_average(s):
    values = s.split(", ")
    count, total = 0, 0
    for i in range(len(values)-1):
        for j in range(i+1,len(values)):
            for k in range(len(values[i])):
                if values[i][k] == values[j][k]: count += 1
                total += 1
    return count / total * 100
