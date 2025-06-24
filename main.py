# Imports
import random
import time
import keyboard
import sys
import os

# Constant global variables
GRID_SIZE = int(sys.argv[1])
WIDTH_BONUS_SIZE = int(sys.argv[2])

POINTS_TO_WIN = int(GRID_SIZE / 2)
PLAYER_CHARACTER = "•"
GRID_BACKGROUND = '‎'

# Function to clear the console on the start
def start_clear():
    os.system('cls')

# Function for clearing the console
def clear_console():
    print("\033[H", end="")

# Class that is used to create, refresh, print grid
class CreateGrid:
    def __init__(self):
        self.grid = []
        self.has_won = False

    # Function that is used to create/refresh grid
    def create_grid(self, grid_size):
        self.grid = []
        for x_cord, x in enumerate(range(0, grid_size+1)):
            self.grid.append([])
            for y in range(0, grid_size+1+WIDTH_BONUS_SIZE):
                self.grid[x_cord].append(GRID_BACKGROUND)

    # Function that is used to print grid in one print
    def print_grid(self, points):
        output = "|" + ("‾" * (GRID_SIZE + WIDTH_BONUS_SIZE+1)) + "|\n|"
        for x in self.grid:
            for y in x:
                output += y
            output += "|\n|"
        output += "_" * (GRID_SIZE + WIDTH_BONUS_SIZE + 1) + "|"
        if not self.has_won:
            print(output + f"\n{points}")
        else:
            print("YOU WON!")

# Class that is used to manage player movement
class MovementManager:
    def __init__(self, grid_size):
        self.player_position = [int(GRID_SIZE/2), int((GRID_SIZE+WIDTH_BONUS_SIZE)/2)]
        self.grid_size = grid_size

    def move_up(self):
        if self.player_position[0] > 0:
            self.player_position[0] -= 1

    def move_down(self):
        if self.player_position[0] < self.grid_size:
            self.player_position[0] += 1

    def move_left(self):
        if self.player_position[1] > 0:
            self.player_position[1] -= 1

    def move_right(self):
        if self.player_position[1] < self.grid_size + WIDTH_BONUS_SIZE:
            self.player_position[1] += 1

if __name__ == "__main__":
    # Preparing
    start_clear()
    grid_manager = CreateGrid()
    movement_manager = MovementManager(GRID_SIZE)

    # Stats Management
    player_points = 0

    # FPS Management
    FPS = 240
    frame_duration = 1 / FPS
    last_time = time.time()

    # Random trophy pos
    random_pos = [random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE + WIDTH_BONUS_SIZE)]
    while True:
        pointed = False
        # FPS Management
        current_time = time.time()
        elapsed = current_time - last_time
        if elapsed >= frame_duration:

            # Keyboard listening
            if keyboard.is_pressed('w'):
                movement_manager.move_up()
                time.sleep(0.3)

            elif keyboard.is_pressed('s'):
                movement_manager.move_down()
                time.sleep(0.3)

            elif keyboard.is_pressed('d'):
                movement_manager.move_right()
                time.sleep(0.3)

            elif keyboard.is_pressed('a'):
                movement_manager.move_left()
                time.sleep(0.3)

            elif keyboard.is_pressed('esc'):
                sys.exit()

            # Manage printing
            grid_manager.create_grid(GRID_SIZE)
            grid_manager.grid[movement_manager.player_position[0]][movement_manager.player_position[1]] = PLAYER_CHARACTER
            grid_manager.grid[random_pos[0]][random_pos[1]] = "X"

            # Got score
            if movement_manager.player_position[0] == random_pos[0] and movement_manager.player_position[1] == random_pos[1]:
                player_points += 1
                if player_points >= POINTS_TO_WIN:
                    grid_manager.has_won = True
                movement_manager.player_position = [int(GRID_SIZE/2), int((GRID_SIZE+WIDTH_BONUS_SIZE)/2)]
                GRID_SIZE -= 1
                grid_manager.create_grid(GRID_SIZE)
                pointed = True
                random_pos = [random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE + WIDTH_BONUS_SIZE)]

            # Refresh
            if pointed:
                start_clear()
                clear_console()
            else:
                clear_console()
            grid_manager.print_grid(f"POINTS: {player_points}")
            last_time = current_time