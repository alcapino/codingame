import sys
import math
from operator import attrgetter

grid = []
open_set = []
closed_set = []
nodes = {}

class Node(object):
    def __init__(self, stn_id, name, lat, lon, stn_type):
        self.name = name[1:-1]
        self.lat = float(lat)
        self.lon = float(lon)
        self.f = 0
        self.g = 100000000000.000
        self.h = 0
        self.neighbors = []
        self.previous = None
        
    def distanceTo(self, b):
        # math.sqrt(((s[0]-b[0])**2) + ((s[1]-b[1])**2))
        d = math.sqrt(
                ((b.lon - self.lon) * math.cos((self.lat + b.lat)/2))**2 + 
                (b.lat - self.lat)**2
            ) * 6371
        return d
        
    def heuristic(self, b):
        # math.sqrt(((s[0]-b[0])**2) + ((s[1]-b[1])**2))
        d = math.sqrt(
                ((b.lon - self.lon) * math.cos((self.lat + b.lat)/2))**2 + 
                (b.lat - self.lat)**2
            ) * 6371
        return d
    
    def get_neighbors():
        return self.neighbors



# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

start_point = (raw_input().split(":"))[1]
end_point = (raw_input().split(":"))[1]
print >> sys.stderr, str(start_point)
print >> sys.stderr, str(end_point)

# set nodes
n = int(raw_input())
for i in xrange(n):
    stop_name = raw_input()
    stn_id, name, desc, lat, lon, zid, url, stn_type, stn_mother = stop_name.split(",")
    #print >> sys.stderr, stop_name.split(",")
    stn_id = (stn_id.split(":"))[1]
    nd = Node(stn_id, name, lat, lon, stn_type)
    nodes.update({stn_id: nd})
    
# set connections
m = int(raw_input())
for i in xrange(m):
    route = raw_input().split()
    a = (route[0].split(":"))[1]
    b = (route[1].split(":"))[1]
    nodes[a].neighbors.append(b)
    #print >> sys.stderr, route.split()
    
#print >> sys.stderr, "nodes: "+str(nodes)
for k, v in nodes.items():
    print >> sys.stderr, k+".neighbors: "+str(v.neighbors)
    
# setup starting values
done = False
success = False
end_node = nodes[end_point]
nodes[start_point].g = 0
open_set.append(start_point)


# start!
while not done:
    print >> sys.stderr, "open_set: "+str(open_set)
    print >> sys.stderr, "closed_set: "+str(closed_set)
    if len(open_set) > 0:
        
        # get lowest cost node in open_set
        best_node = 0 #min(nodes[], key=nodes[].f)
        for i in range(len(open_set)):
            if nodes[open_set[i]].f < nodes[open_set[best_node]].f:
                best_node = i
                print >> sys.stderr, "best node changed!"
        current = open_set[best_node] # lowest cost
        curr_node = nodes[current]
        print >> sys.stderr, "current: "+str(current)
        
        # if current is goal, its done!
        if current == end_point:
            done = True
            success = True
            print >> sys.stderr, "DONE!"
            continue
            
        # close current, then get current's neighbors, then add them to open
        open_set.remove(current)
        closed_set.append(current)
        nb = curr_node.neighbors
        for i in range(len(nb)):
            neighbor = nb[i]
            nb_node = nodes[neighbor]
            # if neighbor is in closed_set, continue
            if neighbor in closed_set:
                continue
            else:
                # else evaluate their 'g': e.g. distance from start
                #neighbor.g = nodes[current].g # plus something else
                temp_g = nodes[current].g + nb_node.distanceTo(curr_node)
                
                # heuristic from neighbor to end, TODO: add other variables
                # set neighbor's 'h': e.g. distance from neighbor to end
                nb_node.h = nb_node.heuristic(end_node)
                print >> sys.stderr, "temp_g: "+str(temp_g)
                # if neighbor is in open_set and 'g' is lower, then replace previous
                if neighbor in open_set:
                    if temp_g < nb_node.g:
                        nb_node.g = temp_g
                else:
                    # else put it in open_set
                    open_set.append(neighbor)
                    nb_node.g = temp_g
                    
            # set neighbor's 'f': g + h
            nb_node.f = nb_node.g + nb_node.h
            
            # set current as 'previous'
            nb_node.previous = current
            
    else:        
        done = True
        ans = "IMPOSSIBLE"
        continue
    
# TODO: find the path
path = []
path.insert(0, current)
while curr_node.previous:
    path.insert(0,curr_node.previous)
    curr_node = nodes[curr_node.previous]

print >> sys.stderr, "path: "+str(path)
if success:
    for i in range(len(path)):
        print nodes[path[i]].name
else:
    print "IMPOSSIBLE"
    

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

#print "IMPOSSIBLE"
#print ans
