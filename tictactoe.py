"""
Tic Tac Toe Player
"""

import math
import copy

# which player starts firts with thier symbol 
playerX = True
PlayerO = False
X = "X"
O = "O"
EMPTY = None

# dimensions 
colSize = 3
rowSize = 3

# actions and board 
playerXactions = []
playerOactions = []
board = [   ["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "O", EMPTY]]


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    global playerX 
    global playerO 
    if playerX == True:
        playerX = False
        playerO = True
        return X

    else:
        playerO = False
        playerX = True
        return O


    raise Exception("unable to select player")


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()
    for i in range(rowSize):
        for j in range(colSize):
            if board[i][j] != EMPTY:
                continue
            else: 
                possibleActions.add((i,j))
    print("Empty spots on board: ")
    print(possibleActions)
    return possibleActions
  


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action
    currentPlayer = player(board)
    actionBoard = copy.deepcopy(board)
    if actionBoard[row][col] == EMPTY:
        actionBoard[row][col] = currentPlayer
        if currentPlayer == "X":
            playerXactions.append(action)
        else:
            playerOactions.append(action)
        print(actionBoard)
        return actionBoard
    
    else:
        raise Exception("Please choose a move that is not taken!")

def winner():
    """
    Returns the winner of the game, if there is one.
    """
    winCondition = [
        # rows
        {(0, 0), (0, 1), (0, 2)}, 
        {(1, 0), (1, 1), (1, 2)},  
        {(2, 0), (2, 1), (2, 2)},  
        
        # columns 
        {(0, 0), (1, 0), (2, 0)},  
        {(0, 1), (1, 1), (2, 1)},  
        {(0, 2), (1, 2), (2, 2)},  
        
        # diagonals
        {(0, 0), (1, 1), (2, 2)},  
        {(0, 2), (1, 1), (2, 0)}   
    ]
    for condition in winCondition:
        if condition.issubset(playerXactions):
            print("Player X won")
            return playerX
        elif condition.issubset(playerOactions):
            print("Player O won")
            return playerO
        else:
            print("No one Won")
            return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

actions(board)
result(board, (2,2))
print(playerXactions)
