import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

allies = []
enemies = []
rums = []

class Ship(object):
    def __init__(self,id,posx,posy,rotation,speed,rum):
        self.id = id
        self.pos = [posx,posy]
        self.rotation = rotation
        self.speed = speed
        self.rum = rum

class Barrel(object):
    def __init__(self,id,posx,posy,amount):
        self.id = id
        self.pos = [posx,posy]
        self.amount = amount

class Cannonball(object):
    def __init__(self,id,posx,posy,owner,turns):
        self.id = id
        self.pos = [posx,posy]
        self.owner = owner
        self.detonate = turns


class Mine(object):
    def __init__(self,posx,posy):
        self.id = id
        self.pos = [posx,posy]


def get_distance(s,b):
    return math.sqrt(((s[0]-b[0])**2) + ((s[1]-b[1])**2))
    
def get_nearest_barrel(x,y):
    nxy = []
    nd = 100000
    for i in range(len(rums)):
        dcurr = get_distance([x,y],[rums[i][0],rums[i][1]])
        if dcurr < nd:
            nd = dcurr
            nxy = [ rums[i][0], rums[i][1] ]
    return nxy
    
def move_ship():
    
    
    
# game loop
while True:
    allies = []
    enemies = []
    rums = []
    mines = []
    cannonballs = []
    my_ship_count = int(raw_input())  # the number of remaining ships
    entity_count = int(raw_input())  # the number of entities (e.g. ships, mines or cannonballs)
    for i in xrange(entity_count):
        entity_id, entity_type, x, y, arg_1, arg_2, arg_3, arg_4 = raw_input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)
        if entity_type == "BARREL":
            e = Barrel(entity_id,x,y,arg_1)
            rums.append(e)
        elif entity_type == "CANNONBALL" and arg_4 == 0:
            e = Cannonball(entity_id,x,y,arg_1,arg_2)
            cannonballs.append(e)
        elif entity_type == "MINE" and arg_4 == 0:
            e = Mine(entity_id,x,y)
            mines.append(e)
        elif entity_type == "SHIP" and arg_4 == 1:
            e = Ship(entity_id,x,y,arg_1,arg_2,arg_3)
            allies.append(e)
        elif entity_type == "SHIP" and arg_4 == 0:
            e = Ship(entity_id,x,y,arg_1,arg_2,arg_3)
            enemies.append(e)

    print "mine: "+str(allies)
    print "enemies: "+str(enemies)
    print "barrels: "+str(rums)
    print "mine: "+str(mines)
    print "cannonballs: "+str(cannonballs)
    for i in xrange(my_ship_count):

        # Write an action using print
        # To debug: print >> sys.stderr, "Debug messages..."

        # Any valid action, such as "WAIT" or "MOVE x y"
        d = get_nearest_barrel(allies[i][0],allies[i][1])
        print "MOVE "+str(d[0])+" "+str(d[1])


    