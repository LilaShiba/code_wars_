import math
def brute_force(points):
    if len(points) == 2:
        return points
    best = (points[0], points[1])
    past_score = 100
    count = 1
    for x,y in points[count-1:]:
        for i,j in points[count:-1]:
            # manhattan distance
            score = abs(x - i) + abs(y -j)
            # euclidean distance
            #score = math.sqrt( (x-i)**2 + (y-j)**2 )
            if score < past_score:
                best = ((x,y), (i,j))
                past_score = score
                #print(best)
        count +=1
    return(best)

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

def cp_helper(X,Y):
  length = len(X)
  # base case

  if length <= 3:
    return brute_force(X)

  # get median
  mid = (length)//2
  # sort x cords by pos to median
  xl = X[:mid]
  xr = X[mid:]
  # sort y cords of the sorted x cords
  # yl = [x for x in Y if x in xl]
  # yr = [x for x in Y if x in xr]

  yl,yr = [],[]

  midpoint = X[mid][0]

  for x in Y:
    if x[0] <= midpoint:
          yl.append(x)
    else:
        yr.append(x)

  # divide recursively
  (pl, ql) = cp_helper(xl,yl)
  (pr, qr) = cp_helper(xr,yr)


  # distance
  dl = math.sqrt((pl[0]- ql[0])**2 + (pl[1] - ql[1])**2)
  dr = math.sqrt((pr[0]- qr[0])**2 + (pr[1] - qr[1])**2)

  # finding min points for left and right halves
  d = min(dl,dr)

  # points in y where x-cord is within d of mid
  ys = [x for x in Y if x[0] - d <= X[mid][0]]

  # checking points that cross left/right line for min
  e = 1000000

  for i in range(len(ys)-1):
    p = ys[i]
    new_min = min(i+7, len(ys))
    new_loop = ys[i+1:new_min]
    for q in ys[i+1:new_min]:
      loop_dist = math.sqrt( ( p[0]- q[0] )**2 + ( p[1] - q[1] )**2 )
      if e > loop_dist:
        e = loop_dist
        pp = p
        qq = q

  if e < d:
    return(pp,qq)
  elif dr < dl:
    return(pr,qr)
  else:
    return(pl,ql)



def closest_pair(points):
    if len(points) <= 2:
        return points

    if len(points) <= 3:
        # no need for divide_conquer if n < 3
        return brute_force(points)
    else:
        # preprocess arrays to make life easier and faster

        # sort by x cords & sort by y cords
        arr_x = list(points)
        arr_y = list(points)
        # Do everything yourself because otherwise what do you learn?
        # Run merge sort as it is O(nlogn)
        # pass in arr and pos of where to sort, e.g. x or y
        # sorted_x = merge_sort(arr_x,0)
        # sorted_y = merge_sort(arr_y,1)

        # the pythonic way
        arr_x.sort(key=lambda x: x[0])
        arr_y.sort(key=lambda x: x[1])

        # Basic visual test passes
        # print(sorted_x)
        # print(sorted_y)

        # pass the dirty work to
        return cp_helper(arr_x,arr_y)
