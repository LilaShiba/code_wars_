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
