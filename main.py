from os import system, name
import time
from pynput.keyboard import Key, Listener


level=[
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'], #0,0 0,1, 0,2, 0,3, 0,4 0,5 0,6 0,7 0,8 0,9 
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
['[X]','[X]','[X]','[X]','[X]','[X]','[X]','[X]','[X]', '[X]'],
['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'] # 15,0
]

rungame=1
rowscleared=0

# our variables
yminlimit=0 # top most row
ymaxlimit=(len(level)-1) # bottom most row
xminlimit=0 # left most column
xmaxlimit=(len(level[0])-1) # right most column

cursorx=0 #(xmaxlimit//2) # to set the cursor in the center.
cursory=0
# set cursor in middle

# for falling blocks (tetris physics)
G=1
gravity=G*.25 # the "automatic" drop. 1G = 1 cell per frame, 0.1G = 1 cells per 10 frames, etc...
gravity=float(gravity)
velocity=.25 # falling block's velocity,
velocity=float(velocity)

playerscore=0

# set our cursor character's location on the tilemap grid.
def set_cursor(column, row):
	level[row][column]="[X]"
# I changed the columns and rows around to make the arguments more intuitive with x, y coordinates.
def remove_cursor(column, row):
    level[row][column]="[ ]"

set_cursor(cursorx, cursory) # note: row has to be a y-value. column has to be a x-value. 

def set_block(type="Oblock"):
    if type=="Oblock":
        set_cursor(cursorx, cursory)
        set_cursor(cursorx+1, cursory)
        set_cursor(cursorx, cursory+1)
        set_cursor(cursorx+1, cursory+1)
    if type=="Iblock":
        set_cursor(cursorx, cursory)
        set_cursor(cursorx+1, cursory)
        set_cursor(cursorx+2, cursory)
        set_cursor(cursorx+3, cursory)

def remove_block(type="Oblock"):
    if type=="Oblock":
        remove_cursor(cursorx, cursory)
        remove_cursor(cursorx+1, cursory)
        remove_cursor(cursorx, cursory+1)
        remove_cursor(cursorx+1, cursory+1)
    if type=="Iblock":
        remove_cursor(cursorx, cursory)
        remove_cursor(cursorx+1, cursory)
        remove_cursor(cursorx+2, cursory)
        remove_cursor(cursorx+3, cursory)
# ================================
'''
# set cursor blocks on to screen
def set_block(piece, column, row):
    if piece==Ipiece:
        pass


    elif piece==Opiece:
        pass


'''
# ================================

# clearing lines (prototype)
def clear_line(row):
    global rungame
    global rowscleared
    row.clear()
    row.extend(['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'])
    rowscleared+=1
# ================================

def check_to_clear_row():
    global level
    global playerscore
    i=0
    for row in level:
        result = all(element == '[X]' for element in row)
        if (result):
            clear_line(level[i])
            playerscore+=400
            i+=1
        else:
            i+=1



# "tetris" game logic.
def drop_blocks(droptype='normal'):
    global cursorx; global cursory
    global gravity; global velocity # values that may need to be altered depending on drop.
    # making sure to reset, in order to ensure multiple blocks can be dropped.   
    if droptype=='normal':
        if cursory < ymaxlimit: # check if block hasn't fallen to the floor. (Will have to update collision detection later when I implement other blocks.)
            time.sleep(gravity)
            remove_cursor(cursorx, cursory) # removing previous position
            cursory += 1 #downward (y is inversed)
            set_cursor(cursorx, cursory)
    elif droptype=="hard":
        if cursory < ymaxlimit:
            remove_cursor(cursorx, cursory)
            cursory = ymaxlimit # drop block to bottom of floor. later add better collision detection to account for blocks.
            set_cursor(cursorx, cursory)
    elif droptype=="soft": # lets try to modify the coordinates around the cursor to make a block
        if cursory < ymaxlimit-1: # stops crashing when block hits the ground. However, after two blocks stack the game gets stuck in some kind of loop.
            if level[cursory+2][cursorx]!="[X]": # note row is y coord.
                #if cursory+1 < ymaxlimit:
                # ^ block detection collision followed by floor detection collision
                time.sleep(gravity*velocity) # speed the fall of the drop.
                # remove_cursor(cursorx, cursory)
                # remove_cursor(cursorx+1, cursory)
                # remove_cursor(cursorx, cursory+1)
                # remove_cursor(cursorx+1, cursory+1)
                remove_block()
                cursory += 1
                # set_cursor(cursorx, cursory)
                # set_cursor(cursorx+1, cursory)
                # set_cursor(cursorx, cursory+1)
                # set_cursor(cursorx+1, cursory+1)
                set_block()
    #        elif 0:
    #            pass #implement detection for the top of the screen being filled up.
            # also: need to make this code work with multiple collision surfaces,
            # as well as the floor.
                #else: # reset the cursor position for the next block when this one is done.
                #    cursorx=(xmaxlimit//2)
                #    cursory=0
        else: # reset the cursor position for the next block when this one is done.
            # if cursorx is less than xmaxlimit:
            cursorx+=2
            cursory=0
            # else, reset:
'''
        if cursory < ymaxlimit-1: # since we are using a square block, the cursor will be higher.
            # ^ floor detection collision
            time.sleep(gravity*velocity) # speed the fall of the drop.
            remove_cursor(cursorx, cursory)
            remove_cursor(cursorx+1, cursory)
            remove_cursor(cursorx, cursory+1)
            remove_cursor(cursorx+1, cursory+1)
            cursory += 1
            set_cursor(cursorx, cursory)
            set_cursor(cursorx+1, cursory)
            set_cursor(cursorx, cursory+1)
            set_cursor(cursorx+1, cursory+1)
        else: # reset the cursor position for the next block when this one is done.
            cursorx=(xmaxlimit//2)
            cursory=0
'''


            
            






# important functions for displaying the screen properly.

def refreshscreen():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for 'posix': mac, linux, unix
	else:
		_ = system('clear')



def display_screen():
    global cursorx; global cursory
    global rungame
 #   i = input("'hard' for hard (instant) drop. 'soft' for soft (fast) drop. Else: watch gravity do its work.")
    while rungame==1:
        if rowscleared>=4:
            rungame=0
        refreshscreen()
        tilemap=level
        outputstr=''
        for row in tilemap:
            for columnitem in row:
                outputstr += columnitem
            outputstr += "\n"
        # lets add in our cursor location and grid coords for debugging:
        outputstr += f"\nCURSORX:{cursorx}    CURSORY:{cursory}\n"
        outputstr += f"\nSCORE:{playerscore}\n{(4-rowscleared)} lines left.\n"
        
#        if level[cursory+2][cursorx]=="[X]": # note row is y coord.
#            outputstr+="COLLISION EVENT"
        check_to_clear_row()

        print(outputstr) # instead of printing each iteration, we iterate first in order to print
        # all of the "pixels" on our display.
        drop_blocks('soft')
        time.sleep(.25) # note: this is combined with the "G" variable for a total frame. i.e: 1G*.25=gravity, gravity*sleep(.25)=sleep(.5) aka one frame.
        
        # clear-line / floor collision prototyping
        #for column in level[ymaxlimit]: #ymaxlimit == floor squares
        #    if column != '[ ]':
        #        clear_line(level[ymaxlimit])


def main():
    display_screen()
    print("TETRIS")
    return 0

main()