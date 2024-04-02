from random import randint
import turtle


# global variables

g_colors = ['tan1', 'PeachPuff3', 'PaleVioletRed1',
            'MediumPurple3', 'SteelBlue2']
g_board = list()
g_tile_size = 80
g_tile_func_size = 4
g_tile_bdry = 5
g_scr_bdry = 25
g_scr_wd = 500
g_scr_ht = 580
g_pivot = (-1, -1)
g_tile_basis = turtle.Turtle()
g_s = turtle.Screen()
g_bar_co_lst = list()
g_board_co_lst = list()
# here we use globals() to generate many
# global variables which are similar
# these are g_c0,g_c1,...,g_c4
# which represent 5 colors in bar
# and g_t00,g_t01,...,g_t44
# which represent 25 tiles in board
g_var = globals()
for c in range(5):
    g_var['g_c'+str(c)] = ''
for r in range(5):
    for c in range(5):
        g_var['g_t'+str(r)+str(c)] = ''


# this function is used to set
# the parameters of screen
# it returns None
def setScreen():
    g_s.tracer(0)
    g_s.setup(g_scr_wd, g_scr_ht)
    g_s.setworldcoordinates(0, 0, g_scr_wd, g_scr_ht)

# this function is used to set standard
# parameters for basis tile, other different
# tiles which are 30 in total are all clones
# of this basis tile
# it returns None


def setTileBasis():
    g_tile_basis.penup()
    g_tile_basis.shape('square')
    g_tile_basis.speed(0)
    g_tile_basis.shapesize(g_tile_func_size,
                           g_tile_func_size,
                           0)


# this function is used to store all the
# coordinates of the tiles in board or
# bar in two lists seperately
def createCoLst():
    for n in range(5):
        x = (g_scr_bdry*(1)
             + g_tile_size*(0.5+n)
             + g_tile_bdry*(2+n)
             )
        y = (g_scr_bdry*(0.5)
             + g_tile_size*(0.5)
             + g_tile_bdry*(1)
             )
        g_bar_co_lst.append((x, y))

    for r in range(5):
        for c in range(5):
            x = (g_scr_bdry*(1)
                 + g_tile_size*(0.5+c)
                 + g_tile_bdry*2*(c)
                 )
            y = (g_scr_bdry*(0.5)
                 + g_tile_size*(1.7+r)
                 + g_tile_bdry*2*(1+r)
                 )
            g_board_co_lst.append((x, y))

# this function is used to create random
# colors for each tile in board


def createBoard():
    for _ in range(25):
        g_board.append(g_colors[randint(0, 4)])


# this function is used to set 5 tiles
# with colors in bar on the screen
def setBar():
    g_tile_basis.showturtle()
    for c in range(5):
        # we do not need to claim that these are
        # global variables because g_var = globals()
        # has already globalized them
        g_var['g_c'+str(c)] = g_tile_basis.clone()
        g_var['g_c'+str(c)].color('black', g_colors[c])
        g_var['g_c'+str(c)].setpos(g_bar_co_lst[c])
        g_var['g_c'+str(c)].shapesize(g_tile_func_size,
                                      g_tile_func_size,
                                      g_tile_bdry)
    g_tile_basis.hideturtle()

# this function is used to set 25 tiles
# with random colors in board on the screen


def setBoard():
    g_tile_basis.showturtle()
    for r in range(5):
        for c in range(5):
            idx = r*5 + c
            # we do not need to claim that these are
            # global variables because g_var = globals()
            # has already globalized them
            g_var['g_t'+str(r)+str(c)] = g_tile_basis.clone()
            g_var['g_t'+str(r)+str(c)].color('white', g_board[idx])
            g_var['g_t'+str(r)+str(c)].setpos(g_board_co_lst[idx])
    g_tile_basis.hideturtle()


# this function is used to test whethter
# the clicking area is the board area or not,
# it returns True or False
def isBoardArea(p_x, p_y):
    x_min = g_board_co_lst[0][0] - g_tile_size*0.5 - g_tile_bdry
    x_max = g_board_co_lst[24][0] + g_tile_size*0.5 + g_tile_bdry
    y_min = g_board_co_lst[0][1] - g_tile_size*0.5 - g_tile_bdry
    y_max = g_board_co_lst[24][1] + g_tile_size*0.5 + g_tile_bdry
    # check the coordinate area
    if (x_max > p_x > x_min
            and y_max > p_y > y_min
            ):
        return True
    else:
        return False

# this function is used to test whethter
# the clicking area is the main color area or not,
# it is given the coordinate of the clicking x, y
# it returns True or False


def isBarArea(p_x, p_y):
    x_min = g_bar_co_lst[0][0] - g_tile_size*0.5 - g_tile_bdry
    x_max = g_bar_co_lst[4][0] + g_tile_size*0.5 + g_tile_bdry
    y_min = g_bar_co_lst[0][1] - g_tile_size*0.5 - g_tile_bdry
    y_max = g_bar_co_lst[4][1] + g_tile_size*0.5 + g_tile_bdry
    # check the coordinate area
    if (x_max > p_x > x_min
            and y_max > p_y > y_min
            ):
        return True
    else:
        return False


# this function is used to find the most updated
# pivot after the func 'isBoardArea()' returns True
# it is given the coordinate of the clicking x, y
# it returns the most updated pivot
def boardAreaPivot(p_x, p_y):
    min_dist_sqr = 9999
    pivot = (0, 0)
    for r in range(5):
        for c in range(5):
            idx = r*5 + c
            x_dist = g_board_co_lst[idx][0] - p_x
            y_dist = g_board_co_lst[idx][1] - p_y
            cur_dist_sqr = x_dist**2 + y_dist**2
            # test whether the distance
            # is smaller than the current
            # minimum distance or not
            if cur_dist_sqr < min_dist_sqr:
                min_dist_sqr = cur_dist_sqr
                pivot = (r, c)
    return pivot

# this function is used to find which color you
# flips after the func 'isBarArea()' returns True
# it is given the coordinate of the clicking x, y
# it returns the num of the color


def barAreaNum(p_x, p_y):
    min_dist_sqr = 9999
    num = 0
    for n in range(5):
        x_dist = g_bar_co_lst[n][0] - p_x
        y_dist = g_bar_co_lst[n][1] - p_y
        cur_dist_sqr = x_dist**2 + y_dist**2
        # test whether the distance
        # is smaller than the current
        # minimum distance or not
        if cur_dist_sqr < min_dist_sqr:
            min_dist_sqr = cur_dist_sqr
            num = n
    return num


# this function is used to porcess the
# events after clicking the screen
# it is given the coordinate of clicking x, y
# it returns None
def coordFunc(p_x, p_y):
    global g_pivot
    row, col = g_pivot
    idx = row*5 + col
    # click the board area
    if isBoardArea(p_x, p_y):
        g_pivot = boardAreaPivot(p_x, p_y)
    # click the bar area
    elif isBarArea(p_x, p_y):
        num = barAreaNum(p_x, p_y)
        ini = g_board[idx]
        fin = g_colors[num]
        flipColor(row, col, ini, fin)
        g_pivot = (-1, -1)
    # update the screen
    refreshScreen()


# this recursive function is used to flip the color
# this function is given the row, column, initial color,
# and final color of the tile the player select.
# it returns None
def flipColor(p_r, p_c, p_ini, p_fin):
    if p_ini == p_fin:
        return
    if p_r < 0 or p_r >= 5:
        return
    if p_c < 0 or p_c >= 5:
        return
    idx = p_r*5 + p_c
    if g_board[idx] != p_ini:
        return
    g_board[idx] = p_fin
    flipColor(p_r-1, p_c, p_ini, p_fin)
    flipColor(p_r+1, p_c, p_ini, p_fin)
    flipColor(p_r, p_c-1, p_ini, p_fin)
    flipColor(p_r, p_c+1, p_ini, p_fin)


# this function is used to refresh the screen,
# i.e. to keep the screen to the most updated one
# it returns None
def refreshScreen():
    for r in range(5):
        for c in range(5):
            idx = r*5 + c
            # set the selected tile's parameter
            # or it is just a common one
            bdrysize = g_tile_bdry if g_pivot == (r, c) else 0
            bdrycolor = 'black' if g_pivot == (r, c) else 'white'
            g_var['g_t'+str(r)+str(c)].color(bdrycolor, g_board[idx])
            g_var['g_t'+str(r)+str(c)].shapesize(g_tile_func_size,
                                                 g_tile_func_size,
                                                 bdrysize)
    g_s.update()


def testing():
    print("testing!")

# this is the main processing of this game
def main():
    # do basic gaming preparation
    setScreen()
    setTileBasis()
    createCoLst()
    createBoard()
    setBar()
    setBoard()
    refreshScreen()
    # process clicking events
    g_s.onclick(coordFunc)
    g_s.mainloop()


if __name__ == '__main__':
    main()
