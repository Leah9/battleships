import random
from os import system, name
# BATTLESHIPS
print("BATTLESHIPS")
#print("Please enter your name :")

player_name = input("Plese enter your name :")
testing = 0
cpu_last_shot = ["No shots taken"]
player_last_shot = ["No shots taken"]
grid_translate = {"A": 0, "B": 10, "C": 20, "D": 30, "E": 40, "F": 50, "G": 60, "H": 70, "I": 80, "J": 90}
ship_type = {1: "Carrier", 2:"Battleship", 3:"Cruiser", 4:"Submarine", 5: "Destroyer"}
ship_size = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer":2}
player_lives = 1
cpu_lives = 1

# Create a blank grid and return
def blank_grid():
    grid = {}
    i = 1
    while i in range(1,101):
        grid[i] = ("- ")
        i += 1
    return(grid)

### Print to screen the named grid
def output(grid):
    string = "  1 2 3 4 5 6 7 8 9 10\nA "
    i = 0
    for i in grid:
        string += grid[i]
        if i % 10 == 0:
            string += "\n"
            if i == 0: string += "A"
            elif i == 10: string += "B "
            elif i == 20: string += "C "
            elif i == 30: string += "D "
            elif i == 40: string += "E "
            elif i == 50: string += "F "
            elif i == 60: string += "G "
            elif i == 70: string += "H "
            elif i == 80: string += "I "
            elif i == 90: string += "J "
    print(string)

# Ads a ship to the grid as per parameters
def add_ship(grid, ship, location): 
    ship_length = ship_size[ship] #ship_size["Carrier"]
    for i in range(ship_length):
        grid[location + i] = "# "

# Translates user input to grid location number
def grid_to_location(row, column):
    location = 0
    location = grid_translate[row] + int(column)
    #print(location)
    return location

# Generates a random position for ship taking into account its
# length
def random_position_select(length, grid):
    num1 = random.randrange(0, 9)
    num2 = random.randrange(1, 10 - length + 2)
    num = num1 * 10 + num2
    #print("Num 1 = ", num1,"Num 2 = ", num2)
    #print(num)
    #print("Num 2 ", num2)
    # Check it does not overlap another ship
    for i in range(length):
        #print(i)
        if grid[num + i] == "# ":
            num = -1
            #print("CRASH" , num)
            return num
    return num

def player_input():
    while True:
        row = input("Enter Row A to J or X to quit:")
        row = row.upper()
        if row == "X":
            exit()
        if row in grid_translate:
            print("You selected row: ", row)
        else:
            continue
        column = input("Enter Column 1 to 10:")
        column = int(column)
        if column <= 0 or column >= 11:
            print("Column out of range")
            continue
        #print(row, column)
        return grid_to_location(row, column)
        break

def count_lives(grid):
    count = 0
    for i in grid:
        if grid[i] == "# ":
            count += 1
    #print(count)
    return count

def check_shot(grid, shot):
    if grid[shot] == "# ":
        if grid == cpu_grid:
            cpu_grid[shot] = "X "
            pl_grid_shots[shot] = "X "
            player_last_shot[0] = "Player hit an enemy ship"
        if grid == pl_grid:
            pl_grid[shot] = "X "
            cpu_grid_shots[shot] = "X "
            cpu_last_shot[0] = "CPU hit one of your ships"

    elif grid[shot] == "- ":
        if grid == cpu_grid:
            cpu_grid[shot] = "~ "
            pl_grid_shots[shot] = "~ "
            player_last_shot[0] = "Player missed"
        if grid == pl_grid:
            pl_grid[shot] = "~ "
            cpu_grid_shots[shot] = "~ "
            cpu_last_shot[0] = "CPU missed"

def cpu_take_shot():
    num = random.randrange(1, 100)
    check_shot(pl_grid, num)

def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Initialises blank grids
pl_grid = blank_grid()
pl_grid_shots = blank_grid()
cpu_grid = blank_grid()
cpu_grid_shots = blank_grid()

# Generate player ships placement
for i in ship_size:
    pos = 0
    #print("Ship Size" , ship_size[i])
    #print(i)
    while pos <= 0:
        pos = random_position_select(ship_size[i], pl_grid)
    add_ship(pl_grid, i, pos)

for i in ship_size:
    pos = 0
    #print("Ship Size" , ship_size[i])
    #print(i)
    while pos <= 0:
        pos = random_position_select(ship_size[i], cpu_grid)
    add_ship(cpu_grid, i, pos)

# MAIN LOOP
while player_lives >= 1 and cpu_lives >= 1:
    if testing == 1: # Shows CPU ship positions and shots for testing
        print("Shots by CPU")
        output(cpu_grid_shots)
        print("CPU ships")
        output(cpu_grid)
    #Main display output
    print("Shots on enemy")
    output(pl_grid_shots)
    print("Player ships")
    output(pl_grid)
    print(cpu_last_shot[0])
    print(player_last_shot[0])
    #Player takes a shot
    shot = player_input()
    check_shot(cpu_grid, shot)
    print(shot)
    cpu_take_shot() #CPU takes shot
    player_lives = count_lives(pl_grid)
    cpu_lives = count_lives(cpu_grid)

    clear_screen()

if player_lives == 0:
    print("CPU wins !!! better luck next time ", player_name)
else:
    print("Well done ", player_name, "you won !")

exit()