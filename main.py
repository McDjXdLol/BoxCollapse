# Imports
import os
import random
import sys
import time

import keyboard

# Global variables
while True:
    GRID_SIZE = 0
    WIDTH_BONUS_SIZE = 0
    POINTS_TO_WIN = 1
    try:
        GRID_SIZE = int(input("Enter the grid size: "))
        WIDTH_BONUS_SIZE = int(input("Enter the bonus width: "))

        # Player data
        POINTS_TO_WIN = int(input("Enter the number of points required to win: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    if GRID_SIZE <= 0:
        print("Grid size must be greater than 0. Please try again.")
        continue

    if WIDTH_BONUS_SIZE < 0:
        print("Bonus width cannot be negative. Please enter a valid value.")
        continue

    if POINTS_TO_WIN <= 0:
        print("Points to win must be greater than 0. Try again.")
        continue
    break

GRID_BACKGROUND = '‎'
PLAYER_CHARACTER = "•"


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
    def create_grid(self):
        self.grid = []
        for x_cord, x in enumerate(range(GRID_SIZE + 1)):
            self.grid.append([])
            for y in range(GRID_SIZE + 1 + WIDTH_BONUS_SIZE):
                self.grid[x_cord].append(GRID_BACKGROUND)

    # Function that is used to print grid in one print
    def print_grid(self, points):
        output = "|" + ("‾" * (GRID_SIZE + WIDTH_BONUS_SIZE + 1)) + "|\n|"
        for x in self.grid:
            for y in x:
                output += y
            output += "|\n|"
        output += "_" * (GRID_SIZE + WIDTH_BONUS_SIZE + 1) + "|"
        if not self.has_won:
            print(output + f"\n{points}")
        else:
            start_clear()
            print("YOU WON!")
            time.sleep(3)
            sys.exit()


# Class that is used to manage player movement
class MovementManager:
    def __init__(self, grid_size):
        self.player_position = [1, 1]
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


def randomize_obstacles():
    randomized_obstacles = []
    for _ in range(10):
        random_x = random.randint(0, GRID_SIZE)
        random_y = random.randint(0, GRID_SIZE + WIDTH_BONUS_SIZE)
        if random_x == 1 and random_y == 1:
            continue
        randomized_obstacles.append([random_x, random_y])
    return randomized_obstacles


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

    # Adding obstacles
    obstacles = randomize_obstacles()

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

            # Getting actuall player position
            player_pos = [movement_manager.player_position[0], movement_manager.player_position[1]]

            # Manage printing
            grid_manager.create_grid()
            grid_manager.grid[player_pos[0]][player_pos[1]] = PLAYER_CHARACTER
            grid_manager.grid[random_pos[0]][random_pos[1]] = "X"

            # Printing obstacles
            for obstacle in obstacles:
                if obstacle[0] == random_pos[0] and obstacle[1] == random_pos[1]:
                    continue
                if obstacle[0] == player_pos[0] and obstacle[1] == player_pos[1]:
                    start_clear()
                    print("GAME OVER!")
                    time.sleep(3)
                    sys.exit()
                grid_manager.grid[obstacle[0]][obstacle[1]] = "#"

            # Got score
            if player_pos[0] == random_pos[0] and player_pos[1] == random_pos[1]:
                movement_manager.player_position = [1, 1]
                GRID_SIZE -= 1
                movement_manager.grid_size = GRID_SIZE
                obstacles = randomize_obstacles()
                player_points += 1
                if player_points >= POINTS_TO_WIN:
                    grid_manager.has_won = True
                    continue
                if GRID_SIZE <= 1:
                    grid_manager.has_won = True
                    continue
                grid_manager.create_grid()
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
