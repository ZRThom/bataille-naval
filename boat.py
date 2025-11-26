from grid import *


#-------------------------------------------------------------#
#--------------GLOBAL VERIFICATIONS---------------------------#
#-------------------------------------------------------------#

def is_valid_placement(start, size, orientation, grid):
    start = start.upper()
    row = start[0]
    col = int(start[1:])
    
    # Vérification des limites de la grille
    if orientation == 'H' and col + size - 1 > 10:
        return False
    if orientation == 'V' and letters.index(row) + size > 10:
        return False
    
    # Vérification des collisions
    for i in range(size):
        if orientation == 'H':
            coord = f"{row}{col+i}"
        else:
            coord = f"{letters[letters.index(row)+i]}{col}"
        if grid[coord] != 0:
            return False
    return True


#-------------------------------------------------------------#
# ---------------to place the boat on the grid----------------#
#-------------------------------------------------------------#

def place_boat(start, size, orientation, marker, grid):
    start = start.upper()
    row = start[0]
    col = int(start[1:])
    for i in range(size):
        if orientation == 'H':
            coord = f"{row}{col+i}"
        else:
            coord = f"{letters[letters.index(row)+i]}{col}"
        grid[coord] = marker


#-------------------------------------------------------------#
#------ looking for input from the user for placing boats ----#
#-------------------------------------------------------------#

def input_boat(name, size, grid):
    while True:
        start = input(f"Case de départ pour {name} (ex: A1) : ").upper()
        orientation = input(f"Orientation (H pour horizontal, B pour vertical) : ").upper()

        if orientation not in ['H', 'B']:
            print("Orientation invalide.")
            continue
        
        if not is_valid_placement(start, size, orientation, grid):
            print("Placement impossible (collision ou dépassement). Réessayez.")
            continue
        
        place_boat(start, size, orientation, name[0].upper(), grid)
        break


#-------------------------------------------------------------#
#----------------Definition for the boats ---------------------#
#-------------------------------------------------------------#


#THE LETTER IN CAPSLOCK REPRESENTS THE BOAT ON THE GRID (SO AIRCRAFT CARRIER = A, CRUISER = C, DESTROYER = D, SUBMARINE = S, TORPEDO BOAT = T)


def aircraft_carrier(grid):
    input_boat("Aircraft Carrier", 5, grid)

def cruiser(grid):
    input_boat("Cruiser", 4, grid)

def destroyer(grid):
    input_boat("Destroyer", 3, grid)

def submarine(grid):
    input_boat("Submarine", 3, grid)

def torpedo_boat(grid):
    input_boat("Torpedo Boat", 2, grid)


# -------------------------------------------------------------#
# ---------------PLACEMENT  BOATS FOR PLAYER 1-----------------#
# -------------------------------------------------------------#

print("Placement des bateaux pour le Joueur 1 :")
aircraft_carrier(grille)
cruiser(grille)
destroyer(grille)
submarine(grille)
torpedo_boat(grille)

print("Grille du joueur 1 après placement des bateaux :")
print_gridP1()  

# -------------------------------------------------------------#
# ---------------PLACEMENT BOATS FOR PLAYER 2------------------#
# -------------------------------------------------------------#
print("Grid J2-------------------------------------")
print_gridP2()
print("Placement des bateaux pour le Joueur 2 :")
aircraft_carrier(grill2)
cruiser(grill2)
destroyer(grill2)
submarine(grill2)
torpedo_boat(grill2)
print("Grille du joueur 2 après placement des bateaux :")
print_gridP2() 
