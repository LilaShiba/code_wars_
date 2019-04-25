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


def easy(arr):
    return sorted(arr)

arr = [[0, 0], [5, 3], [0, 5], [0, 3]]
    # [[0, 0], [0, 5], [5, 3]]
print(merge_sort(arr))
print(easy(arr))
