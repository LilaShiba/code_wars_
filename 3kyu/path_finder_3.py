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
