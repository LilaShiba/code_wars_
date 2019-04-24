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
