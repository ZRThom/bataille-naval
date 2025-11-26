import grid

#a = input("blabla : ")
#print(f"ton blabla est : {a}")

# Dimensions des bateaux (en nombre de cases)
BOAT_SIZES = {
    "aircraft_carrier": 5,
    "cruiser": 4,
    "destroyer": 3,
    "submarine": 3,
    "torpedo_boat": 2
}

# Conversion colonne lettre -> index
COLS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}


def parse_coord(coord_str):
    """Convertit une coordonnée comme 'A1' en index (row, col).
    Retourne None si invalide."""
    try:
        col_letter = coord_str[0].upper()
        row_num = int(coord_str[1:])
        
        if col_letter not in COLS or not (1 <= row_num <= 10):
            return None
        
        col = COLS[col_letter]
        row = row_num - 1
        return (row, col)
    except (ValueError, IndexError):
        return None


def check_boat_placement(grid_matrix, start_coord, direction, boat_size):
    """Vérifie si on peut placer un bateau sans collision.
    
    Args:
        grid_matrix: la matrice A ou B
        start_coord: tuple (row, col) de départ
        direction: 'up', 'down', 'left', 'right'
        boat_size: taille du bateau en cases
    
    Returns:
        bool: True si le placement est valide, False sinon
    """
    row, col = start_coord
    direction = direction.lower()
    
    # Déterminer les coordonnées finales selon la direction
    if direction == 'right':
        end_col = col + boat_size - 1
        if end_col >= 10:
            return False
        for c in range(col, end_col + 1):
            if grid_matrix[row][c] != 0:
                return False
    
    elif direction == 'left':
        end_col = col - boat_size + 1
        if end_col < 0:
            return False
        for c in range(end_col, col + 1):
            if grid_matrix[row][c] != 0:
                return False
    
    elif direction == 'down':
        end_row = row + boat_size - 1
        if end_row >= 10:
            return False
        for r in range(row, end_row + 1):
            if grid_matrix[r][col] != 0:
                return False
    
    elif direction == 'up':
        end_row = row - boat_size + 1
        if end_row < 0:
            return False
        for r in range(end_row, row + 1):
            if grid_matrix[r][col] != 0:
                return False
    
    else:
        return False
    
    return True


def place_boat_on_grid(grid_matrix, start_coord, direction, boat_name, boat_size):
    """Place un bateau sur la grille en marquant les cases.
    
    Args:
        grid_matrix: la matrice A ou B
        start_coord: tuple (row, col) de départ
        direction: 'up', 'down', 'left', 'right'
        boat_name: nom du bateau
        boat_size: taille du bateau
    """
    row, col = start_coord
    direction = direction.lower()
    
    # Remplir les cases avec le nom du bateau (ou un code)
    marker = boat_name[0].upper()  # Utiliser la première lettre du bateau
    
    if direction == 'right':
        for c in range(col, col + boat_size):
            grid_matrix[row][c] = marker
    elif direction == 'left':
        for c in range(col - boat_size + 1, col + 1):
            grid_matrix[row][c] = marker
    elif direction == 'down':
        for r in range(row, row + boat_size):
            grid_matrix[r][col] = marker
    elif direction == 'up':
        for r in range(row - boat_size + 1, row + 1):
            grid_matrix[r][col] = marker


def choice():
    case = input("which case did you want to place the boat? (exemple : A1 B2): ")
    direction = input("wich direction did you want to go? (up / down / left / right): ")
    boat = input("choose your boat ( aircraft_carrier / cruiser / destroyer / submarine / torpedo_boat ): ")
    return case, direction, boat


def placement():
    case_string, direction, boat = choice()  # case_string = "A1"
    
    # Vérifier que le bateau existe
    if boat not in BOAT_SIZES:
        print(f"Erreur: bateau '{boat}' non reconnu.")
        return None
    
    # Parser la coordonnée
    coords = parse_coord(case_string)
    if coords is None:
        print(f"Erreur: coordonnée '{case_string}' invalide.")
        return None
    
    # Vérifier le placement sur la grille (joueur 1)
    boat_size = BOAT_SIZES[boat]
    if not check_boat_placement(grid.A, coords, direction, boat_size):
        print(f"Erreur: impossible de placer le bateau {boat} à {case_string} vers {direction}. Il y a une collision ou elle dépasse la grille.")
        return None
    
    # Placer le bateau sur la grille
    place_boat_on_grid(grid.A, coords, direction, boat, boat_size)
    
    print(f"✓ Placement valide: {boat} à {case_string} vers {direction}")
    print("\nGrille mise à jour:")
    grid.print_gridP1()
    
    return coords, direction, boat



def cruiser():
    pass

    
def destroyer():
    pass


def submarine():
    pass


def torpedo_boat():
    pass


def aircraft_carrier():
    pass


if __name__ == '__main__':
    result = placement()
    if result:
        coords, direction, boat = result
        print(f"Bateau placé: {boat} à {coords} vers {direction}")
 