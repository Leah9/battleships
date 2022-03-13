# BATTLESHIPS
print("BATTLESHIPS")
print("Please enter your name :")
#name = input()

def blank_grid():
    grid = {}
    i = 1
    while i in range(1,101):
        grid[i] = ("--")
        #print(i)
        i += 1
    return(grid)
  #i += 1

def output(grid):
    string = ""
    #print("here")
    i = 0
    for i in grid:
        #print(i, "here")
        string += grid[i]
        #print(i)
        if i % 10 == 0:
            string += "\n"
    print(string)

grid = blank_grid()

#print(grid)

output(grid)

exit()