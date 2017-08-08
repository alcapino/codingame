import sys
import math

prev_pos = -1

def clone_heading():
    global prev_pos
    #prev_pos = -1
    #curr_pos = -1
    if prev_pos < 0:
        prev_pos = curr_pos
    if prev_pos > curr_pos:
        return "L"
    elif prev_pos < curr_pos:
        return "R"
    else:
        return "S"

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in raw_input().split()]
is_floor_blocked = [False] * nb_floors
elevators = []
for i in xrange(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in raw_input().split()]
    #elevators.append([elevator_floor,elevator_pos])
    elevators.insert(elevator_floor,elevator_pos)

elev = 0
prev_pos = -1

# game loop
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = raw_input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    curr_pos = clone_pos
    if prev_pos == -1:
        prev_pos = clone_pos
    clone_dir = clone_heading()
    print >> sys.stderr, "elevators: "+str(elevators)
    elev_below = -1
    if len(elevators) > 0 and clone_floor >0:
        elev_below = elevators[clone_floor-1]
    
    
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    action = "WAIT"
    
    print >> sys.stderr, "clone_floor: "+str(clone_floor)
    print >> sys.stderr, "clone_pos: "+str(clone_pos)
    #print >> sys.stderr, "clone_floor: "+str(elevators[clone_floor])
    print >> sys.stderr, "prev_pos: "+str(clone_pos)
    print >> sys.stderr, "prev_elev: "+str(elev_below)
    print >> sys.stderr, "clone_dir: "+str(clone_dir)
    print >> sys.stderr, "is_floor_blocked: "+str(is_floor_blocked)
    #print >> sys.stderr, "clone_pos: "+str(clone_pos)
    
    
    # unknown
    if clone_floor == -1 or clone_dir == "S":
        action = "WAIT"
    # check if on exit floor and heading away from
    elif clone_floor == exit_floor:
        if clone_pos > exit_pos and clone_dir != "L":
            if not is_floor_blocked[clone_floor]:
                print >> sys.stderr, ""
                action = "BLOCK"
                is_floor_blocked[clone_floor] = True
    
    # if has an elevator below, and heading away from exit/elevator
    #if clone_floor > 0:
    elif clone_pos > elevators[clone_floor] and clone_dir != "L":
        # block path leading away from elevator
        if not is_floor_blocked[clone_floor]:
            action = "BLOCK"
            is_floor_blocked[clone_floor] = True
        
    
    if clone_pos <= 0 or clone_pos >= width-1:
        action = "BLOCK"

    # action: WAIT or BLOCK
    prev_pos = clone_pos
    print >> sys.stderr, str(action)
    print str(action)
