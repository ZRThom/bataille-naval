#------------------------------------------------------------#
#----definition of the variables used for the coordinates----#
#------------------------------------------------------------#

#Definition of the grid in dictionary form for placing (example: A1) as unencrypted coordinates 
grille = {}
letters = "ABCDEFGHIJ"

for l in letters:
    for n in range(1, 11):
        coord = f"{l}{n}"
        grille[coord] = 0


#-------------------------------------------------------------#
#---------creation of the matrix for player one---------------#
#-------------------------------------------------------------#

#the grid is called to reference the dictionary as for the string f

def print_gridP1():
    print(f"      1  2  3  4  5  6  7  8  9  10")
    print(f" A  | {grille['A1']} | {grille['A2']} | {grille['A3']} | {grille['A4']} | {grille['A5']} | {grille['A6']} | {grille['A7']} | {grille['A8']} | {grille['A9']} | {grille['A10']} |")
    print(f" B  | {grille['B1']} | {grille['B2']} | {grille['B3']} | {grille['B4']} | {grille['B5']} | {grille['B6']} | {grille['B7']} | {grille['B8']} | {grille['B9']} | {grille['B10']} |")
    print(f" C  | {grille['C1']} | {grille['C2']} | {grille['C3']} | {grille['C4']} | {grille['C5']} | {grille['C6']} | {grille['C7']} | {grille['C8']} | {grille['C9']} | {grille['C10']} |")
    print(f" D  | {grille['D1']} | {grille['D2']} | {grille['D3']} | {grille['D4']} | {grille['D5']} | {grille['D6']} | {grille['D7']} | {grille['D8']} | {grille['D9']} | {grille['D10']} |")
    print(f" E  | {grille['E1']} | {grille['E2']} | {grille['E3']} | {grille['E4']} | {grille['E5']} | {grille['E6']} | {grille['E7']} | {grille['E8']} | {grille['E9']} | {grille['E10']} |")
    print(f" F  | {grille['F1']} | {grille['F2']} | {grille['F3']} | {grille['F4']} | {grille['F5']} | {grille['F6']} | {grille['F7']} | {grille['F8']} | {grille['F9']} | {grille['F10']} |")
    print(f" G  | {grille['G1']} | {grille['G2']} | {grille['G3']} | {grille['G4']} | {grille['G5']} | {grille['G6']} | {grille['G7']} | {grille['G8']} | {grille['G9']} | {grille['G10']} |")
    print(f" H  | {grille['H1']} | {grille['H2']} | {grille['H3']} | {grille['H4']} | {grille['H5']} | {grille['H6']} | {grille['H7']} | {grille['H8']} | {grille['H9']} | {grille['H10']} |")
    print(f" I  | {grille['I1']} | {grille['I2']} | {grille['I3']} | {grille['I4']} | {grille['I5']} | {grille['I6']} | {grille['I7']} | {grille['I8']} | {grille['I9']} | {grille['I10']} |")
    print(f" J  | {grille['J1']} | {grille['J2']} | {grille['J3']} | {grille['J4']} | {grille['J5']} | {grille['J6']} | {grille['J7']} | {grille['J8']} | {grille['J9']} | {grille['J10']} |")


#-------------------------------------------------------------#
#---------creation of the matrix for player two---------------#
#-------------------------------------------------------------#

#the grid is called to reference the dictionary as for the string f

def print_gridP2():
    print(f"      1  2  3  4  5  6  7  8  9  10")
    print(f" A  | {grille['A1']} | {grille['A2']} | {grille['A3']} | {grille['A4']} | {grille['A5']} | {grille['A6']} | {grille['A7']} | {grille['A8']} | {grille['A9']} | {grille['A10']} |")
    print(f" B  | {grille['B1']} | {grille['B2']} | {grille['B3']} | {grille['B4']} | {grille['B5']} | {grille['B6']} | {grille['B7']} | {grille['B8']} | {grille['B9']} | {grille['B10']} |")
    print(f" C  | {grille['C1']} | {grille['C2']} | {grille['C3']} | {grille['C4']} | {grille['C5']} | {grille['C6']} | {grille['C7']} | {grille['C8']} | {grille['C9']} | {grille['C10']} |")
    print(f" D  | {grille['D1']} | {grille['D2']} | {grille['D3']} | {grille['D4']} | {grille['D5']} | {grille['D6']} | {grille['D7']} | {grille['D8']} | {grille['D9']} | {grille['D10']} |")
    print(f" E  | {grille['E1']} | {grille['E2']} | {grille['E3']} | {grille['E4']} | {grille['E5']} | {grille['E6']} | {grille['E7']} | {grille['E8']} | {grille['E9']} | {grille['E10']} |")
    print(f" F  | {grille['F1']} | {grille['F2']} | {grille['F3']} | {grille['F4']} | {grille['F5']} | {grille['F6']} | {grille['F7']} | {grille['F8']} | {grille['F9']} | {grille['F10']} |")
    print(f" G  | {grille['G1']} | {grille['G2']} | {grille['G3']} | {grille['G4']} | {grille['G5']} | {grille['G6']} | {grille['G7']} | {grille['G8']} | {grille['G9']} | {grille['G10']} |")
    print(f" H  | {grille['H1']} | {grille['H2']} | {grille['H3']} | {grille['H4']} | {grille['H5']} | {grille['H6']} | {grille['H7']} | {grille['H8']} | {grille['H9']} | {grille['H10']} |")
    print(f" I  | {grille['I1']} | {grille['I2']} | {grille['I3']} | {grille['I4']} | {grille['I5']} | {grille['I6']} | {grille['I7']} | {grille['I8']} | {grille['I9']} | {grille['I10']} |")
    print(f" J  | {grille['J1']} | {grille['J2']} | {grille['J3']} | {grille['J4']} | {grille['J5']} | {grille['J6']} | {grille['J7']} | {grille['J8']} | {grille['J9']} | {grille['J10']} |")





#-------------------------------------------------------------#
#-----------------------printing grids------------------------#
#-------------------------------------------------------------#
print_gridP1()
print_gridP2()