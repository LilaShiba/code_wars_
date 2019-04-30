# https://algorithmtutor.com/Computational-Geometry/Determining-if-two-consecutive-segments-turn-left-or-right/
def cross_product(p1,p2):
    return p1[0] * p2[1] - p2[0] * p1[1]

def direction(p1,p2,p3):
    cross_product(p3.substract(p1), p2.substrct(p1))

def left(p1,p2,p3):
    return direction(p1,p2,p3) < 0

def right(p1,p2,p3):
    return direction(p1,p2,p3) > 0

def collinear(p1,p2,p3):
    return direction(p1,p2,p3) == 0

def merge_sort(arr,pos):
    if len(arr) > 1:
        mid = len(arr)//2
        l_half = arr[:mid]
        r_half = arr[mid:]

        merge_sort(l_half, pos)
        merge_sort(r_half, pos)

        li = ri = k = 0
        # two pointers to stitch together new array
        while li < len(l_half) and ri < len(r_half):
            if l_half[li][pos] < r_half[ri][pos]:
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

#  find the leftmost point and add it to the convex hull vertices in each pass.
def jarvis_march(points):
    sorted_by_x = merge_sort(points)
    min_x = sorted_by_x[0]
    index = points.index(min_x)

    l = index
    result = []
    result.append(min_x)

    while (True):
        q = (l+1) % len(points)
        for i in range(len(points)):
            if i == l:
                continue
            d = direction(points[l], points[i], points[q])
            if d > 0:
                q = i

        l = q
        if l == index:
            break
        result.append(points[q])
