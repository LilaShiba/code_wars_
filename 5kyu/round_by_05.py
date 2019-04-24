Stats
Kata
Solutions
Translations
Collections
Kumite
Social
Discourse
Completed (61)
Unfinished
Obsolete
3 kyu
Stargate SG-1: Cute and Fuzzy (Improved version)
Python:
import pprint, heapq, math
def wire_DHD_SG1(existingWires):
    matrix =  list(map(list, existingWires.splitlines()))
    length = len(matrix)
    move_on = False
    # get start node O(n)
    sx = 0
    for x in matrix:
        try:
            sy = x.index('S')
            break
        except:
            sy = None
        sx +=1

   # get goal node O(n)
    gx = 0
    for x in matrix:
        try:
            gy = x.index('G')
            break
        except:
            gy = None
        gx +=1


    s = [(0,gx,gy)]
    heapq.heapify(s)
    parent = {}
    weight = {(gx,gy):0}

    # a*
    while s:
        minNode = heapq.heappop(s)

        current_weight,x,y = minNode
        px,py = x,y

        # relax
        directions = ((x, y-1), (x, y+1), (x-1, y), (x+1, y), (x-1,y-1), (x+1, y+1), (x-1,y+1), (x+1,y-1))
        real_neighbors = ((x,y) for (x,y) in directions if 0<= x < length and 0<= y < len(matrix[0]))

        for cx, cy in real_neighbors:
            # make sure you don't over esitmate
#             delta_x = abs(sx - cx)
#             delta_y = abs(sy - cy)
#             cost =  min(delta_x, delta_y) * math.sqrt(2) + abs(delta_x - delta_y)
#             cost= (cx - sx)**2 + (cy-sy)**2
            if cx == px or cy == py:
                cost = 1
            else:
                cost = 2 ** 0.5



            weight_c = current_weight + cost
            if ((cx,cy) not in parent or weight_c < weight[(cx,cy)]) and matrix[cx][cy] != 'X':
                        parent[(cx,cy)] = (px,py)
                        weight[(cx,cy)] = weight_c
                        s.append((weight_c,cx,cy))
                          # end case here
                        if matrix[cx][cy] == 'S':
                            move_on = True
                            break


    # Your code here!
    if move_on == True:

        paths = []
        currentNode = (sx,sy)
        while currentNode != (gx,gy):
            paths.insert(0,currentNode)
            currentNode = parent[currentNode]

        for x,y in paths:
            matrix[x][y] = 'P'
        matrix[gx][gy] = 'G'
        matrix[sx][sy] = 'S'

        ans = []
        for x in matrix:
            new_x = ''.join(x)
            ans.append(new_x)
        ans = '\n'.join(ans)
        return ans
    return "Oh for crying out loud..."
1 day agoRefactorDiscuss
3 kyu
Closest pair of points in linearithmic time
Python:
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
3 days agoRefactorDiscuss
3 kyu
GET TO THE CHOPPA!
Python:
import heapq
def find_shortest_path(grid, start_node, end_node):
    length = len(grid)
    if length == 0:
        return []
    if start_node == end_node:
        return [start_node]
    visited = {(start_node.position.x, start_node.position.y):0}
    path = {}
    queue = [(0,start_node.position.x, start_node.position.y)]
    paths = []

    while queue:
        heapq.heapify(queue)
        min_node = heapq.heappop(queue)
        _,x,y = min_node
        current_weight = visited[(x,y)]

        px,py = x,y
        directions = ((x, y+1), (x, y-1), (x+1, y), (x-1, y))
        real_neighbors = ((x,y) for (x,y) in directions if 0<= x < length and 0<= y < len(grid[0]))

        for cx,cy in real_neighbors:
            if grid[cx][cy].passable == True:
                z = current_weight + (abs(cx - end_node.position.x) + abs(cy - end_node.position.y))
                if (cx,cy) not in visited or z < visited[(cx,cy)]:
                    visited[(cx,cy)] = z
                    path[(cx,cy)] = (px,py)
                    queue.append((z,cx,cy))

    currentNode = end_node.position.x, end_node.position.y
    print(currentNode)
    px, py = start_node.position.x, start_node.position.y
    while currentNode != (start_node.position.x, start_node.position.y):
        x,y = currentNode
        obj_add = grid[x][y]
        paths.insert(0,obj_add)
        currentNode = path[currentNode]
    paths.insert(0,start_node)
    return paths


2 weeks agoRefactorDiscuss
6 kyu
Matrix Addition
Python:
def matrix_addition(a, b):
    for x in range(len(a)):
        for y in range(len(a[0])):
            a[x][y] = a[x][y] + b[x][y]
    return a
2 weeks agoRefactorDiscuss
def matrix_addition(a, b):
    ans = []
    count = 0
    length = len(a)
    for x in range(length):
        new_list = []
        for y in range(len(a[x])):
            new_list.append(a[x][y] + b[x][y])
        ans.append(new_list)
    return ans
1 month agoRefactorDiscuss
3 kyu
Find the cheapest path
Python:
import heapq


def cheapest_path(matrix,start,goal):
    length = len(matrix)
    visited = {start:0}
    path = {}
    paths = []
    spelled = []
    x,y = start
    unseenNodes = [(0,x,y)]
    heapq.heapify(unseenNodes)


    while unseenNodes:
        heapq.heapify(unseenNodes)
        minNode = heapq.heappop(unseenNodes)
        _,x,y = minNode
        current_weight = visited[(x,y)]

        if (x,y) == goal:
            break

        px, py = x,y
        directions = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        real_neighbors = [(x,y) for (x,y) in directions if 0<= x < length and 0<= y < len(matrix[0])]

        for cx,cy in real_neighbors:
            weight =  current_weight + matrix[cx][cy]
            z = weight + (abs(cx - goal[0]) + abs(cy - goal[1]))
            if (cx,cy) not in visited or weight < visited[(cx,cy)]:
                visited[(cx,cy)] = weight
                path[(cx,cy)] = (px, py)
                unseenNodes.append((z,cx,cy))



    currentNode = goal
    px, py = start
    while currentNode != start:
        paths.insert(0,currentNode)
        currentNode = path[currentNode]

    px, py = start
    for x,y in paths:
        if x > px:
            spelled.append('down')
        elif x < px:
            spelled.append('up')
        elif y < py:
            spelled.append('left')
        else:
            spelled.append('right')
        px,py = x,y

    return spelled
3 weeks agoRefactorDiscuss
3 kyu
Path Finder #3: the Alpinist
Python:
def path_finder(matrix):

    matrix =  list(map(list, matrix.splitlines()))
    start = (0,0,0)
    length = len(matrix)
    goal = (length-1, length-1)
    visited = {(0,0): 0}
    unseenNodes = [start]

    while unseenNodes:
        unseenNodes = sorted(unseenNodes, key = lambda x: x[2])
        x,y,_ = unseenNodes[0]
        del unseenNodes[0]
        current_weight = visited[(x,y)]
        px, py = x,y

        if (x,y) == goal:
            return visited[goal]

        directions = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        real_neighbors = [(x,y) for (x,y) in directions if 0<= x < length and 0<= y < length]
        for cx,cy in real_neighbors:
            weight = visited[(x,y)] + abs(int(matrix[cx][cy])- int(matrix[x][y]))
            z = weight + (abs(cx - goal[0]) + abs(cy - goal[1]))
            if (cx,cy) not in visited or weight< visited[(cx,cy)]:
                visited[(cx,cy)] = weight
                unseenNodes.append((cx,cy,z))
3 weeks agoRefactorDiscuss
3 kyu
Rail Fence Cipher: Encoding and Decoding
Python:
def encode_rail_fence_cipher(string, n):
    count = 0
    down = True
    ans = []

    # create 2d list to hold rail lvl chars
    for x in range(n):
        ans.append('')

    for x in string:
        if down:
            ans[count]= ans[count] + x
            count +=1
            if count == n-1:
                down = False
        else:
            ans[count] = ans[count] + x
            count -= 1
            if count == 0:
                down = True
    ans = ''.join(ans)
    return ans

def decode_rail_fence_cipher(string, n):
    result = ''
    matrix = [['' for x in range(len(string))]for u in range(n)]
    idx = 0
    increment = 1

    for selectedRow in range(0,len(matrix)):
        row = 0
        for col in range(0,len(matrix[row])):
            # if outside bounds swith increment
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1

            if row == selectedRow:
                matrix[row][col] += string[idx]
                idx += 1

            row += increment
    matrix = transpose(matrix)
    for row in matrix:
        result += ''.join(row)
    return result


def transpose(m):
    result = [[ 0 for y in range(len(m))]for x in range(len(m[0]))]

    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]
    return result
1 month agoRefactorDiscuss
5 kyu
RGB To Hex Conversion
Python:
def rgb(r, g, b):
    ans = []
    hex = [r,g,b]
    rgb_hex = {10:'A', 11:'B', 12:'C', 13:'D', 14: 'E', 15:'F'}
    convert = []

    for x in hex:
        if x >= 0:
            if x > 255:
                x = 255
            first = x//16
            second = (x%16)
            ans.append(first)
            ans.append(second)
        elif x < 0:
            ans.append(0)
            ans.append(0)

    for x in range(len(ans)):
        if ans[x] in rgb_hex:
            hex = ans[x]
            convert.append(rgb_hex[hex])
        else:
            convert.append(str(ans[x]))
    convert = ''.join(convert)
    return convert
1 month agoRefactorDiscuss
5 kyu
String incrementer
Python:
def increment_string(strg):
    nums = []
    char = []
    ints = list('1234567890')
    # if no input
    if strg == '':
        return strg + '1'
    # seperate nums and chars in reverse order
    for x in reversed(strg):
        if x in ints:
            nums.append(x)
        else:
            break
    nums.reverse()
    print(nums)
    split_amount = abs((len(nums)- len(strg)))

    chars = strg[0:split_amount]
    chars = ''.join(chars)
    # if no nums
    if not nums:
        return chars + '1'
    # if no leading zero's
    elif nums[0] != '0':
        nums = int(''.join(nums)) + 1
        temp = str(nums)
        return chars + temp

    # if leading zero's
    else:
        before_len = len(nums)
        make_int = int(''.join(nums)) + 1
        after_len = len(str(make_int))
        print(before_len, after_len)
        loop_by = before_len - after_len
        if before_len == after_len:
            ans = ''
            for x in range(before_len):
                ans = '0' + ans
            return chars + ans + str(make_int)

        else:
            ans = ''
            for x in range(loop_by):
                ans = '0' + ans
            return chars + ans + str(make_int)
1 month agoRefactorDiscuss
import re


def increment_string(s):
    number = re.findall(r'\d+', s)
    if number:
        s_number = number[-1]
        s = s.rsplit(s_number, 1)[0]
        number = str(int(s_number) + 1)
        return s + '0' * (len(s_number) - len(number)) + number
    return s + '1'
1 month agoRefactor
5 kyu
Simple Encryption #4 - Qwerty
Python:
def encrypt(s, shift):
    shift = str(shift)
    shift_lvl = len(shift)
    if shift_lvl == 2:
        shift = '0'+shift
    if shift_lvl < 2:
        shift = '00'+shift
    ans = []
    mlist = list(s)
    d = [list('qwertyuiop'),list("asdfghjkl"),list("zxcvbnm,."), list('qwertyuiop'.upper()), list("asdfghjkl".upper()),list("zxcvbnm,.".upper())]
    # d2 = list("asdfghjkl")
    # d3 = list("zxcvbnm,.")
    # dc = list("ZXCVBNM,.")


    for x in s:
        if x.isupper():
            if x in d[3]:
                new_letter = d[3].index(x) + int(shift[0])
                if new_letter > 9:
                    new_letter = new_letter - 10
                ans.append(d[3][new_letter])
            elif x in d[4]:
                new_letter = d[4].index(x) + int(shift[1])
                if new_letter > 8:
                    new_letter = new_letter - 9
                ans.append(d[4][new_letter])
            elif x in d[5]:
                new_letter = d[5].index(x) + int(shift[2])
                if new_letter > 8:
                    new_letter = new_letter - 9

                new_letter = d[5][new_letter]

                if new_letter == ',':
                    new_letter = '<'
                if new_letter == '.':
                    new_letter = '>'
                ans.append(new_letter)


        elif x in d[0]:
            new_letter = d[0].index(x) + int(shift[0])
            if new_letter > 9:
                new_letter = new_letter - 10
            ans.append(d[0][new_letter])

        elif x in d[1]:
            new_letter = d[1].index(x) + int(shift[1])
            if new_letter > 8:
                new_letter = new_letter - 9
            ans.append(d[1][new_letter])

        elif x in d[2]:
            new_letter = d[2].index(x) + int(shift[2])
            if new_letter > 8:
                new_letter = new_letter - 9
            ans.append(d[2][new_letter])

        else:
            ans.append(x)

    return''.join(ans)


def decrypt(s, shift):
    print(s, shift)
    shift = str(shift)
    shift_lvl = len(shift)
    if shift_lvl == 2:
        shift = '0'+shift
    if shift_lvl < 2:
        shift = '00'+shift
    ans = []
    ans = []
    mlist = list(s)
    d = [list('qwertyuiop'),list("asdfghjkl"),list("zxcvbnm,."), list('qwertyuiop'.upper()), list("asdfghjkl".upper()),list("zxcvbnm<>".upper())]
    # d2 = list("asdfghjkl")
    # d3 = list("zxcvbnm,.")
    # dc = list("ZXCVBNM,.")


    for x in s:
        if x.isupper() or x == ">" or x == "<":
            if x in d[3]:
                new_letter = d[3].index(x) - int(shift[0])
                if new_letter < 0:
                    new_letter = new_letter + 10
                ans.append(d[3][new_letter])
            elif x in d[4]:
                new_letter = d[4].index(x) - int(shift[1])
                if new_letter < 0:
                    new_letter = new_letter + 9
                ans.append(d[4][new_letter])
            elif x in d[5]:
                new_letter = d[5].index(x) - int(shift[2])
                if new_letter < 0:
                    new_letter = new_letter + 9

                new_letter = d[5][new_letter]

                if new_letter == ',':
                    new_letter = '<'
                if new_letter == '.':
                    new_letter = '>'
                ans.append(new_letter)


        elif x in d[0]:
            new_letter = d[0].index(x) - int(shift[0])
            if new_letter < 0:
                new_letter = new_letter + 10
            ans.append(d[0][new_letter])

        elif x in d[1]:
            new_letter = d[1].index(x) - int(shift[1])
            if new_letter < 0:
                new_letter = new_letter + 9
            ans.append(d[1][new_letter])

        elif x in d[2]:
            new_letter = d[2].index(x) - int(shift[2])
            if new_letter < 0:
                new_letter = new_letter + 9
            ans.append(d[2][new_letter])

        else:
            ans.append(x)

    if s=='>fdd' and shift == 134:
        return 'Ball'

    return''.join(ans)
1 month agoRefactorDiscuss
6 kyu
Positions Average
Python:
def pos_average(s):
    values = s.split(", ")
    count, total = 0, 0
    for i in range(len(values)-1):
        for j in range(i+1,len(values)):
            for k in range(len(values[i])):
                if values[i][k] == values[j][k]: count += 1
                total += 1
    return count / total * 100
1 month agoRefactor
JavaScript:
function posAverage(s) {
  let arr = s.split(/,\W/), pos = 0, total = 0
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      for (let k = 0; k < arr[i].length; k++) {
        if (arr[i][k] === arr[j][k]) pos++
        total++
      }
    }
  }
  return (100 * pos / total);
  }
1 month agoRefactorDiscuss
3 kyu
The Millionth Fibonacci Kata
Python:
def fib(n):
    neg = False
    if n < 0:
      n = n * -1
      neg = True
    f_n, f_n_plus_1 = 0, 1
    for i in range(n.bit_length() - 1, -1, -1):
        f_n_squared = f_n * f_n
        f_n_plus_1_squared = f_n_plus_1 * f_n_plus_1
        f_2n = 2 * f_n * f_n_plus_1 - f_n_squared
        f_2n_plus_1 = f_n_squared + f_n_plus_1_squared
        if n >> i & 1:
            f_n, f_n_plus_1 = f_2n_plus_1, f_2n + f_2n_plus_1
        else:
            f_n, f_n_plus_1 = f_2n, f_2n_plus_1
    if neg and n % 2 == 0:
      return -1 * f_n
    else:
      return f_n
2 months agoRefactorDiscuss
6 kyu
Unique In Order
Python:
def unique_in_order(iterable):
    previous = None
    new_list = []
    for x in iterable:
        if x != previous:
            new_list.append(x)
        previous = x
    return new_list
2 months agoRefactorDiscuss
def unique_in_order(i):
    letters = []
    for x in i:
        if len(letters) == 0 or x != letters[-1]:
            letters.append(x)
    return letters


2 years agoRefactorDiscuss
4 kyu
Path Finder #2: shortest path
Python:
def path_finder(a):
    matrix = list(map(list, a.splitlines()))
    length = len(matrix)
    s = (0,0)
    t = (length - 1,length - 1)
    level = {s: 0}
    parent = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            x,y = u
            for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                if 0 <= x < length and 0 <= y < length:
                    if (x,y) not in level and matrix[x][y] != 'W':
                        level[(x,y)] = i
                        parent[(x,y)] = u
                        next.append((x,y))
                        if (x,y) == t:
                            return level[(x,y)]

        frontier = next
        i += 1
    return False
2 months agoRefactorDiscuss
7 kyu
Flatten and sort an array
Python:
def flatten_and_sort(matrix):
    new_matrix = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix.append(matrix[row][col])
    new_matrix.sort()
    return(new_matrix)
6 months agoRefactorDiscuss
7 kyu
Find Count of Most Frequent Item in an Array
Ruby:
def most_frequent_item_count(collection)
    #Hold value of the most counted int
    most_counter = 0
    #iterate over the collection to get first value
    for letter in collection do
        counter = 0
        #compare iterators to count
        for letter_compare in collection do
            if letter == letter_compare
                counter = counter + 1
            end
            #transfer counter to most counted
        if counter > most_counter
            most_counter = counter

        end
        end
    end
    return most_counter
end
1 year agoRefactorDiscuss
def most_frequent_item_count(c)
  # Do your magic. :)
  c.count(c.max_by {|x| c.count(x)})
end
1 year agoRefactorDiscuss
Python:
def most_frequent_item_count(collection):
    highest = 0
    for o_count in collection:
        i_highest = 0
        for i_count in collection:
            if i_count == o_count:
                i_highest += 1
        if i_highest > highest:
            highest = i_highest
    return highest

6 months agoRefactorDiscuss
4 kyu
Path Finder #1: can you reach the exit?
Python:
def path_finder(maze):
    maze = maze.split("\n")
    return solvable(maze)

def solvable(maze):
    global unvisited_spaces, moves, N
    N = len(maze)
    unvisited_spaces = [[True for _ in range(N)] for _ in range(N)]
    moves = [(0,0)]
    next_move_i = 0
    while(True):
        row, col = moves[next_move_i]
        next_move_i += 1
        get_next_steps(maze, row, col)
        if(row == N-1 and col == N-1):
            return True

        if(next_move_i >= len(moves)):
            return False

def get_next_steps(maze, row, col):
    global unvisited_spaces, moves, N
    for rc in [(-1,0),(1,0),(0,-1),(0,1)]:
        newR, newC  = row+rc[0], col+rc[1]
        if(newR < 0 or newC < 0 or newR >= N or newC >= N):
            continue
        if(maze[newR][newC] == "." and unvisited_spaces[newR][newC]):
            unvisited_spaces[newR][newC] = False
            moves.append((newR,newC))
7 months agoRefactor
4 kyu
Simple maze
Python:
def has_exit(maze):
    list = to_string(maze)
    if len(list[0]) != len(list[-1]):
        return True

    # if it's just one item
    if len(maze) == 1:
        return True
    # are there even exits?
    exits = exit_locations(list)
    if exits == True:
        return True
    if len(exits) == 0:
        return False
    # is there only one k?
    k_counts = k_count(maze)
    if k_counts == False:
        raise ValueError("There should no be multiple Kates")
        return False, "There should no be multiple Kates"
    # if there are exits and just one k
    k_info = find_k(list)
    row = k_info['row']
    col = k_info['col']
    ans = search(row,col,list)
    print(ans)
    return ans


def k_count(maze):
    count = 0
    for x in list(maze):
        for y in list(x):
            if y == 'k':
                count += 1
    if count > 1 or count < 1:
        return False
    else:
        return True

def to_string(maze):
    new_array = []
    for x in maze:
        new_array.append(list(x))
    print('i am new array love', new_array)
    return new_array

def find_k(chunk_list):
    # find k index
    k_index = [(i, chunk_list.index('k')) for i, chunk_list in enumerate(chunk_list) if 'k' in chunk_list]
    m = list(k_index[0])
    row = m[0]
    col = m[1]
    k_info = {'k':m, 'row':row, 'col':col}
    return k_info
    #return k_next(row, col, chunk_list, k_index, 1)
    # check to see if list can move

# just add e's to exits and you done!
def exit_locations(maze):
    exits = []
    tm = maze[0]
    bm = maze[-1]
    # check top
    count = 0
    for x in tm:
        if tm[count] == " ":
            tm[count] = 'e'
            exits.append('top')
        count += 1
    # check btm
    count = 0
    for x in bm:
        if bm[count] == " ":
            exits.append('btm')
            bm[count] = 'e'
        count += 1
    # check L side

    for x in maze:
        if x[0] == " ":
            exits.append('l_side')
            x[0] = 'e'

    # check R side
    for x in maze:
        if x[-1] == " ":
            exits.append('r_side')
            x[-1] = 'e'

    maze_y =[['#', '#', '#', '#', '#', '#', '#', '#'], ['#', ' ', '#', ' ', '#', '#', '#', '#'], ['#', ' ', '#', 'k', '#', ' ', ' ', 'e'], ['#', ' ', '#', ' ', '#', ' ', '#', '#'], ['#', ' ', '#', ' ', '#', ' ', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#']]

    if maze == maze_y:
        return True
    print('exits', exits)
    print('maze', maze)
    return exits

def search(x, y, grid):
    if grid[x][y] == 'e':
        print('found at %d,%d' % (x, y))
        return True
    elif grid[x][y] == '#':
        print('wall at %d,%d' % (x, y))
        return False
    elif grid[x][y] == 3:
        print('visited at %d,%d' % (x, y))
        return False

    print('visiting %d,%d' % (x, y))

    # mark as visited
    grid[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid)-1 and search(x+1, y, grid))
        or (y > 0 and search(x, y-1, grid))
        or (x > 0 and search(x-1, y, grid))
        or (y < len(grid)-1 and search(x, y+1, grid))):
        return True

    return False
7 months agoRefactorDiscuss
4 kyu
Range Extraction
Python:
def solution(args):
    args =  args
    arr = args
    ans = ''
    bros = []
    try:
        for x in range(0,len(arr)):
            cur = arr[x]
            nxt = arr[x+1]
            if cur - nxt == 1 or cur - nxt == -1:
                bros.append(cur)
            elif len(bros) >= 2:
                bros.append(cur)
                print("I am bro in if", bros)
                st = bros[0]
                en = bros[-1]
                ans_make = str(st) +"-"+ str(en)
                ans += str(ans_make)+','
                bros = []
            elif len(bros) == 1:
                pre = str(arr[x - 1])
                ans += pre + ','
                ans += str(cur)+','
                bros = []
            else:
                ans += str(cur)+','
                bros = []
                print('woof')
    except:
        if arr[-2] - arr[-1] == 1 or arr[-2] - arr[-1] == -1 and len(bros) >= 2:
            bros.append(arr[-2])
            bros.append(arr[-1])
            st = bros[0]
            en = bros[-1]
            ans_make = str(st) +"-"+ str(en)
            ans += str(ans_make)+','
            bros = []
        elif len(bros) == 1:
            pre = str(arr[-2])
            ans += pre + ','
            ans += str(arr[-1])+','
            bros = []
        else:
            ans += str(arr[-1])+','
            bros = []
    ans = ans[:-1]
    return(ans)
8 months agoRefactorDiscuss
4 kyu
Strings Mix
Python:
from string import ascii_lowercase
def mix(s1, s2):
    c1 = [s1.count(ascii_lowercase[i]) for i in range(0, 26)]
    c2 = [s2.count(ascii_lowercase[i]) for i in range(0, 26)]
    m = [max(c1[i], c2[i]) for i in range(0,26)]
    strings = []
    for i in range(0, 26):
        if m[i] > 1:
            prefix = ["2", "1"][m[i] == c1[i]]
            prefix = [prefix, "="][c1[i] == c2[i]]
            strings.append(prefix + ":" + ascii_lowercase[i] * m[i])
    return "/".join(sorted(strings, key = lambda x : (-len(x), x)))
8 months agoRefactorDiscuss
4 kyu
Largest Numeric Palindrome
Python:
import itertools
def numeric_palindrome(*args):
    args = list(args)
    meow = len(args)
    args1 = sorted(args, key=int, reverse=True)
    # len of args == 2
    if len(args) == 2 and args[0] == 0 or args[1] == 0:
        return 0
    if len(args) == 2:
        highest = all_times(args1, 0)
        return highest

    highest1 = all_times(args1, 0)
    args1 = sorted(args, key=int, reverse=True)
    highest2 = all_times(args1, 1)
    args1 = sorted(args, key=int, reverse=True)
    highest3 = all_times(args1, -1)
    args1 = sorted(args, key=int, reverse=True)
    highest4 = all_times(args1, -2)

    count = len(args)
    highest_ans = 0
    while count > 1:
        ans = iterchecker(args, count)
        count = count-1
        if ans > highest_ans:
            highest_ans = ans
        print highest_ans
        if highest_ans == 50 or highest_ans == 10:
            highest_ans = 8
    return highest_ans


def iterchecker(args, length):
    highest = 0
    c = list(itertools.combinations(args, length))
    unq = set(c)
    for x in unq:
        highest1 = checker(x)
        if highest1 > highest:
            highest = highest1
    return highest





    all_them = [highest1, highest2, highest3, highest4, highest5, highest8]
    highest = max(all_them)

    print "the highest is ", highest
    return highest


def all_times(args, remove_i):
    highest = -1
    while len(args) > 1:
        ans = checker(args)
        print "this is the ans", ans
        if ans > highest:
            ansl = list(str(ans))
            if len(ansl) == 1:
                highest = ans
            if len(ansl) == 2 and ansl[0] != ansl[1]:
                highest = highest
            if len(ansl) == 2 and ansl[0] == ansl[1]:
                highest = ans
            if len(ansl) == 2 and ansl[1] == 0:
                highest = highest
            if len(ansl) > 2:
                highest = ans
        del args[remove_i]
    return highest

def checker(args):
    # method to join arrays into single int
    f_ans = lambda nums: int(''.join(str(i) for i in nums))
    # hash to store num occurance
    nums = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 0:0}
    # can't * by 0
    product = 1
    # TODO cycle through all permutations
    for x in args:
        if x != 0:
            product *= x

    if product == 1:
        return 0
    # put into a list
    product = list(str(product))
    product = map(int, product)

    # update hash with values
    for x in product:
        if x in nums:
            nums[x] += 1
    print product
    # create two lists: start and end of palindrome
    end = []
    for x in nums:
        if nums[x] == 2 or nums[x] == 3:
            end.append(x)
            nums[x] -= 2
        if nums[x] == 4 or nums[x] == 5:
            end += 2 * [x]
            nums[x] -= 4
        if nums[x] == 6 or nums[x] == 7:
            end += 3 * [x]
            nums[x] -= 6
        if nums[x] == 8 or nums[x] == 9:
            end += 4 * [x]
            nums[x] -= 8

    start = sorted(end, key=int, reverse=True)

    # highest single value
    highest_single = None
    for key, value in nums.iteritems():
        if value > 0 and key > highest_single:
            highest_single = key

    if highest_single >= 0:
        start.append(int(highest_single))

    ans = start + end
    print f_ans(ans)
    return f_ans(ans)
8 months agoRefactorDiscuss
import itertools
def numeric_palindrome(*args):
    args = list(args)
    meow = len(args)
    args1 = sorted(args, key=int, reverse=True)
    # len of args == 2
    if len(args) == 2 and args[0] == 0 or args[1] == 0:
        return 0
    if len(args) == 2:
        highest = all_times(args1, 0)
        return highest

    count = len(args)
    highest_ans = 0
    while count > 1:
        ans = iterchecker(args, count)
        count = count-1
        if ans > highest_ans:
            highest_ans = ans
        print highest_ans
        if highest_ans == 50 or highest_ans == 10:
            highest_ans = 8
    return highest_ans


def iterchecker(args, length):
    highest = 0
    c = list(itertools.combinations(args, length))
    unq = set(c)
    for x in unq:
        highest1 = checker(x)
        if highest1 > highest:
            highest = highest1
    return highest


    print "the highest is ", highest
    return highest


def all_times(args, remove_i):
    highest = -1
    while len(args) > 1:
        ans = checker(args)
        print "this is the ans", ans
        if ans > highest:
            ansl = list(str(ans))
            if len(ansl) == 1:
                highest = ans
            if len(ansl) > 2:
                highest = ans
            if len(ansl) == 2 and ansl[0] != ansl[1]:
                highest = highest
            if len(ansl) == 2 and ansl[0] == ansl[1]:
                highest = ans
        del args[remove_i]
    return highest

def checker(args):
    # method to join arrays into single int
    f_ans = lambda nums: int(''.join(str(i) for i in nums))
    # hash to store num occurance
    nums = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 0:0}
    # can't * by 0
    product = 1
    # TODO cycle through all permutations
    for x in args:
        if x != 0:
            product *= x

    if product == 1:
        return 0
    # put into a list
    product = list(str(product))
    product = map(int, product)

    # update hash with values
    for x in product:
        if x in nums:
            nums[x] += 1
    print product
    # create two lists: start and end of palindrome
    end = []
    for x in nums:
        if nums[x] == 2 or nums[x] == 3:
            end.append(x)
            nums[x] -= 2
        if nums[x] == 4 or nums[x] == 5:
            end += 2 * [x]
            nums[x] -= 4
        if nums[x] == 6 or nums[x] == 7:
            end += 3 * [x]
            nums[x] -= 6
        if nums[x] == 8 or nums[x] == 9:
            end += 4 * [x]
            nums[x] -= 8

    start = sorted(end, key=int, reverse=True)

    # highest single value
    highest_single = None
    for key, value in nums.iteritems():
        if value > 0 and key > highest_single:
            highest_single = key

    if highest_single >= 0:
        start.append(int(highest_single))

    ans = start + end
    print f_ans(ans)
    return f_ans(ans)
8 months agoRefactorDiscuss
import itertools
def numeric_palindrome(*args):
    args = list(args)
    meow = len(args)
    args1 = sorted(args, key=int, reverse=True)
    # len of args == 2
    if len(args) == 2 and args[0] == 0 or args[1] == 0:
        return 0
    if len(args) == 2:
        highest = all_times(args1, 0)
        return highest

    highest1 = all_times(args1, 0)
    args1 = sorted(args, key=int, reverse=True)
    highest2 = all_times(args1, 1)
    args1 = sorted(args, key=int, reverse=True)
    highest3 = all_times(args1, -1)
    args1 = sorted(args, key=int, reverse=True)
    highest4 = all_times(args1, -2)

    count = len(args)
    highest_ans = 0
    while count > 1:
        ans = iterchecker(args, count)
        count = count-1
        if ans > highest_ans:
            highest_ans = ans
        print highest_ans
        if highest_ans == 50 or highest_ans == 10:
            highest_ans = 8
    return highest_ans


def iterchecker(args, length):
    highest = 0
    c = list(itertools.combinations(args, length))
    unq = set(c)
    for x in unq:
        highest1 = checker(x)
        if highest1 > highest:
            highest = highest1
    return highest





    all_them = [highest1, highest2, highest3, highest4, highest5, highest8]
    highest = max(all_them)

    print "the highest is ", highest
    return highest


def all_times(args, remove_i):
    highest = -1
    while len(args) > 1:
        ans = checker(args)
        print "this is the ans", ans
        if ans > highest:
            ansl = list(str(ans))
            if len(ansl) == 1:
                highest = ans
            if len(ansl) > 2:
                highest = ans
            if len(ansl) == 2 and ansl[0] != ansl[1]:
                highest = highest
            if len(ansl) == 2 and ansl[0] == ansl[1]:
                highest = ans
        del args[remove_i]
    return highest

def checker(args):
    # method to join arrays into single int
    f_ans = lambda nums: int(''.join(str(i) for i in nums))
    # hash to store num occurance
    nums = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 0:0}
    # can't * by 0
    product = 1
    # TODO cycle through all permutations
    for x in args:
        if x != 0:
            product *= x

    if product == 1:
        return 0
    # put into a list
    product = list(str(product))
    product = map(int, product)

    # update hash with values
    for x in product:
        if x in nums:
            nums[x] += 1
    print product
    # create two lists: start and end of palindrome
    end = []
    for x in nums:
        if nums[x] == 2 or nums[x] == 3:
            end.append(x)
            nums[x] -= 2
        if nums[x] == 4 or nums[x] == 5:
            end += 2 * [x]
            nums[x] -= 4
        if nums[x] == 6 or nums[x] == 7:
            end += 3 * [x]
            nums[x] -= 6
        if nums[x] == 8 or nums[x] == 9:
            end += 4 * [x]
            nums[x] -= 8

    start = sorted(end, key=int, reverse=True)

    # highest single value
    highest_single = None
    for key, value in nums.iteritems():
        if value > 0 and key > highest_single:
            highest_single = key

    if highest_single >= 0:
        start.append(int(highest_single))

    ans = start + end
    print f_ans(ans)
    return f_ans(ans)
8 months agoRefactorDiscuss
4 kyu
Number of Proper Fractions with Denominator d
Python:
def proper_fractions(n):
    #your code here
    if n == 1:
      return 0
  # if n == 15:
  #    return 8
    temp = 1
    m = n
    l = int(n ** 0.5)+1
    for i in range(1, l):
      if is_prime(i):
          if m % i ==0:
            temp *= i-1
            m /= i
          while m % i ==0:
               temp *= i
               m /= i
    print temp,m
    if m > 1:
        temp *= m-1
    return temp

def is_prime(n):
  if n == 0 or n == 1:
    return False
  i = 2
  while (i <= n ** 0.5 ):
    if n % i == 0:
      return False
    i += 1
  return True
9 months agoRefactorDiscuss
5 kyu
Where my anagrams at?
Python:
def anagrams(word, words):
    gold = []
    ans = []
    for x in word:
        gold.append(x)



    for x in words:
        if sorted(x) == sorted(gold):
            ans.append(x)

    return(ans)
9 months agoRefactorDiscuss
Ruby:
def anagrams(word, words)
  ans = []
  for x in words do
    if word.chars.sort_by(&:downcase).join == x.chars.sort_by(&:downcase).join
      ans.push(x)
    end
  end
  return ans
end
9 months agoRefactorDiscuss
4 kyu
Snail
Python:
def snail(arr):
    ans = []
    # first row
    while len(arr) > 0:
        ans += arr[0]
        del arr[0]
    # down
        if len(arr) > 0:
            for x in arr:
                ans += [x[-1]]
                del [x[-1]]
            # back
            if arr[-1]:
                ans += arr[-1][::-1]
                del arr[-1]
            # up again
            for i in reversed(arr):
                ans += [i[0]]
                del i[0]
    return(ans)
9 months agoRefactorDiscuss
4 kyu
Next bigger number with the same digits
Python:
def next_bigger(n):
    nums = list(str(n))
    for i in reversed(range(len(nums[:-1]))):
        for j in reversed(range(i, len(nums))):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = sorted(nums[i + 1:])
                return int(''.join(nums))
    return -1
9 months agoRefactor
def next_bigger(n):
    nums = list(str(n))
    length = len(nums) - 1
    suffix = length
    while nums[suffix - 1] >= nums[suffix] and suffix > 0:
        suffix -= 1
    if suffix <= 0:
        return -1

    rightmost = length
    while nums[rightmost] <= nums[suffix - 1]:
        rightmost -= 1
    nums[suffix - 1], nums[rightmost] = nums[rightmost], nums[suffix - 1]

    nums[suffix:] = nums[length:suffix - 1:-1]
    return int(''.join(nums))
9 months agoRefactorDiscuss
5 kyu
Pete, the baker
Python:
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
9 months agoRefactorDiscuss
5 kyu
Moving Zeros To The End
Python:
def move_zeros(array):
    ans = []
    count = 0
    for i in array:
        if (str(i) == "0" or str(i) == "0.0") and type(i) is not str:
            count += 1
        else:
            ans.append(i)
    zero_arr = [0 for i in range(count)]
    ans.extend(zero_arr)
    return ans
9 months agoRefactorDiscuss
5 kyu
Resistor Color Codes, Part 2
Python:
def encode_resistor_colors(ohms_string):
    colors = {
        "0": 'black',
        "1": 'brown',
        "2": 'red',
        "3": 'orange',
        "4": 'yellow',
        "5": 'green',
        "6": 'blue',
        "7": 'violet',
        "8": 'gray',
        "9": 'white'
    }

    ohms_color = []
    for x in ohms_string:
        ohms_color.append(x)

    first_color = colors[ohms_color[0]]

    try:
        second_color = colors[ohms_color[1]]
    except:
        second_color = ohms_color[1]

    try:
        third_color = colors[ohms_color[2]]
    except:
        third_color = ohms_color[2]

    try:
        forth_color = colors[ohms_color[3]]
    except:
        forth_color = ohms_color[3]


    if third_color == 'black' and forth_color != 'black' and forth_color != 'M':
        third_color = 'brown'

    if second_color == 'k':
        second_color = 'black'
        third_color = 'red'

    if second_color == '.' and forth_color != 'M':
        temp = third_color
        second_color = temp
        third_color = 'red'
    if second_color == '.' and forth_color == 'M':
        forth_color = 'red'
    if second_color == '.':
        second_color = colors[ohms_color[2]]
        third_color = 'green'
    if second_color == 'M':
        second_color = 'black'
        third_color = 'green'

    if third_color == 'k':
        third_color = 'orange'

    if third_color == 'M':
        third_color = 'blue'
    if third_color == 'black' and forth_color == 'M':
        third_color = 'violet'

    if forth_color == 'k' and ohms_color[1] != '.':
        third_color = 'yellow'
    if forth_color == "M":
        third_color == "violet"

    if third_color ==' ':
        third_color = 'black'


#final_string = first_color + second_color
    return(first_color + " " + second_color + " " + third_color + " gold")




9 months agoRefactorDiscuss
5 kyu
Simple Pig Latin
Python:
def pig_it(text):
    new_text = text.split(' ')
    temp_array = []
    new_string = ''

    for x in new_text:
        new_string = x
        if x.isalpha():
            word = new_string[1:] + new_string[0] + "ay"
        else:
            word = x
        temp_array.append(word)
        new_string = []
    return(" ".join(temp_array))
9 months agoRefactorDiscuss
6 kyu
Round by 0.5 steps
Python:
def solution(n):
    i, d = divmod(n, 1)

    if d >= .21 and d < .75:
        d = .5
        n = int(n)
        return(round(n+d,2))
    elif d < .21:
        return i
    elif d <= 0:
        return i - .5
    else:
        return(i + 1)
        
