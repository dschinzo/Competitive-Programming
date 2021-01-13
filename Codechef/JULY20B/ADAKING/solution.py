class Board:
    def __init__(self):
        self.board = [(['.']*8).copy() for i in range(8)]
        self.board[0][0] = 'O'
    
    def obstacle(self, k):
        poss = 64 - k
        i, j = 7, 7
        while poss > 0:
            self.board[i][j] = 'X'
            if j > 0:
                j -= 1
            elif i > 0:
                i -= 1
                j = 7
            else:
                break
            poss -= 1
                
    def printBoard(self):
        for i in range(8):
            print("".join(self.board[i]))
        print("\n")
    
for t in range(int(input())):
    k = int(input())
    chess = Board()
    chess.obstacle(k)
    chess.printBoard()
