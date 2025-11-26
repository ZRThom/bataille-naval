from grid import * 




#-------------------------------------------------------------#
#--------------GLOBAL VERIFICATIONS---------------------------#
#-------------------------------------------------------------#



#verification valid placement (rapport avec border limits , collisions(espaces deja occupés) et espaces vides)a enlever)
#upper() transfrome les inputs en majuscules pour eviter les erreurs( a enlever)

def is_valid_placement(start, size, orientation):
    start = start.upper()
    row = start[0]
    col = int(start[1:])
    
    # Verification of the border limits of the grid ( 10x10 avec valeurs horizontales et vertical=definition H et V pour inputs de direction a enlever) 

    if orientation == 'H' and col + size - 1 > 10:
        return False
    if orientation == 'V' and letters.index(row) + size > 10:
        return False
    
    #verifiaction for collision(ce qu'on avait dit hier (a enlever))
    # variable = to check the number of cells that one of the 5 boats will occupy

    for i in range(size):
        if orientation == 'H':
            coord = f"{row}{col+i}"
        else:
            coord = f"{letters[letters.index(row)+i]}{col}"
        if grille[coord] != 0:
            return False
    return True


#-------------------------------------------------------------#
# ---------------to place the boat on the grid----------------#
#-------------------------------------------------------------#

# placing the boat on the grid (a enlever)
def place_boat(start, size, orientation, marker):
    start = start.upper()
    row = start[0]
    col = int(start[1:])
    for i in range(size):
        if orientation == 'H':
            coord = f"{row}{col+i}"
        else:
            coord = f"{letters[letters.index(row)+i]}{col}"
        grille[coord] = "X"

# looking for input from the user for placing boats( user 1 choice)

def input_boat(name, size):
    while True:
        start = input(f"Case de départ pour {name} (ex: A1) : ").upper()
        orientation = input(f"Orientation (H pour horizontal, B pour vertical) : ").upper()
        if orientation not in ['H','B']:
            print("Orientation invalide.")
            continue
        if not is_valid_placement(start, size, orientation):
            print("Placement impossible (collision ou dépassement). Réessayez.")
            continue
        place_boat(start, size, orientation, name[0].upper())
        break

#-------------------------------------------------------------#
#----------------Definition for the boats and print them------#
#-------------------------------------------------------------#



def aircraft_carrier():
    input_boat("Aircraft Carrier", 5)

def cruiser():
    input_boat("Cruiser", 4)

def destroyer():
    input_boat("Destroyer", 3)

def submarine():
    input_boat("Submarine", 3)

def torpedo_boat():
    input_boat("Torpedo Boat", 2)




aircraft_carrier()
cruiser()
destroyer()
submarine()
torpedo_boat()

print("\nGrille du joueur 1 après placement des bateaux :")
print_gridP1()

