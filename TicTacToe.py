from os import name
import numpy, random, discord
from discord.ext import commands

class Player:
    name = ""
    symbol = ''

    def __init__(self,name="NO NAME", symbol='?'):
        self.name = name
        self.symbol = symbol

    def getSymbol(self):
        return self.symbol

    def getName(self):
        return self.name

grid_x = 10
grid_y = 10

matrix = [[' ' for i in range(grid_x)] for j in range(grid_y)] # initialise matrix with space symbol of size x by y


player_name_1 = "Player 1"
player_name_2 = "Player 2"
player_symbol_1 = 'O'
player_symbol_2 = 'X'

player1 = Player("player 1", 'O')
player2 = Player("player 2", 'X')
players = [player1, player2]
current_player = player1

running = True

#while running: #gameloop
#    print("gameloop")

def update(): # Update the UI

    fields = []

    for i in range(grid_y):
        for j in range(grid_x):
            #print(f"\t{matrix[i-1][j-1]}\t", end="", flush=True)
            fields.append(matrix[i-1][j-1])
        #print("\n")

    print(f"""
    ##########################################################################################
    ——————————————————————————————————————————————————————————————————————————————————————————
    Player {current_player.name}'s turn
    ——————————————————————————————————————————————————————————————————————————————————————————
    ***Select a field to place the {current_player.symbol} mark using the ".play" command.***
    ——————————————————————————————————————————————————————————————————————————————————————————
    {drawGrid(fields)}
    ——————————————————————————————————————————————————————————————————————————————————————————
    ***Command usage is: play <x_coordinate>,<y_coordinate>***
    ——————————————————————————————————————————————————————————————————————————————————————————
    ##########################################################################################
    """)

def drawGrid(fields): # Draw the entire current grid

    grid="\t"

    for i in range(grid_x*4+1):
        grid = grid + '—'
    grid = grid + "\n\t| "

    row = 1

    for c,i in enumerate(fields):

        grid = grid + i + " | "

        if(row <= grid_y):
            if(c+1 == (row * grid_x) and c+1 < (grid_x * grid_y)):
                grid = grid + "\n\t"
                for i in range(grid_x*4+1):
                    grid = grid + '—'
                grid = grid + "\n\t| "
                row+=1
            elif(c+1 == (grid_x * grid_y)):
                grid = grid + "\n\t"
                for i in range(grid_x*4+1):
                    grid = grid + '—'

    return grid

def switchPlayer(current_player, players):
    if(current_player == players[0]):
        current_player = players[1]
    else:
        current_player = players[0]

def moveCoordPrompt(current_player):
    x_coord = int(input(f"What is your next move {current_player.name}? \n\n Enter x coordinate (maximum is {grid_x}): "))
    if(x_coord <= grid_x):
        y_coord = int(input(f"\nEnter y coordinate (maximum is {grid_y}): "))
        if(y_coord <= grid_y):
            pass
        else:
            print(f"ERROR: Invalid move. The grid is only {grid_y} fields high")
    else:
        print(f"ERROR: Invalid move. The grid is only {grid_x} fields wide")
    return [x_coord, y_coord]

def move(matrix, coord, symbol, players, current_player):
    if(matrix[coord[1]-2][coord[0]-2]== ' '):
        matrix[coord[1]-2][coord[0]-2] = symbol
    else:
        print("ERROR: Invalid move. This field is already taken")
    switchPlayer(current_player, players)

def checkConditions(matrix, current_player):

    print("0,0: ",matrix[0][0])
    print("0,1: ",matrix[0][1])
    print("0,2: ",matrix[0][2])
    print("symbol: ", current_player.getSymbol())

    if((matrix[0][0] == current_player.getSymbol() and matrix[0][1] == current_player.getSymbol()) and matrix[0][2] == current_player.getSymbol()):
        print(f"{current_player.getName()} has won the game!")
        while True:
            pass


while running: # test gameloop
    update()
    move(matrix, moveCoordPrompt(current_player), current_player.symbol, players, current_player)
    checkConditions(matrix, current_player)

def setup(bot):
    bot.add_command(_)