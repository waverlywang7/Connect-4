
import random
def print2d(A):
    """print2d prints a 2D array, A,
       as rows and columns
       Argument: A, a 2D list of lists
       Result: None (no return value)
    """
    NR = len(A)
    NC = len(A[0])

    for r in range(NR):      # NR == numrows
        for c in range(NC):  # NC == numcols
            print(A[r][c], end = ' ')
        print()

    return None  # this is implied anyway,
                 # when no return statement is present

# some tests for print2d



# create a 2D array from a 1D string
def createA(NR, NC, s):
    """Returns a 2D array with
       NR rows (numrows) and
       NC cols (numcols)
       using the data from s: across the
       first row, then the second, etc.
       We'll only test it with enough data!
    """
    A = []
    for r in range(NR):
        newrow = []
        for c in range(NC):
            newrow += [s[0]] # add that char
            s = s[1:]        # get rid of that first char
        A += [newrow]
    return A

# a couple of tests for createA:
A = [['X', ' ', 'O'], ['O', 'X', 'O']]
newA = createA(2, 3, 'X OOXO')
assert newA == A


A = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
newA = createA(4, 2, 'XO XOOOX')
assert newA == A

def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True
class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # bottom of the board

        # and the numbers underneath here

        return s       # the board is complete, return it
    def addMove(self,col,ox):
        """takes two arguments: the first, col, represents the index of the 
            column to which the checker will be added. The second 
            argument, ox, will be a 1 character string representing
            the checker to add to the board. That is, ox, should either be 
            'X' or 'O'
        """
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != ' ': #check to see if there is blank space
                self.data[row-1][col] = ox
                return 
        self.data[H-1][col] = ox
    def clear(self):
        """clears board"""
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ' '
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'
    def allowsMove(self,col):
        """ this method should return True if the calling
            object (of type Board) does allow a move into column
            c. It returns False if column c is not legal column
            number for the calling object. IT also
            returns False if colmn c is full.        
            Thus, this method should check to be  sure that c
            is within the range from 0 to the last 
            column and make sure there is still room left in the colm
        """
        H = self.height
        W = self.width
        D = self.data
        if col >= W or col < 0:
            return False
        elif D[0][col] != ' ':
            return False
        else: 
            return True  
    def isFull(self): 
        """This method should return True if the calling object (of type Board) is completley full of checkers. It should
            return False otherwise.
        """
        D = self.data
        for row in range(self.height): #check rows
            for col in range(self.width):
                if D[row][col] != ' ':
                    return True
                else:
                    return False # check columns
    def delMove(self,c):
        """should remove the top checker from the
            column c. If the column is empty, then delMove should
            do nothign. 
        """
        H = self.height
        W = self.width
        D = self.data
        for row in range(0,H):
            if self.data[row][c] != ' ': #check to see if there is blank space
                self.data[row][c] = ' '
                return 
    def winsFor(self,ox):
        """This method's argument ox is a 1 character checker: either
            'X' or 'O'. It should return True if there
            are four checkers of type ox in a row on the board. 
            It should return False otherwise.
        """
        H = self.height
        W = self.width
        D = self.data
        for row in range(0, H):
            for col in range(0, W - 3): #checks for horizontal wins
                 if D[row][col] == ox and \
                   D[row][col + 1] == ox and \
                   D[row][col + 2] == ox and \
                   D[row][col + 3] == ox:
                    return True
        for row in range(0,H-3): #for vertical wins
            for col in range(0,W):
                if D[row][col] == ox and \
                    D[row + 1][col] == ox and \
                    D[row + 2][col] == ox and  \
                    D[row + 3][col] == ox:
                    return True
        for row in range(0, H-3): # for southeast
            for col in range(0,W-3):
                if D[row][col] == ox and \
                    D[row+1][col+1] == ox and \
                    D[row+2][col+2] == ox and \
                    D[row+3][col+3] == ox:
                    return True
        for row in range(3,H):
            for col in range(0,W-3): #check northeast
                if  D[row][col] == ox and \
                    D[row-1][col+1] == ox and \
                    D[row-2][col+2] == ox and \
                    D[row-3][col+3] == ox:
                    return True
        return False
    def hostGame(self):
        """This method should print the board before prompting for each move.

            You will probably want to use a large while loop to structure the game. You should have 'X' go first and 'O' go second. My suggestion would be to put both 'X's and 'O's turn into the body of the while loop. Thus, one iteration of the while loop will make two Connect-Four turns.
        """

        print("Welcome to Connect Four!") 
        print(self)
        users_col = int(input("X's Choice: "))
        #while not self.winsFor(ox):
        while True: #since you break to escpae
            while not self.allowsMove(users_col):
                users_col = int(input("Choose a column: "))
            self.addMove(users_col, "X")
            if self.winsFor("X") == True:
                print(self)
                print("X wins! Congratulations!")
                break
            if self.isFull == True and self.winsFor("X") == False and self.winsFor("O") == False:
                print(self) 
                print("Tie")
                break
            #else: 
            print(self)
            #print("O's Choice:" , users_col)
            users_col = int(self.aiMove('O'))
            print("Computer turn")
            while not self.allowsMove(users_col):
                users_col = random.choice((range(7)))
            self.addMove(users_col,"O")
            if self.winsFor("O") == True:
                print(self)
                print("O wins! Congratulations. I'm sorry human")
                break
            if self.isFull == True and self.winsFor("O") == False and self.winsFor("X")== False:
                print(self) 
                print("Tie")
                break
            #else:
            print(self)
            users_col = int(input(("X's Choice: ")))                       
    def colsToWin(self,ox): 
        """returns a list of columns at which ox
        would win on the next move,
        """
        L = []
        W = self.width
        for col in range(0, W):
            if self.allowsMove(col) == True:
                self.addMove(col, ox)
                if self.winsFor(ox) == True:
                    L += [col]
                self.delMove(col)
                #if self.winsFor(ox) == False:
                    #self.delMove(col)
        return L
    def aiMove(self,ox):
        """ When the ox checker does have a win—or, lacking that, a move to block a win—it should take it.
        However, when the AI does not have a win nor a move to block a win, you'll choose your own design as to how it plays, e.g., strategically (move to the center?),
         randomly, or some other approach...
        """
                           # if there is a way for ox to win then, aiMove MUST return that move(That column number. any winnign column moves may be returned)
        if self.colsToWin(ox) != []:
            return random.choice(self.colsToWin(ox)) #[0] #just choose first win in list of wins
        elif self.colsToWin(ox) == []:
            if ox == 'X': #if the list is empty
                self.colsToWin('O') #look at opponent
                if self.colsToWin('O') != []: #is there wins?
                    return random.choice(self.colsToWin('O')) #then choose a random choice out wins
                else: 
                            #is self.width odd
                    middle = int((self.width/2) - .5)
                    if self.allowsMove(middle) == True:
                        return middle # no way to block or win. go to center
                    else: 
                        return random.choice(range(7))
            elif ox == 'O': #if you are O
                self.colsToWin('X') #if there is a way to win if opponent
                if self.colsToWin('X') != []:
                    return random.choice(range(7)) # return random choice of wins
                else:
                    middle = int((self.width/2) - .5)
                    if self.allowsMove(middle) == True:
                        return middle
                    else:
                        return random.choice(range(7))
            


        
        
            
                                     #if there is NO way for ox to win, but there is a way to BLOCK the opponents four in a row, then
        #aiMove must return a move that blocks its opponent's four in a row. Choose one way to block

        #if there is NO way for ox to win NOR a way for ox to block teh opponent from winnign. then aiMove should
        #return a move of your programmer's choice. 

        #preferring the center. 
        