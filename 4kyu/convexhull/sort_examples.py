# merge sort
def merge_sort(arr, pos):
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
