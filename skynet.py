import sys
import math

nodes = {}

class Node(object):
    def __init__(self, nid):
        self.nid = nid
        self.isExit = False
        self.cost = 0
        self.neighbors = []
        self.previous = None
    
    def get_neighbors():
        return self.neighbors
        
def add_node(n):
    if not n in nodes:
        nd = Node(n)
        nodes.update({n: nd})

def get_nearest_exit(start):
    # get all exits
    longest_path = 10000
    for n in nodes:
        if nodes[n].isExit:
            #print >> sys.stderr, "start: "+str(start)
            #print >> sys.stderr, "goal: "+str(n)
            path = pathfinder(start,n)
            #print >> sys.stderr, "cost: "+str(path) + " --------"
            if path < longest_path:
                longest_path = path
                nearest = n
    return nearest
    
# breadth-first traversal
def pathfinder(start, goal):
    queue = []
    expanded_set = []
    closed_set = []
    nodes[start].previous = None
    nodes[start].cost = 0
    nodes[goal].cost = 100000
    #cost = 0
    
    queue.insert(0,start)
    
    while len(queue) > 0:
        #print >> sys.stderr, "loop"
        #print >> sys.stderr, "queue: "+str(queue)+" ==========================="
        current = queue.pop()
        #print >> sys.stderr, "current: "+str(current)
        #print >> sys.stderr, "cost: "+str(nodes[current].cost)
        expanded_set.append(current)
        if current == goal:
            #print >> sys.stderr, "goal found as current"
            return nodes[goal].cost
            
        #print >> sys.stderr, "expand to neighbors"
        #print >> sys.stderr, "neighbors: "+str(nodes[current].neighbors)
        for n in nodes[current].neighbors:
            #print >> sys.stderr, "n: "+str(n)
            if not n in expanded_set:
                #print >> sys.stderr, "add n to set and queue"
                expanded_set.append(n)
                queue.insert(0,n)
                #print >> sys.stderr, "previous: "+str(current)
                nodes[n].previous = current
                nodes[n].cost = nodes[current].cost + 1
            #if n == goal:
            #    print >> sys.stderr, "goal found as child"
            #    return cost
        #print >> sys.stderr, "goal not found, incrementing..."
        
    return nodes[goal].cost
    
def get_path_to_node(n):
    curr_node = nodes[n]
    path = []
    path.insert(0, n)
    #print >> sys.stderr, "exit: "+str(curr_node.nid)
    while curr_node.previous:
        #print >> sys.stderr, "curr: "+str(curr_node.nid)
        #print >> sys.stderr, "curr_previous: "+str(curr_node.previous)
        path.insert(0,curr_node.previous)
        curr_node = nodes[curr_node.previous]
        #print >> sys.stderr, "curr_previous: "+str(curr_node.previous)
    return path
        
    
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in raw_input().split()]
for i in xrange(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in raw_input().split()]
    #print >> sys.stderr, "path: "+str(n1)+":"+str(n2)
    nd1 = Node(n1)
    nd2 = Node(n2)
    add_node(n1)
    add_node(n2)
    #nodes.update({n1: nd1})
    #nodes.update({n2: nd2})
    nodes[n1].neighbors.append(n2)
    nodes[n2].neighbors.append(n1)
for i in xrange(e):
    ei = int(raw_input())  # the index of a gateway node
    nodes[ei].isExit = True
#for k, v in nodes.items():
#    print >> sys.stderr, str(k)+".neighbors: "+str(v.neighbors)
#    print >> sys.stderr, str(k)+".isExit: "+str(v.isExit)

# game loop
while True:
    si = int(raw_input())  # The index of the node on which the Skynet agent is positioned this turn
    print >> sys.stderr, "si: "+str(si)
    #print >> sys.stderr, "neighbors: "+str(nodes[si].neighbors)
    # get nearest exit
    e = get_nearest_exit(si)
    print >> sys.stderr, "e: "+str(e)
    print >> sys.stderr, "e.neighbors: "+str(nodes[e].neighbors)
    p = get_path_to_node(e)
    print >> sys.stderr, "path: "+str(p)
    p1 = p[0]
    p2 = p[1]
    
    nodes[p1].neighbors.remove(p2)
    nodes[p2].neighbors.remove(p1)
    print str(p1)+" "+str(p2)

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    #print "2 3"
