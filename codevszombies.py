import sys
import math

# Save humans, destroy zombies!

    
class Human(object):
    def __init__(self,id,posx,posy):
        self.id = id
        self.pos = [posx,posy]
        self.in_danger = False
    def __str__(self):
        ("ID: %d - X:%d, Y:%d" % (self.id,self.pos[0],self.pos[1])) 
    def in_danger(self):
        return self.in_danger
        
class Zombie(object):
    def __init__(self,id,posx,posy,z2p_d,z2h_d):
        self.id = id
        self.pos = [posx,posy]
        #self.nextpos = [nposx,nposy]
        self.player_distance = z2p_d
        self.human_distance = z2h_d
    def __str__(self):
        return "ID: "+str(self.id)+" - X:"+str(self.pos[0])+", Y:"+str(self.pos[1]) 
    def __repr__(self):
        return str(self)
        
def get_distance(s,b):
    return math.sqrt(((s[0]-b[0])**2) + ((s[1]-b[1])**2))

# def get_nearest_zombie(x,y):
#     nxy = []
#     nd = 100000
#     for i in range(len(zombies)):
#         print("zombies #%d: " % (i), file=sys.stderr, flush=True)
#         dcurr = get_distance([x,y],[zombies[i].npos[0],zombies[i].pos[1]])
#         print("dcurr" + str(dcurr), file=sys.stderr, flush=True)
#         if dcurr < nd:
#             nd = dcurr
#             nxy = [ zombies[i].npos[0], zombies[i].npos[1] ]
#     print("NXY" + str(nxy), file=sys.stderr, flush=True)
#     return nxy
    
def get_nearest_human(x,y):
    nxy = 0
    nd = 100000
    for i in range(len(humans)):
        dcurr = get_distance([x,y],[humans[i].pos[0],humans[i].pos[1]])
        if dcurr < nd:
            nd = dcurr
            # nxy = [ humans[i].pos[0],humans[i].pos[1] ]
            nxy = i
    return nxy

def get_nearest_zombie(x,y):
    nxy = 0
    nd = 100000
    for i in range(len(zombies)):
        # print("zombies #%d: " % (i), file=sys.stderr, flush=True)
        dcurr = get_distance([x,y],[zombies[i].pos[0],zombies[i].pos[1]])
        if dcurr < nd:
            nd = dcurr
            # nxy = [ zombies[i].pos[0],zombies[i].pos[1] ]
            nxy = i
    return nxy

def get_distance_to_nearest(x, y, side):
    nid = 0
    nd = 100000
    for i in range(len(side)):
        dcurr = get_distance([x,y],[side[i].pos[0], side[i].pos[1]])
        if dcurr < nd:
            nd = dcurr
            nid = i
    return nd, nid


# game loop
while True:
    humans = []
    in_danger = []
    zombies = []
    hID = 0
    nz2h = 0
    nz2p = 0
    nz2h_d = 100000
    nz2p_d = 100000
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans.append(Human(human_id,human_x, human_y))
        #print("Human #%d: %d, %d" % (human_id, human_x, human_y), file=sys.stderr, flush=True)
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        z2h_d, hID = get_distance_to_nearest(zombie_x, zombie_x, humans)
        z2p_d = get_distance([zombie_x, zombie_y],[x, y])
        zombies.append(Zombie(zombie_id, zombie_x, zombie_y, z2p_d, z2h_d))
        # is zombie dangerously close to human?
        if z2h_d < 1000:
            print("HUMAN in danger!", file=sys.stderr, flush=True)
            humans[hID].in_danger = True
        
        # target the zombie nearest to a human
        if z2h_d > 400 and (z2h_d < nz2h_d):
            nz2h_d = z2h_d
            nz2h = i
        if z2p_d < nz2p_d:
            nz2p_d = z2p_d
            nz2p = i
    
    for h in humans:
        print(str(h.in_danger), file=sys.stderr, flush=True)
            
        #print("Zombie `#%d: %d, %d" % (zombie_id, zombie_x, zombie_y), file=sys.stderr, flush=True)

    # print(zombies , file=sys.stderr, flush=True) 
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Your destination coordinates
    # print("0 0")

    # PRIORITY:
    # 1. zombie nearest to human
    # 2. zombie nearest to a human nearest to player
    # 3. zombie nearest to player
    
    # print(str( get_nearest_human(x,y)))
    nzid = get_nearest_zombie(x, y)
    # pd2z = get_distance([x,y],[])

    print("z2h: %d" % (nz2h_d), file=sys.stderr, flush=True)
    print("z2p: %d" % (nz2p_d), file=sys.stderr, flush=True)
    if nz2h_d < nz2p_d:
        nzid = nz2h
        print("protect humans", file=sys.stderr, flush=True)

    else:
        nzid = nz2p
        print("protect self", file=sys.stderr, flush=True)
    print("zombie #%d" % (nzid), file=sys.stderr, flush=True)
    print("%d %d" % (zombies[nzid].pos[0], zombies[nzid].pos[1]))
