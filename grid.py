#------------------------------------------------------------#
#----definition of the variables used for the coordinates----#
#------------------------------------------------------------#

#Definition of the grid in dictionary form for placing (example: A1) as unencrypted coordinates 
grille = {}                    # Dictionary for player 1 main grid
grill2 = {}                    # Dictionary for player 2 main grid
shot1 = {}                    # Dictionary for player 1 shot grid
shots2 = {}                   # Dictionary for player 2 shot grid
letters = "ABCDEFGHIJ"        # List of valid row letters

for l in letters:             # Loop through all row letters
    for n in range(1, 11):    # Loop through all column numbers from 1 to 10
        coord = f"{l}{n}"     # Build coordinate string such as "A1"
        grille[coord] = 0     # Initialize player 1 grid cell to empty
        grill2[coord] = 0     # Initialize player 2 grid cell to empty
        shot1[coord] = 0      # Initialize player 1 shot grid cell to empty
        shots2[coord] = 0     # Initialize player 2 shot grid cell to empty




#-------------------------------------------------------------#
#---------creation of the matrix for player one---------------#
#-------------------------------------------------------------#

#the grid is called to reference the dictionary as for the string f
#row = the letter of the row on the grid (A, B, C, …, J)
#col = the column number on the grid (1, 2, …, 10)

def print_gridP1():                                               # Print player 1's grid
    print(f"    1    2   3   4   5   6   7   8   9   10")          # Print column header
    print(f" A | {grille['A1']} | {grille['A2']} | {grille['A3']} | {grille['A4']} | {grille['A5']} | {grille['A6']} | {grille['A7']} | {grille['A8']} | {grille['A9']} | {grille['A10']} |")  # Row A
    print(f" B | {grille['B1']} | {grille['B2']} | {grille['B3']} | {grille['B4']} | {grille['B5']} | {grille['B6']} | {grille['B7']} | {grille['B8']} | {grille['B9']} | {grille['B10']} |")  # Row B
    print(f" C | {grille['C1']} | {grille['C2']} | {grille['C3']} | {grille['C4']} | {grille['C5']} | {grille['C6']} | {grille['C7']} | {grille['C8']} | {grille['C9']} | {grille['C10']} |")  # Row C
    print(f" D | {grille['D1']} | {grille['D2']} | {grille['D3']} | {grille['D4']} | {grille['D5']} | {grille['D6']} | {grille['D7']} | {grille['D8']} | {grille['D9']} | {grille['D10']} |")  # Row D
    print(f" E | {grille['E1']} | {grille['E2']} | {grille['E3']} | {grille['E4']} | {grille['E5']} | {grille['E6']} | {grille['E7']} | {grille['E8']} | {grille['E9']} | {grille['E10']} |")  # Row E
    print(f" F | {grille['F1']} | {grille['F2']} | {grille['F3']} | {grille['F4']} | {grille['F5']} | {grille['F6']} | {grille['F7']} | {grille['F8']} | {grille['F9']} | {grille['F10']} |")  # Row F
    print(f" G | {grille['G1']} | {grille['G2']} | {grille['G3']} | {grille['G4']} | {grille['G5']} | {grille['G6']} | {grille['G7']} | {grille['G8']} | {grille['G9']} | {grille['G10']} |")  # Row G
    print(f" H | {grille['H1']} | {grille['H2']} | {grille['H3']} | {grille['H4']} | {grille['H5']} | {grille['H6']} | {grille['H7']} | {grille['H8']} | {grille['H9']} | {grille['H10']} |")  # Row H
    print(f" I | {grille['I1']} | {grille['I2']} | {grille['I3']} | {grille['I4']} | {grille['I5']} | {grille['I6']} | {grille['I7']} | {grille['I8']} | {grille['I9']} | {grille['I10']} |")  # Row I
    print(f" J | {grille['J1']} | {grille['J2']} | {grille['J3']} | {grille['J4']} | {grille['J5']} | {grille['J6']} | {grille['J7']} | {grille['J8']} | {grille['J9']} | {grille['J10']} |")  # Row J

def shots_gridP1():                                               # Print player 1's shot grid
    print(f"    1    2   3   4   5   6   7   8   9   10")          # Print column header
    print(f" A | {shot1['A1']} | {shot1['A2']} | {shot1['A3']} | {shot1['A4']} | {shot1['A5']} | {shot1['A6']} | {shot1['A7']} | {shot1['A8']} | {shot1['A9']} | {shot1['A10']} |")  # Row A
    print(f" B | {shot1['B1']} | {shot1['B2']} | {shot1['B3']} | {shot1['B4']} | {shot1['B5']} | {shot1['B6']} | {shot1['B7']} | {shot1['B8']} | {shot1['B9']} | {shot1['B10']} |")  # Row B
    print(f" C | {shot1['C1']} | {shot1['C2']} | {shot1['C3']} | {shot1['C4']} | {shot1['C5']} | {shot1['C6']} | {shot1['C7']} | {shot1['C8']} | {shot1['C9']} | {shot1['C10']} |")  # Row C
    print(f" D | {shot1['D1']} | {shot1['D2']} | {shot1['D3']} | {shot1['D4']} | {shot1['D5']} | {shot1['D6']} | {shot1['D7']} | {shot1['D8']} | {shot1['D9']} | {shot1['D10']} |")  # Row D
    print(f" E | {shot1['E1']} | {shot1['E2']} | {shot1['E3']} | {shot1['E4']} | {shot1['E5']} | {shot1['E6']} | {shot1['E7']} | {shot1['E8']} | {shot1['E9']} | {shot1['E10']} |")  # Row E
    print(f" F | {shot1['F1']} | {shot1['F2']} | {shot1['F3']} | {shot1['F4']} | {shot1['F5']} | {shot1['F6']} | {shot1['F7']} | {shot1['F8']} | {shot1['F9']} | {shot1['F10']} |")  # Row F
    print(f" G | {shot1['G1']} | {shot1['G2']} | {shot1['G3']} | {shot1['G4']} | {shot1['G5']} | {shot1['G6']} | {shot1['G7']} | {shot1['G8']} | {shot1['G9']} | {shot1['G10']} |")  # Row G
    print(f" H | {shot1['H1']} | {shot1['H2']} | {shot1['H3']} | {shot1['H4']} | {shot1['H5']} | {shot1['H6']} | {shot1['H7']} | {shot1['H8']} | {shot1['H9']} | {shot1['H10']} |")  # Row H
    print(f" I | {shot1['I1']} | {shot1['I2']} | {shot1['I3']} | {shot1['I4']} | {shot1['I5']} | {shot1['I6']} | {shot1['I7']} | {shot1['I8']} | {shot1['I9']} | {shot1['I10']} |")  # Row I
    print(f" J | {shot1['J1']} | {shot1['J2']} | {shot1['J3']} | {shot1['J4']} | {shot1['J5']} | {shot1['J6']} | {shot1['J7']} | {shot1['J8']} | {shot1['J9']} | {shot1['J10']} |")  # Row J


#-------------------------------------------------------------#
#---------creation of the matrix for player two---------------#
#-------------------------------------------------------------#

#the grid is called to reference the dictionary as for the string f
#row = the letter of the row on the grid (A, B, C, …, J)
#col = the column number on the grid (1, 2, …, 10)

def print_gridP2():                                               # Print player 2's grid
    print(f"    1    2   3   4   5   6   7   8   9   10")          # Print column header
    print(f" A | {grill2['A1']} | {grill2['A2']} | {grill2['A3']} | {grill2['A4']} | {grill2['A5']} | {grill2['A6']} | {grill2['A7']} | {grill2['A8']} | {grill2['A9']} | {grill2['A10']} |")  # Row A
    print(f" B | {grill2['B1']} | {grill2['B2']} | {grill2['B3']} | {grill2['B4']} | {grill2['B5']} | {grill2['B6']} | {grill2['B7']} | {grill2['B8']} | {grill2['B9']} | {grill2['B10']} |")  # Row B
    print(f" C | {grill2['C1']} | {grill2['C2']} | {grill2['C3']} | {grill2['C4']} | {grill2['C5']} | {grill2['C6']} | {grill2['C7']} | {grill2['C8']} | {grill2['C9']} | {grill2['C10']} |")  # Row C
    print(f" D | {grill2['D1']} | {grill2['D2']} | {grill2['D3']} | {grill2['D4']} | {grill2['D5']} | {grill2['D6']} | {grill2['D7']} | {grill2['D8']} | {grill2['D9']} | {grill2['D10']} |")  # Row D
    print(f" E | {grill2['E1']} | {grill2['E2']} | {grill2['E3']} | {grill2['E4']} | {grill2['E5']} | {grill2['E6']} | {grill2['E7']} | {grill2['E8']} | {grill2['E9']} | {grill2['E10']} |")  # Row E
    print(f" F | {grill2['F1']} | {grill2['F2']} | {grill2['F3']} | {grill2['F4']} | {grill2['F5']} | {grill2['F6']} | {grill2['F7']} | {grill2['F8']} | {grill2['F9']} | {grill2['F10']} |")  # Row F
    print(f" G | {grill2['G1']} | {grill2['G2']} | {grill2['G3']} | {grill2['G4']} | {grill2['G5']} | {grill2['G6']} | {grill2['G7']} | {grill2['G8']} | {grill2['G9']} | {grill2['G10']} |")  # Row G
    print(f" H | {grill2['H1']} | {grill2['H2']} | {grill2['H3']} | {grill2['H4']} | {grill2['H5']} | {grill2['H6']} | {grill2['H7']} | {grill2['H8']} | {grill2['H9']} | {grill2['H10']} |")  # Row H
    print(f" I | {grill2['I1']} | {grill2['I2']} | {grill2['I3']} | {grill2['I4']} | {grill2['I5']} | {grill2['I6']} | {grill2['I7']} | {grill2['I8']} | {grill2['I9']} | {grill2['I10']} |")  # Row I
    print(f" J | {grill2['J1']} | {grill2['J2']} | {grill2['J3']} | {grill2['J4']} | {grill2['J5']} | {grill2['J6']} | {grill2['J7']} | {grill2['J8']} | {grill2['J9']} | {grill2['J10']} |")  # Row J

def shots_gridP2():                                               # Print player 2's shot grid
    print(f"    1    2   3   4   5   6   7   8   9   10")          # Print column header
    print(f" A | {shots2['A1']} | {shots2['A2']} | {shots2['A3']} | {shots2['A4']} | {shots2['A5']} | {shots2['A6']} | {shots2['A7']} | {shots2['A8']} | {shots2['A9']} | {shots2['A10']} |")  # Row A
    print(f" B | {shots2['B1']} | {shots2['B2']} | {shots2['B3']} | {shots2['B4']} | {shots2['B5']} | {shots2['B6']} | {shots2['B7']} | {shots2['B8']} | {shots2['B9']} | {shots2['B10']} |")  # Row B
    print(f" C | {shots2['C1']} | {shots2['C2']} | {shots2['C3']} | {shots2['C4']} | {shots2['C5']} | {shots2['C6']} | {shots2['C7']} | {shots2['C8']} | {shots2['C9']} | {shots2['C10']} |")  # Row C
    print(f" D | {shots2['D1']} | {shots2['D2']} | {shots2['D3']} | {shots2['D4']} | {shots2['D5']} | {shots2['D6']} | {shots2['D7']} | {shots2['D8']} | {shots2['D9']} | {shots2['D10']} |")  # Row D
    print(f" E | {shots2['E1']} | {shots2['E2']} | {shots2['E3']} | {shots2['E4']} | {shots2['E5']} | {shots2['E6']} | {shots2['E7']} | {shots2['E8']} | {shots2['E9']} | {shots2['E10']} |")  # Row E
    print(f" F | {shots2['F1']} | {shots2['F2']} | {shots2['F3']} | {shots2['F4']} | {shots2['F5']} | {shots2['F6']} | {shots2['F7']} | {shots2['F8']} | {shots2['F9']} | {shots2['F10']} |")  # Row F
    print(f" G | {shots2['G1']} | {shots2['G2']} | {shots2['G3']} | {shots2['G4']} | {shots2['G5']} | {shots2['G6']} | {shots2['G7']} | {shots2['G8']} | {shots2['G9']} | {shots2['G10']} |")  # Row G
    print(f" H | {shots2['H1']} | {shots2['H2']} | {shots2['H3']} | {shots2['H4']} | {shots2['H5']} | {shots2['H6']} | {shots2['H7']} | {shots2['H8']} | {shots2['H9']} | {shots2['H10']} |")  # Row H
    print(f" I | {shots2['I1']} | {shots2['I2']} | {shots2['I3']} | {shots2['I4']} | {shots2['I5']} | {shots2['I6']} | {shots2['I7']} | {shots2['I8']} | {shots2['I9']} | {shots2['I10']} |")  # Row I
    print(f" J | {shots2['J1']} | {shots2['J2']} | {shots2['J3']} | {shots2['J4']} | {shots2['J5']} | {shots2['J6']} | {shots2['J7']} | {shots2['J8']} | {shots2['J9']} | {shots2['J10']} |")  # Row J

#-------------------------------------------------------------#
#-----------------------printing grids------------------------#
#-------------------------------------------------------------#
print("Grid J1-------------------------------------")   # Print title for player 1 grid
print_gridP1()                                         # Print player 1 grid
#print("Grid J2-------------------------------------") # (Commented) Print player 2 grid title
#print_gridP2()                                        # (Commented) Print player 2 grid
#je l'ai mis en commentaire car je le definis dans boats pour le placement logique( A ENLEVER)
# I commented it out because I define it inside boats for logical placement (REMOVE LATER)
