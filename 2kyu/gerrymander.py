# O = your voters

# fun fact from source below
# The word ”gerrymander” was coined in 1812 after Massachusetts
# governor Elbridge Gerry signed into law a salamander-shaped
# district.

# great resource for DP https://www.cs.upc.edu/~mjserna/docencia/grauA/P17/ProgramacioDinamica.pdf
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

def convext_hull(pointlist):
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

def gerrymander(s):
    print(s)
    # transform into 2D array
    matrix = []
    for x in s:
        x = list(x)
        matrix.append(x)

    # solve
    #  Voronoi Approach
    #  Bowyer-Watson algorithm
    #  Fortune's algorithm




    # return ans
    ans = []
    for x in matrix:
        new_x = ''.join(x)
        ans.append(new_x)
    ans = '\n'.join(ans)
    return ans



example_test =[
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX'
        ]

print(gerrymander(example_test))
