# Attack System & Verification Branch — README

This branch is dedicated exclusively to the implementation of the **attack system** and all related **validations performed on the grids**.  
Its purpose is to isolate the shooting logic so it can be reviewed, tested, and improved without interference from other gameplay features.

---

## Purpose of This Branch

- Implement the attack mechanic used to target cells on the enemy grid.  
- Add all necessary verifications to ensure valid and consistent shots.  
- Manage the marking of hits and misses on the appropriate grids.  
- Provide a clean, isolated environment to test the attack logic.  
- Prepare a stable foundation for integrating the combat system into the main project.

---

## Features Included

### 1. Attack Input Handling
- Reading and processing coordinates entered by the player.  
- Ensuring the format of the input is valid (e.g., `A1`, `C7`, `J10`).  
- Verifying that the coordinate exists on the grid.

### 2. Verification Rules
- Checking that the selected cell has not already been targeted.  
- Ensuring the column number is between 1 and 10.  
- Ensuring the row letter is between A and J.  
- Rejecting malformed or incomplete input.

### 3. Attack Outcome Logic
- Determining whether the shot is a **hit** or a **miss** based on the enemy grid.  
- Marking:
  - `X` on the attack grid for a hit  
  - `O` on the attack grid for a miss  
- Updating the enemy grid by marking hit boat cells.  
- Providing feedback to the player (hit / miss).

### 4. Grid Management
- Ensuring the correct grids are updated (attacker shot grid & enemy boat grid).  
- Preventing invalid writes or overwriting protected data.  
- Maintaining consistent game state after each attack.

---

## Intended Audience

This branch is designed for:

- Developers working specifically on combat mechanics.  
- Contributors reviewing or testing the attack validation rules.  
- New team members who need to understand how shooting actions are processed.  
- Developers preparing to extend the system (AI attacks, special shots, UI interactions).

---

## How to Use This Branch

- Review the commented code to follow the complete attack workflow.  
- Test shot inputs to validate the behavior of the verification rules.  
- Use this branch before integrating more advanced combat features.  
- Refer back to it when debugging issues related to coordinates, hits, or shot validation.

