# BATTLESHIPS
### Battleships in python terminal
===

First playable version allows a player to play against the CPU. The CPU player is not very good at all and most players should be able to win.

Each player has 5 ships randomly placed in the play area.

* Carrier       # # # # #
* Battleship    # # # #
* Cruiser       # # #
* Submarine     # # #
* Destroyer     # #

"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer":2}

The player goes first and enters coordinates A to J then 1 to 10. If the player hits an enemy ship the player shots grid changes to X, if it is a miss it changes to ~.

The CPU player then takes a shot at your ships, as each section is hit it will change from # to X.

