import sys
import math

class Hero(object):
    pos = []
    prev_pos = []
    speed = 0
    turning = False
    boosting = False
    def __init__(self):
        self.pos = []
        self.prev_pos = []
        self.speed = 0
        self.turning = False
        self.boosting = False
        #self.reset_view()
        
    def distance_to_obj(self,there):
        return math.sqrt(((self.pos[0]-there[0])**2) + ((self.pos[1]-there[1])**2))
        
    def reset_view(self):
        self.turning = False
        self.boosting = False
        self.speed = self.get_speed()
        
    def set_pos(self,x,y):
        self.pos = [x,y]
        if len(self.prev_pos) == 0:
            self.prev_pos = [x,y]
        
    def set_prev_pos(self,x,y):
        self.prev_pos = [x,y]
        
    def get_move(self):
        dto = self.distance_to_obj([opponent_x,opponent_y])
        #xoc = (next_checkpoint_x+opponent_x)/2
        #yoc = (next_checkpoint_y+opponent_y)/2
        print >> sys.stderr, "D to enemy: "+str(dto)
        #print >> sys.stderr, "Debug: "+str([next_checkpoint_dist,dto])
        pspeed = me.get_speed()#distance_to_obj([x,y],pxy)
        #ospeed = en.get_speed()#distance_to_obj([opponent_x,opponent_y],oxy)
        #me.set_prev_pos(x,y) #pxy = [x,y]
        #oxy = [opponent_x,opponent_y]
        print >> sys.stderr, "SPEEDs: "+str(pspeed)#+" vs "+str(ospeed)
        
        
        
        # angles and boost
        if next_checkpoint_angle==0 and next_checkpoint_dist>5000:
            t="BOOST"
            me.boosting = True
            print >> sys.stderr, "BOOST"
        elif next_checkpoint_angle>45 or next_checkpoint_angle<-45:
            t = 50
            me.turning = True
            print >> sys.stderr, "TURN CORRECTION"
        elif next_checkpoint_angle>90 or next_checkpoint_angle<-90:
            print >> sys.stderr, "TURN CORNER"
            t = 0
            me.turning = True
        #elif next_checkpoint_dist<3000 and next_checkpoint_angle!=0:
        #    t = (next_checkpoint_dist/3000)*100+40
        #    print >> sys.stderr, "TURN CORRECTION"
        else:
            t=100
            print >> sys.stderr, "CRUISE"
        
        # bump enemy
        xoff = 0 
        yoff = 0
        if next_checkpoint_dist>4000 and next_checkpoint_dist<8000 and next_checkpoint_dist>dto:
            if x > opponent_x:
                xoff = -1000
            else:
                xoff = 1000
            if y > opponent_y:
                yoff = -1000
            else:
                yoff = 1000
            
            if dto < 900 and self.get_speed>700 and not me.turning and not me.boosting and len(cp)>2:
                t="SHIELD"
                print >> sys.stderr, "SHIELD!"
            print >> sys.stderr, "BUMP!: "+str([xoff,yoff])
            
        # activate shield
        # only when between CP and EN
        print >> sys.stderr, "SHIELD? %s" % (dto < 1000)
        print >> sys.stderr, "SHIELD? %s" % (self.get_speed>700)
        print >> sys.stderr, "SHIELD? %s" % (not me.turning)
        print >> sys.stderr, "SHIELD? %s" % (not me.boosting)
        #if dto < 900 and self.get_speed>500 and not me.turning and not me.boosting:
        #    t="SHIELD"
        #    print >> sys.stderr, "SHIELD!"
        return str(next_checkpoint_x+xoff) + " " + str(next_checkpoint_y+yoff) + " " + str(t)
        
    def get_speed(self):
        self.speed = self.distance_to_obj(self.prev_pos)
        return self.distance_to_obj(self.prev_pos)

class Enemy(object):
    def __init__(self):
        self.pos = []
        self.prev_pos = []
        self.speed = 0
        #self.turning = False
        #self.boosting = False
        
    def distance_to_obj(self,there):
        return math.sqrt(((self.pos[0]-there[0])**2) + ((self.pos[1]-there[1])**2))
        
    def set_pos(self,x,y):
        self.pos = [x,y]
        if len(self.prev_pos) == 0:
            self.prev_pos = [x,y]
        
    def set_prev_pos(self,x,y):
        self.prev_pos = [x,y]
        
    def get_speed(self):
        self.speed = self.distance_to_obj(self.prev_pos)
        return self.distance_to_obj(self.prev_pos)
        
        
        
cp = []
me = Hero()
en = Enemy()

def collect_cp(cpx,cpy):
    if len(cp) == 0:
        cp.append([cpx,cpy])
        return
    found = False
    for i in range(len(cp)):
        if cp[i][0] == cpx and cp[i][1] == cpy:
            found = True
    if not found:
        cp.append([cpx,cpy])
        
def distance_to_obj(a,b):
    return math.sqrt(((a[0]-b[0])**2) + ((a[1]-b[1])**2))
 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.      

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in raw_input().split()]
    opponent_x, opponent_y = [int(i) for i in raw_input().split()]
    en.set_pos(opponent_x,opponent_y)
    me.set_pos(x,y)
    me.turning = False
    me.boosting = False

    collect_cp(next_checkpoint_x,next_checkpoint_y)
    print >> sys.stderr, "CP collection: "+str(len(cp))
    
    # get speeds
    #try:
    #  oxy
    #except NameError:
    #  pxy = [x,y]
    #  oxy = [opponent_x,opponent_y]
    mt = me.get_move()
    
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    #print >> sys.stderr, "Debug: "+str([x,y,next_checkpoint_dist])
    
    # OUTPUT!    
    print mt#str(next_checkpoint_x+xoff) + " " + str(next_checkpoint_y+yoff) + " " + str(t)
    


            
