# Turn-Based Gameplay & Victory Branch — README

This branch focuses on implementing the **real turn-by-turn game flow** and the **conditions for victory**.  
It builds on the previously set up grids with boats and attack mechanics, allowing the full game loop to function correctly.

---

## Purpose of This Branch

- Implement the actual **turn-based gameplay** between two players.  
- Manage switching turns in a controlled, logical sequence.  
- Integrate **victory condition checks** to determine when a player has won.  
- Ensure all verifications are in place to maintain consistent game state.  
- Provide a clear, testable implementation of the game loop.

---

## Features Included

### 1. Turn Management
- Alternates turns between Player 1 and Player 2.  
- Prints the current player’s grids (shots & boats) for reference.  
- Prompts the active player to choose a cell to attack.  
- Ensures that each turn is fully processed before switching.

### 2. Attack Integration
- Utilizes the attack and verification system from the previous branch.  
- Validates each shot, marking hits (`X`) and misses (`O`).  
- Updates both the attack grid and the target player’s boat grid.  
- Prevents repeated attacks on the same cell.

### 3. Victory Conditions
- Checks whether all boat cells of a player have been hit (`x`).  
- Declares the winner as soon as one player has no remaining boat cells.  
- Ends the game loop immediately upon victory.

### 4. Game State Verification
- Ensures each move is valid and all grids remain consistent.  
- Maintains turn integrity so that no player can act out of turn.  
- Provides feedback to the players after each shot (hit/miss).  

---

## Intended Audience

This branch is designed for:

- Developers implementing the main game loop.  
- Contributors who need to understand turn management and victory checks.  
- Team members testing the complete gameplay flow.  
- Anyone planning to extend, refactor, or debug the turn-based mechanics.

---

## How to Use This Branch

- Run the game with both players’ grids prepared and boats placed.  
- Follow the prompts to execute alternating turns.  
- Observe the feedback for each shot and monitor the grids.  
- Confirm that victory is correctly determined when all of a player’s boats are destroyed.  
- Use this branch as the foundation for AI integration, advanced scoring, or UI improvements.
