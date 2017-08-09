import sys
import math

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
floor_going_right = [-1] * nb_floors
elevators = [-1] * nb_floors
for i in xrange(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in raw_input().split()]
    elevators[elevator_floor] = elevator_pos
    

elevators = [x for x in elevators if x != -1]

# game loop
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = raw_input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    action = "WAIT"
    
    print >> sys.stderr, "exit_floor: "+str(exit_floor)
    print >> sys.stderr, "clone_floor: "+str(clone_floor)
    print >> sys.stderr, "clone_pos: "+str(clone_pos)
    print >> sys.stderr, "elevators: "+str(elevators)
    print >> sys.stderr, "floor_going_right: "+str(floor_going_right)
    
    #if floor_going_right[clone_floor] == -1:
    #    floor_going_right[clone_floor] = True
    
    if clone_floor == -1 or clone_pos == -1:
        action = "WAIT"
    elif clone_floor < len(elevators):
        print >> sys.stderr, "FLOOR HAS ELEVATOR"
        # riding elevator
        if clone_pos == elevators[clone_floor]:
            action = "WAIT"
            if floor_going_right[clone_floor+1] == -1:
                floor_going_right[clone_floor+1] = floor_going_right[clone_floor]
            print >> sys.stderr, "IN ELEVATOR"
        # if heading away from exit/elevator
        elif (clone_pos > elevators[clone_floor] and floor_going_right[clone_floor]) or (clone_pos < elevators[clone_floor] and not floor_going_right[clone_floor]):
            print >> sys.stderr, "elevpos: "+str(elevators[clone_floor])
            print >> sys.stderr, "gright: "+str(floor_going_right[clone_floor])
            print >> sys.stderr, "left of bot: "+str(clone_pos > elevators[clone_floor] and floor_going_right[clone_floor])
            print >> sys.stderr, "right of bot: "+str(clone_pos < elevators[clone_floor] and not floor_going_right[clone_floor])
            print >> sys.stderr, "MOVING AWAY FROM ELEVATOR"
            action = "BLOCK"
    # check if on exit floor and heading away from exit
    elif clone_floor == exit_floor:
        print >> sys.stderr, "FLOOR HAS EXIT"
        if (clone_pos > exit_pos and floor_going_right[clone_floor]) or (clone_pos < exit_pos and not floor_going_right[clone_floor]):
            print >> sys.stderr, "MOVING AWAY FROM EXIT"
            action = "BLOCK"
        
    if action == "BLOCK":
        floor_going_right[clone_floor] = not floor_going_right[clone_floor]

    # action: WAIT or BLOCK
    print >> sys.stderr, str(action)
    print str(action)
