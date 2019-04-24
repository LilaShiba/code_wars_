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
