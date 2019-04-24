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
