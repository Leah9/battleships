Battleships

grid = {}

  1 2 3 4 5 6 7 8 9 10
A 1
B 11
C 21
D 31
E 41
F 51
G 51
H 71
I 81
J 91

Empty " - "
hit = " X "
miss = " ~ "
Ship = " # "

Ship Types
1. Carrier #####
2. Battleship ####
3. Cruiser ###
4. Submarine ###
5. Destroyer ##

Position random at start for both teams.
Computer random generate shot coordinates

pl_grid = players grid with their ships
cpu_grid = cpu player with their ships
the above grids only conain owner ships and enemy hits on them

pl_grid_shots
cpu_grid_shots = contais the shots and hits cpu have

input in the form of row, column

random ship position
random number so that the length of the ship will not wrap around
number  <= 10 and number 
