"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
playerX = True
playerO = False
## Dimensions ##
colSize = 3
rowSize = 3
board = [   [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]


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
    if playerX :
        return X
        playerX = False
        playerO = True
    else:
        return O
        playerO = False
        playerX = True

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
    currentPlayer = player(board)
    actionBoard = copy.deepcopy(board)
    if actionBoard[action] != EMPTY:
     actionBoard[action] = currentPlayer
     return actionBoard
    else:
       raise Exception("Please choose a move that is not taken!")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    
    raise NotImplementedError


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