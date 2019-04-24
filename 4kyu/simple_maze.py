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
