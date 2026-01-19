# Snake Game Code Explanation

This is a terminal-based implementation of the classic Snake game written in Python. The game runs directly in your command line interface.

## Overview

The player controls a snake that moves around a grid, eating food to grow longer. The game ends if the snake hits a wall or collides with itself.

## Key Components

### Constants and Configuration

```python
GRID_WIDTH = 20
GRID_HEIGHT = 10
```

These define the playing field dimensions: 20 cells wide by 10 cells tall.

### Direction System

The `Direction` enum defines the four possible movement directions. Each direction is represented as a tuple of (x_change, y_change):

- UP: (0, -1) - no horizontal change, move up one cell
- DOWN: (0, 1) - no horizontal change, move down one cell  
- LEFT: (-1, 0) - move left one cell, no vertical change
- RIGHT: (1, 0) - move right one cell, no vertical change

## The SnakeGame Class

### Initialization (`__init__`)

Sets up the initial game state and timing variables. The `move_delay` of 0.15 seconds controls how fast the snake moves.

### Game State (`reset_game`)

Initializes or resets all game variables:

- **snake**: A deque (double-ended queue) storing the coordinates of each snake segment, starting with one segment at the center
- **direction**: The current movement direction
- **next_direction**: Queued direction change (prevents illegal 180-degree turns)
- **food**: Random coordinates for the food item
- **score**: Player's current score
- **game_over**: Boolean flag for game state

### Food Generation (`spawn_food`)

Generates random coordinates for food placement, ensuring it doesn't spawn on top of the snake. It keeps trying random locations until it finds an empty spot.

### Game Logic (`update`)

This is the core game loop that runs every frame:

1. **Timing Check**: Only updates when enough time has passed (based on `move_delay`)
2. **Direction Update**: Applies the queued direction change
3. **Movement**: Calculates the new head position by adding the direction vector to the current head
4. **Wall Collision**: Checks if the new head is outside the grid boundaries
5. **Self Collision**: Checks if the new head overlaps with any existing snake segment
6. **Growth**: Adds the new head to the front of the snake
7. **Food Check**: If food is eaten, increases score and spawns new food; otherwise removes the tail segment

### Display (`draw`)

Renders the game state to the terminal:

- Clears the screen
- Draws a bordered grid
- Displays the snake head as "O", body segments as "o", and food as "*"
- Shows the current score and controls
- Displays game over message when applicable

### Input Handling (`get_input`)

Uses non-blocking input to read keyboard commands without pausing the game:

- **WASD keys**: Control snake direction (with validation to prevent 180-degree turns)
- **Q**: Quit the game
- **R**: Restart after game over

The direction validation prevents the snake from reversing into itself (e.g., can't go LEFT if currently moving RIGHT).

### Main Loop (`run`)

The primary game execution loop:

1. Displays initial instructions
2. Continuously updates game state
3. Redraws the screen
4. Processes input
5. Sleeps briefly between iterations to control frame rate

## How It Works

The snake is represented as a deque of coordinate tuples. When the snake moves:

1. A new head segment is added at the front in the direction of movement
2. If no food was eaten, the tail segment is removed (snake maintains length)
3. If food was eaten, the tail remains (snake grows by one segment)

This efficient approach means the snake only needs to modify the front and back of the deque, which are O(1) operations.

## Game Mechanics

- **Starting**: Snake begins with one segment at the center, moving right
- **Movement**: Automatic continuous movement with directional control
- **Scoring**: +10 points per food item consumed
- **Losing**: Game ends on wall collision or self-collision
- **Speed**: Fixed at 0.15 seconds per move (can be adjusted via `move_delay`)

## Technical Notes

The game uses terminal control codes to clear the screen and relies on the `select` module for non-blocking input on Unix-like systems. This allows the game to continuously update while checking for user input without blocking execution.