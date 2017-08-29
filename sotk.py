import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in raw_input().split()]
n = int(raw_input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in raw_input().split()]
U_limit,D_limit,L_limit,R_limit = 0,h,0,w

# game loop
while True:
    bomb_dir = raw_input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    for i in bomb_dir:
        if i == "U":
            D_limit = y0 - 1
        if i == "D":
            U_limit = y0 + 1
        if i == "L":
            R_limit = x0 - 1
        if i == "R":
            L_limit = x0 + 1
    x0 = (L_limit + R_limit) / 2
    y0 = (U_limit + D_limit) / 2
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # the location of the next window Batman should jump to.
    print str(x0)+" "+str(y0)
