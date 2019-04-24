def rake_garden(garden):
    dic = {"slug":"gravel", "spider":"gravel", "snail":"gravel", "ant":"gravel", "moss":"gravel"}
    for x, z in dic.iteritems():
        garden = garden.replace(x, z)
    return gardens
