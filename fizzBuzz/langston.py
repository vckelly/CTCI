#Langston's Ant

from random import *

#return a Size X Size 2D array 
#this array will serve as the board for the main program
def _buildBoard(size):
    return [['.' for i in range(size)] for y in range(size)]

def _printBoard(board):
    for list in board:
        print(list)

    print('\n\n')
        

#randomly place ant on board
def _placeAnt(board, size):

    x = randint(0, size-1)
    y = randint(0, size-1)

    board[x][y] = "X"

    return board, (x, y)

#returns the direction the ant should move in following 
#landing on a new square
def _turnAnt(direction, nextTurn):
    
    turns = {
        'N' : {
            'L': 'W',
            'R': 'E'
        },
        'E' : {
            'L': 'N',
            'R': 'S'
        },
        'S' : {
            'L': 'E',
            'R': 'W'
        },
        'W' : {
            'L': 'S',
            'R': 'N'
        }
    }
    return turns.get(direction).get(nextTurn)

#returns a bool based on whether the ant will collide 
#with the edge of the board on the next turn
#position is a tuple containing the x, y coordinates of the ant
def _detectCollision(position, direction, size):
    if direction == 'N':
        if position[1] == 0: 
            return True 
    elif direction == 'E':
        if position[0] == size - 1:
            return True
    elif direction == 'S':
        if position[1] == size - 1:
            return True
    elif direction == 'W':
        if position[0] == 0:
            return True
    
    return False

def _changeTileColor(position, board):
    newTile = 'X' if board[position[1]][position[0]] == '.' else '.'
    board[position[1]][position[0]] = newTile
    return board

# #moves the ant to the next tile based on the direction arg
# def _moveAnt(board, position, direction):
#     if _detectCollision(position, direction, len(board)):
#         if position[0] == 0 or position[0] == len(board) - 1:
#             if position[0] == 0: 
#                 position[0] = len(board) - 1
#             else: 
#                 position[0] = 0
#         else:
#             if position[1] == 0: 
#                 position[1] = len(board) - 1
#             else: 
#                 position[1] = 0
#     else: 

    
    


#def langston():



if __name__== "__main__":
    #langston()
    board = _buildBoard(10)
    # _printBoard(board)
    # print()
    board , pos = _placeAnt(board, len(board))
    _printBoard(board)
    # print(_detectCollision(pos, 'S', 10))

    _changeTileColor(pos, board)
    _printBoard(board)