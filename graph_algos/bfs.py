def path_finder(maze):
    maze = list(map(list, maze.splitlines()))
    start = (0,0)
    end = (len(maze)-1, len(maze)-1)
    frontier = [start]
    length = len(maze)
    explored = []

    while frontier:
        # u = (0,0)
        # loop through all nodes
        for u in frontier:
            x,y = u
            # search for neighbors
            for x,y in (x,y-1), (x, y+1), (x-1, y), (x+1, y):
                # see if maze
                0<= x < length and 0<= y < length:
                    # make sure (x,y) hasn't been explored and is not a wall
                    if (x,y) not in explored and maze[x][y] != 'W':
                        # update explored and frontier
                        explored.append((x,y))
                        frontier.append((x,y))
                        # end condition
                        # if (x,y) == end success!
                        if (x,y) == end:
                            return True
    return False
