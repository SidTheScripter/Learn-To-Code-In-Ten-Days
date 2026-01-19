import os
import random
import time
import sys
from collections import deque
from enum import Enum

# Constants
GRID_WIDTH = 20
GRID_HEIGHT = 10

# Direction enum
class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class SnakeGame:
    def __init__(self):
        self.reset_game()
        self.last_time = time.time()
        self.move_delay = 0.15  # Seconds between moves
    
    def reset_game(self):
        """Initialize or reset the game state"""
        self.snake = deque([(GRID_WIDTH // 2, GRID_HEIGHT // 2)])
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False
    
    def spawn_food(self):
        """Generate food at a random location not occupied by snake"""
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake:
                return food
    
    def update(self):
        """Update game logic"""
        if self.game_over:
            return
        
        # Check if enough time has passed for the next move
        current_time = time.time()
        if current_time - self.last_time < self.move_delay:
            return
        
        self.last_time = current_time
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        # Check wall collision
        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.appendleft(new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def draw(self):
        """Draw game elements to terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Draw top border
        print("+" + "-" * (GRID_WIDTH * 2 - 1) + "+")
        
        # Draw grid
        for y in range(GRID_HEIGHT):
            print("|", end="")
            for x in range(GRID_WIDTH):
                if (x, y) == self.snake[0]:
                    print("O", end=" ")  # Head
                elif (x, y) in self.snake:
                    print("o", end=" ")  # Body
                elif (x, y) == self.food:
                    print("*", end=" ")  # Food
                else:
                    print(" ", end=" ")
            print("|")
        
        # Draw bottom border
        print("+" + "-" * (GRID_WIDTH * 2 - 1) + "+")
        
        # Draw score and instructions
        print(f"\nScore: {self.score}")
        print("Controls: W=Up, S=Down, A=Left, D=Right, Q=Quit")
        
        if self.game_over:
            print("\n*** GAME OVER! ***")
            print("Press 'R' to restart or 'Q' to quit")
    
    def get_input(self):
        """Input handling"""
        import select
        
        try:
            # Non-blocking input check
            if sys.stdin in select.select([sys.stdin], [], [], 0.01)[0]:
                key = sys.stdin.read(1).lower()
                if key == 'w' and self.direction != Direction.DOWN:
                    self.next_direction = Direction.UP
                elif key == 's' and self.direction != Direction.UP:
                    self.next_direction = Direction.DOWN
                elif key == 'a' and self.direction != Direction.RIGHT:
                    self.next_direction = Direction.LEFT
                elif key == 'd' and self.direction != Direction.LEFT:
                    self.next_direction = Direction.RIGHT
                elif key == 'q':
                    return False
                elif key == 'r' and self.game_over:
                    self.reset_game()
        except:
            pass
        
        return True
    
    def run(self):
        """Main game loop"""
        print("\n=== SNAKE GAME ===")
        print("Controls: W=Up, S=Down, A=Left, D=Right, Q=Quit\n")
        time.sleep(2)
        
        running = True
        while running:
            self.update()
            self.draw()
            running = self.get_input()
            time.sleep(0.05)
        
        print("\nThanks for playing!")


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
