# Boat Placement Preparation Branch — README

This branch focuses on the **pre-game setup** by implementing the logic to **place boats on the grids** for both players.  
Its purpose is to ensure that all ships are correctly positioned before the game begins, allowing a consistent and fair start.

---

## Purpose of This Branch

- Implement boat placement logic for both players’ grids.  
- Provide verifications to ensure valid placement (boundaries, collisions, orientation).  
- Mark boats on the grids so the game is ready to start.  
- Provide a structured, isolated environment to handle pre-game setup.  
- Serve as a reference for understanding the preparation phase of the game.

---

## Features Included

### 1. Boat Placement System
- Accepts starting coordinates from the player (e.g., `A1`, `C5`).  
- Supports both orientations:
  - **Horizontal (H)**  
  - **Vertical (B)**  
- Performs **boundary checks** to ensure boats fit inside the grid.  
- Performs **collision checks** to prevent overlapping boats.  
- Marks the grid with a unique identifier for each boat type.

### 2. Grid Management
- Updates the player’s grid after each successful placement.  
- Keeps track of empty cells to prevent illegal placement.  
- Supports multiple boats of different sizes:
  - Aircraft Carrier  
  - Cruiser  
  - Destroyer  
  - Submarine  
  - Torpedo Boat

### 3. Player Setup Workflow
- Prompts players in sequence to place all their boats.  
- Provides error messages for invalid coordinates or placements.  
- Ensures both players’ grids are fully prepared before the game starts.  

---

## Intended Audience

This branch is designed for:

- Developers implementing the pre-game setup mechanics.  
- Contributors who need to understand the logic of player preparation.  
- New team members reviewing how boats are added to grids.  
- Anyone preparing to extend or modify the game setup phase.

---

## How to Use This Branch

- Follow the step-by-step boat placement prompts to position all boats.  
- Check that grids are correctly updated after each placement.  
- Use this branch as a base for integrating the attack and gameplay logic.  
- Refer to it when debugging pre-game setup issues or verifying boat positions.
