from grid import *
from grid import letters

#-------------------------------------------------------------#
#-------------- GLOBAL VERIFICATIONS --------------------------#
#-------------------------------------------------------------#

def is_valid_placement(start, size, orientation, grid):
    start = start.upper()
    row = start[0]
    col = int(start[1:])
    
    # Boundary check
    if orientation == 'H' and col + size - 1 > 10:
        return False
    if orientation == 'B' and letters.index(row) + size > 10:
        return False
    
    # Collision check
    for i in range(size):
        if orientation == 'H':
            coord = f"{row}{col+i}"
        else:  # orientation == 'B'
            coord = f"{letters[letters.index(row)+i]}{col}"
        if grid[coord] != 0:
            return False
    return True

#-------------------------------------------------------------#
#------------------ Boat Placement ----------------------------#
#-------------------------------------------------------------#

def place_boat(start, size, orientation, marker, grid):
    start = start.upper()
    row = start[0]
    col = int(start[1:])
    for i in range(size):
        if orientation == 'H':
            coord = f"{row}{col+i}"
        else:  # 'B'
            coord = f"{letters[letters.index(row)+i]}{col}"
        grid[coord] = marker

#-------------------------------------------------------------#
#------------------ Shot Placement ----------------------------#
#-------------------------------------------------------------#

def place_shot(coord, marker, grid):
    grid[coord] = marker

#-------------------------------------------------------------#
#------------------------ SHOOT -------------------------------#
#-------------------------------------------------------------#

def shoot(target_grid, shots_grid):
    while True:
        pos = input("Choose a cell (ex: A1): ").upper()

        # Basic validation
        if len(pos) < 2 or pos[0] not in letters:
            print("Invalid coordinate.")
            continue

        try:
            col = int(pos[1:])
        except:
            print("Invalid coordinate.")
            continue

        if col < 1 or col > 10:
            print("Invalid coordinate.")
            continue

        # Already shot here?
        if shots_grid[pos] != 0:
            print("Already shot here.")
            continue

        # Hit?
        if target_grid[pos] != 0:
            print("HIT!")
            place_shot(pos, "X", shots_grid)
            target_grid[pos] = "x"
        else:
            print("Missed.")
            place_shot(pos, "O", shots_grid)

        break

#-------------------------------------------------------------#
#---------- Boat placement with your orientations -------------#
#-------------------------------------------------------------#

def input_boat(name, size, grid):
    while True:
        start = input(f"Starting cell for {name} (ex: A1): ").upper()
        orientation = input("Orientation (H = horizontal, B = vertical): ").upper()

        if orientation not in ['H', 'B']:
            print("Invalid orientation.")
            continue
        
        if not is_valid_placement(start, size, orientation, grid):
            print("Incorrect placement.")
            continue
        
        place_boat(start, size, orientation, name[0].upper(), grid)
        break

#-------------------------------------------------------------#
#------------------ Boat Definitions --------------------------#
#-------------------------------------------------------------#

def aircraft_carrier(grid): input_boat("Aircraft Carrier", 5, grid)
def cruiser(grid):          input_boat("Cruiser", 4, grid)
def destroyer(grid):        input_boat("Destroyer", 3, grid)
def submarine(grid):        input_boat("Submarine", 3, grid)
def torpedo_boat(grid):     input_boat("Torpedo Boat", 2, grid)

#-------------------------------------------------------------#
#-------------------- Player 1 Placement ---------------------#
#-------------------------------------------------------------#

print("Boat placement of player 1:")
aircraft_carrier(grille)
cruiser(grille)
destroyer(grille)
submarine(grille)
torpedo_boat(grille)

print("\nPlayer 1 grid:")
print_gridP1()

#-------------------------------------------------------------#
#-------------------- Player 2 Placement ---------------------#
#-------------------------------------------------------------#

print("\nBoat placement of player 2:")
aircraft_carrier(grill2)
cruiser(grill2)
destroyer(grill2)
submarine(grill2)
torpedo_boat(grill2)

print("\nPlayer 2 grid:")
print_gridP2()
 
#-------------------------------------------------------------#
#--------------------------- GAME -----------------------------#
#-------------------------------------------------------------#

print("\n=== GAME START NOW ===")

while True:

    # ----------------------- TURN P1 ------------------------
    print("\n--- Player 1 Turn ---")
    shots_gridP2()
    shoot(grill2, shots2)

    # Player 1 victory?
    if all(v == 0 or v == "x" for v in grill2.values()):
        print("Player 1 wins!")
        break

    # ----------------------- TURN P2 ------------------------
    print("\n--- Player 2 Turn ---")
    shots_gridP1()
    shoot(grille, shot1)

    if all(v == 0 or v == "x" for v in grille.values()):
        print("Player 2 wins!")
        break
