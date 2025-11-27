from grid import *
from grid import letters

#-------------------------------------------------------------#
#--------------GLOBAL VERIFICATIONS---------------------------#
#-------------------------------------------------------------#

def is_valid_placement(start, size, orientation, grid):
    start = start.upper()
    row = start[0]
    col = int(start[1:])
    
    # Vérification limite
    if orientation == 'H' and col + size - 1 > 10:
        return False
    if orientation == 'B' and letters.index(row) + size > 10:
        return False
    
    # Vérification collision
    for i in range(size):
        if orientation == 'H':
            coord = f"{row}{col+i}"
        else:  # orientation == 'B'
            coord = f"{letters[letters.index(row)+i]}{col}"
        if grid[coord] != 0:
            return False
    return True


#-------------------------------------------------------------#
#------------------ Placement bateau --------------------------#
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
#------------------ Placement tir -----------------------------#
#-------------------------------------------------------------#

def place_shot(coord, marker, grid):
    grid[coord] = marker


#-------------------------------------------------------------#
#------------------ Fonction TIR ------------------------------#
#-------------------------------------------------------------#

def shoot(target_grid, shots_grid):
    while True:
        pos = input("Choisis une case (ex : A1) : ").upper()

        # Vérification simple
        if len(pos) < 2 or pos[0] not in letters:
            print("Coordonnée invalide.")
            continue

        try:
            col = int(pos[1:])
        except:
            print("Coordonnée invalide.")
            continue

        if col < 1 or col > 10:
            print("Coordonnée invalide.")
            continue

        # Déjà tiré ?
        if shots_grid[pos] != 0:
            print("already shot here.")
            continue

        # Touché ?
        if target_grid[pos] != 0:
            print("HIT !")
            place_shot(pos, "X", shots_grid)
            target_grid[pos] = "x"
        else:
            print("missed.")
            place_shot(pos, "O", shots_grid)

        break

#-------------------------------------------------------------#
#------ Placement des bateaux avec tes orientations ----------#
#-------------------------------------------------------------#

def input_boat(name, size, grid):
    while True:
        start = input(f"Case de départ pour {name} (ex: A1) : ").upper()
        orientation = input("Orientation (H = horizontal, B = vertical) : ").upper()

        if orientation not in ['H', 'B']:
            print("Orientation invalide.")
            continue
        
        if not is_valid_placement(start, size, orientation, grid):
            print("Incorrect placement.")
            continue
        
        place_boat(start, size, orientation, name[0].upper(), grid)
        break


#-------------------------------------------------------------#
#------------------ Définition des bateaux -------------------#
#-------------------------------------------------------------#

def aircraft_carrier(grid): input_boat("Porte-avion", 5, grid)
def cruiser(grid):          input_boat("Croiseur", 4, grid)
def destroyer(grid):        input_boat("Destroyer", 3, grid)
def submarine(grid):        input_boat("Sous-marin", 3, grid)
def torpedo_boat(grid):     input_boat("Torpilleur", 2, grid)


#-------------------------------------------------------------#
#--------------------- Placement J1 ---------------------------#
#-------------------------------------------------------------#

print("Boat placement of player 1 :")
aircraft_carrier(grille)
cruiser(grille)
destroyer(grille)
submarine(grille)
torpedo_boat(grille)

print("\nPlayer's 1 grid :")
print_gridP1()


#-------------------------------------------------------------#
#--------------------- Placement J2 ---------------------------#
#-------------------------------------------------------------#

print("\nBoat placement of player 1 :")
aircraft_carrier(grill2)
cruiser(grill2)
destroyer(grill2)
submarine(grill2)
torpedo_boat(grill2)

print("\nPlayer's 2 grid :")
print_gridP2()


#-------------------------------------------------------------#
#------------------------ JEU --------------------------------#
#-------------------------------------------------------------#

print("\n=== GAME START NOW ===")

while True:

    # ----------------------- TOUR J1 ------------------------
    print("\n--- Tour du Joueur 1 ---")
    shots_gridP2()
    shoot(grill2, shots2)

    # victoire J1 ?
    if all(v == 0 or v == "x" for v in grill2.values()):
        print("Payer 1 win !")
        break

    # ----------------------- TOUR J2 ------------------------
    print("\n--- Tour du Joueur 2 ---")
    shots_gridP1()
    shoot(grille, shot1)

    if all(v == 0 or v == "x" for v in grille.values()):
        print("Player 2 win !")
        break
