from grid import *                 # Import everything from the grid module
from grid import letters           # Import the list of row letters

#-------------------------------------------------------------#
#-------------- GLOBAL VERIFICATIONS --------------------------#
#-------------------------------------------------------------#

def is_valid_placement(start, size, orientation, grid):   # Check if a boat placement is valid
    start = start.upper()                                 # Normalize the starting cell to uppercase
    row = start[0]                                        # Extract the row letter
    col = int(start[1:])                                  # Extract the column number
    
    # Boundary check
    if orientation == 'H' and col + size - 1 > 10:        # Check horizontal boundary overflow
        return False                                      # Invalid placement horizontally
    if orientation == 'B' and letters.index(row) + size > 10:  # Check vertical boundary overflow
        return False                                      # Invalid placement vertically
    
    # Collision check
    for i in range(size):                                 # Loop through each part of the boat
        if orientation == 'H':                            # If horizontally placed
            coord = f"{row}{col+i}"                       # Calculate horizontal coordinate
        else:                                             # Otherwise vertically placed
            coord = f"{letters[letters.index(row)+i]}{col}"  # Calculate vertical coordinate
        if grid[coord] != 0:                              # Check if the cell is already occupied
            return False                                  # Placement invalid due to collision
    return True                                           # Placement is valid

#-------------------------------------------------------------#
#------------------ Boat Placement ----------------------------#
#-------------------------------------------------------------#

def place_boat(start, size, orientation, marker, grid):   # Place a boat on the grid
    start = start.upper()                                 # Normalize input
    row = start[0]                                        # Get row
    col = int(start[1:])                                  # Get column
    for i in range(size):                                 # Place each part of the boat
        if orientation == 'H':                            # Horizontal placement
            coord = f"{row}{col+i}"                       # Compute coordinate
        else:                                             # Vertical placement
            coord = f"{letters[letters.index(row)+i]}{col}"  # Compute coordinate
        grid[coord] = marker                              # Mark the cell with boat identifier

#-------------------------------------------------------------#
#------------------ Shot Placement ----------------------------#
#-------------------------------------------------------------#

def place_shot(coord, marker, grid):     # Place a shot marker (hit or miss)
    grid[coord] = marker                 # Update the grid at the given coordinate

#-------------------------------------------------------------#
#------------------------ SHOOT -------------------------------#
#-------------------------------------------------------------#

def shoot(target_grid, shots_grid):                          # Handle a player taking a shot
    while True:                                               # Loop until a valid shot is made
        pos = input("Choose a cell (ex: A1): ").upper()       # Ask player for a target cell

        # Basic validation
        if len(pos) < 2 or pos[0] not in letters:             # Check format and row
            print("Invalid coordinate.")                      # Display error
            continue                                          # Retry

        try:
            col = int(pos[1:])                                # Try converting column
        except:
            print("Invalid coordinate.")                      # Error if conversion fails
            continue                                          # Retry

        if col < 1 or col > 10:                               # Check column boundaries
            print("Invalid coordinate.")                      # Error message
            continue                                          # Retry

        # Already shot here?
        if shots_grid[pos] != 0:                              # Check if cell already targeted
            print("Already shot here.")                       # Inform user
            continue                                          # Retry

        # Hit?
        if target_grid[pos] != 0:                             # If the opponent has a boat here
            print("HIT!")                                     # Inform user
            place_shot(pos, "X", shots_grid)                  # Mark hit on shots grid
            target_grid[pos] = "x"                            # Mark hit on target grid
        else:
            print("Missed.")                                  # Missed shot
            place_shot(pos, "O", shots_grid)                  # Mark miss on shots grid

        break                                                 # Break the loop after valid shot

#-------------------------------------------------------------#
#---------- Boat placement with your orientations -------------#
#-------------------------------------------------------------#

def input_boat(name, size, grid):                                  # Ask user to place a specific boat
    while True:                                                    # Loop until valid placement
        start = input(f"Starting cell for {name} (ex: A1): ").upper()  # Request starting cell
        orientation = input("Orientation (H = horizontal, B = vertical): ").upper()  # Request orientation

        if orientation not in ['H', 'B']:                          # Check valid orientation
            print("Invalid orientation.")                          # Error message
            continue                                               # Retry
        
        if not is_valid_placement(start, size, orientation, grid): # Validate placement
            print("Incorrect placement.")                          # Invalid placement message
            continue                                               # Retry
        
        place_boat(start, size, orientation, name[0].upper(), grid)  # Place boat with its initial letter
        break                                                      # Stop loop when boat is placed

#-------------------------------------------------------------#
#------------------ Boat Definitions --------------------------#
#-------------------------------------------------------------#

def aircraft_carrier(grid): input_boat("Aircraft Carrier", 5, grid)  # Aircraft carrier is size 5
def cruiser(grid):          input_boat("Cruiser", 4, grid)           # Cruiser is size 4
def destroyer(grid):        input_boat("Destroyer", 3, grid)         # Destroyer is size 3
def submarine(grid):        input_boat("Submarine", 3, grid)         # Submarine is size 3
def torpedo_boat(grid):     input_boat("Torpedo Boat", 2, grid)      # Torpedo boat is size 2

#-------------------------------------------------------------#
#--------------------- Player 1 Placement ----------------------#
#-------------------------------------------------------------#

print("Boat placement of player 1:")     # Announce start of player 1 boat placement
aircraft_carrier(grille)                 # Place aircraft carrier for player 1
cruiser(grille)                          # Place cruiser for player 1
destroyer(grille)                        # Place destroyer for player 1
submarine(grille)                        # Place submarine for player 1
torpedo_boat(grille)                     # Place torpedo boat for player 1

print("\nPlayer 1 grid:")                # Display player 1 grid
print_gridP1()                           # Print player 1 grid

#-------------------------------------------------------------#
#--------------------- Player 2 Placement ----------------------#
#-------------------------------------------------------------#

print("\nBoat placement of player 2:")   # Announce start of player 2 boat placement
aircraft_carrier(grill2)                 # Place aircraft carrier for player 2
cruiser(grill2)                          # Place cruiser for player 2
destroyer(grill2)                        # Place destroyer for player 2
submarine(grill2)                        # Place submarine for player 2
torpedo_boat(grill2)                     # Place torpedo boat for player 2

print("\nPlayer 2 grid:")                # Display player 2 grid
print_gridP2()                           # Print player 2 grid
 
#-------------------------------------------------------------#
#--------------------------- GAME -----------------------------#
#-------------------------------------------------------------#

print("\n=== GAME START NOW ===")        # Announce game start

while True:                               # Main game loop

    # ----------------------- TURN P1 ------------------------
    print("\n--- Player 1 Turn ---")     # Announce player 1 turn
    shots_gridP2()                       # Show player 1 shot grid
    shoot(grill2, shots2)                # Player 1 shoots at player 2

    # Player 1 victory?
    if all(v == 0 or v == "x" for v in grill2.values()):  # Check if player 2 has no boats left
        print("Player 1 wins!")         # Victory message
        break                           # End game

    # ----------------------- TURN P2 ------------------------
    print("\n--- Player 2 Turn ---")    # Announce player 2 turn
    shots_gridP1()                       # Show player 2 shot grid
    shoot(grille, shot1)                 # Player 2 shoots at player 1

    if all(v == 0 or v == "x" for v in grille.values()):  # Check if player 1 has no boats left
        print("Player 2 wins!")         # Victory message
        break                           # End game
