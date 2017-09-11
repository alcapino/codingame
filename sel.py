import sys
import math
maxv = None
max_loss = 0

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
for i in raw_input().split():
    v = int(i)
    if(v > maxv or maxv == None):
        maxv = v
    
    tl = maxv - v
    if(v < maxv and tl > max_loss ):
        max_loss = maxv - v
    
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
if max_loss > 0:
    print "-"+str(max_loss)
else:
    print 0
