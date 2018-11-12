#
# Tick Tack Toe
# ...just having fun
#

# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class PlayerNumberWrong(Error):
   """Raised when input value is LQ zeor or > 2"""
   pass

class Row_or_Col_NumberWrong(Error):
   """Raised when the input value LQ 0 or > 3"""
   pass

class CellAlreadyPlayed(Error):
   """Raised when the input is trying to fill an position that is played"""
   pass
class InvalidValueinMatrix(Error):
   """Raised when the stored value in matrix is not zero or 1"""
   pass
class GameOverNoWinner(Error):
   """Raised when matrix is full but no winner"""
   pass



class ticTacToe(object):
    def __init__(self):
    # no parameters allowed assume a 3x3 matrix, allowed cell values are None, 0, 1
    # 0 for player-1 and 1 for player-2
        self.matrix = []
        self.countOfNone = 9
        self.rows = 3
        self.columns = 3
        
        for i in range(0,9):
            self.matrix.append(None)
    
    def play(self, player=0, row=0, col=0):
        # check if correct argument
        if player <=0 or player > 2:
            raise PlayerNumberWrong
         
        # check if correct argument
        if row <= 0 or row > 3 or col <= 0 or col > 3:
            raise Row_or_Col_NumberWrong
        
        index = (row-1)*3 + (col-1)
        # check if correct move: can not be already played cell
        if (self.matrix[index] != None):
            raise CellAlreadyPlayed
            
        # all checked, play now!
        self.matrix[index] = player-1
        self.countOfNone -= 1
        
        # check if player-1 is a winner
        valueToCheck = player - 1
        
        # check for each row
        for r in range(0,9,3): 
            if (self.matrix[r] == None) or (self.matrix[r+1] == None) or (self.matrix[r+2] == None):
                continue
            if ((self.matrix[r] == self.matrix[r+1]) and (self.matrix[r]== self.matrix[r+2])):
                return (player)
                   
        # for each col
        for c in range(0,3,1): 
            if (self.matrix[c] == None) or (self.matrix[c+3] == None) or (self.matrix[c+6] == None):
                continue
            if ((self.matrix[c] == self.matrix[c+3]) and (self.matrix[c]== self.matrix[c+6])):
                return (player)

        # check for left to right diagonal going down
        if ((self.matrix[0] == self.matrix[4]) and (self.matrix[0]== self.matrix[8])):
            if (self.matrix[0] != None): # if all are none, there is no winner
                return (player)

        # check for right to left diagonal going down
        if (self.matrix[2] == self.matrix[4]) and (self.matrix[2] == self.matrix[6]):
            if (self.matrix[2] != None): # if all are none, there is no winner
                return (player)
        
        if self.countOfNone <= 0:
            raise GameOverNoWinner
        else:
            return(None)
    # --- 

    def print(self):
        print('Current positions:')
        for r in range(1, self.rows+1):
            print("Row: ", r, ' ', end='')
            for c in range(1, self.columns+1):
                val = self.matrix[(r-1) * self.columns + (c-1)]
                if val == None:
                    print(' .', ' ', end='')
                elif val == 0:
                    print(' O', ' ', end='')
                elif val == 1:
                    print(' X', ' ', end='')
                else:
                    raise
            print()
        print('---')
    # ---        
    

t1 = ticTacToe()
p1 = input("Player 1: name?")
p2 = input("Player 2: name?")
try:
    winner = None
    who = 1 # indicates whose turn is next
    while (winner == None):
        if who == 1:
            who = 2
            print(p1, end='')
            turn = input(': your turn (row#,column#):?')
        else:
            who = 1
            print(p2, end='')
            turn = input(': your turn (row#,column#):?')
        inList = turn.split(',')
        row = int(inList[0])
        col = int(inList[1]) 
        winner = t1.play(who, row, col)
        t1.print()
    else: #ends while
        if who == 1:
            print("Winner is:", p2)
        else:
            print("Winner is:", p1)
except CellAlreadyPlayed:
    print('CellAlreadyPlayed')
except Row_or_Col_NumberWrong:
    print('Row_or_Col_NumberWrong')
except PlayerNumberWrong:
    print('PlayerNumberWrong')
except InvalidValueinMatrix:
    print('InvalidValueinMatrix') 
except GameOverNoWinner:
    print('Game Over No Winner: Please Play Again') 

GameOverNoWinner
print ('winner:', winner, " who:", who)

# ---
