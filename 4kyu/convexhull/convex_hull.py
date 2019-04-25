import math
def cross_product(o,a,b):
    return( a[0] - o[0]) * (b[1]- o[1]) - (a[1]-o[1]) * (b[0] - o[0])


# merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l_half = arr[:mid]
        r_half = arr[mid:]

        merge_sort(l_half)
        merge_sort(r_half)

        li = ri = k = 0
        # two pointers to stitch together new array
        while li < len(l_half) and ri < len(r_half):
            if (l_half[li][0] + l_half[li][1]) < (r_half[ri][0] + r_half[ri][1]):
                arr[k] = l_half[li]
                li +=1
            else:
                arr[k] = r_half[ri]
                ri +=1
            k+=1
        # the invarient is that you merge two sorted lists
        # so, this makes sure you merge both lists brah
        while li < len(l_half):
            arr[k] = l_half[li]
            li+=1
            k+=1
        while ri < len(r_half):
            arr[k] = r_half[ri]
            ri+=1
            k+=1

    return arr
def remove_dups(arr):
    no_dups = []
    for x in arr:
        if x not in no_dups:
            no_dups.append(x)
    return no_dups




# gift wrap
def hull_method(pointlist):
    # remove dups
    #points = remove_dups(pointlist)
    # get ride of colinear
    points = merge_sort(pointlist)
    lower = []

    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <=0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]
