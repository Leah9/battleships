# BATTLESHIPS
print("BATTLESHIPS")
print("Please enter your name :")
#name = input()

grid_translate = {"A": 0, "B": 10, "C": 20, "D": 30, "E": 40, "F": 50, "G": 60, "H": 70, "I": 80, "J": 90}

ship_type = {1: "Carrier", 2:"Battleship", 3:"Cruiser", 4:"Submarine", 5: "Destroyer"}
ship_size = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer":2}
# Create a blank grid and return
def blank_grid():
    grid = {}
    i = 1
    while i in range(1,101):
        grid[i] = ("--")
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

def add_ship(grid, ship_type, location):
    ship_length = ship_size["Carrier"]
    for i in range(ship_length):
        grid[location + i] = "# "
    print(ship_length)

def grid_to_location(row, column):
    location = 0
    location = grid_translate[row] + int(column)
    print(location)
    return location
    

pl_grid = blank_grid()
pl_grid_shots = blank_grid()

row = input("Enter Row A to J :")
column = input("Enter Column 1 to 10:")
location = grid_to_location(row, column)
add_ship(pl_grid, "Carrier", 25)

print("Shots on enemy")
output(pl_grid_shots)

print("Player ships")
output(pl_grid)



exit()