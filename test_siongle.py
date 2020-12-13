import random
from translate_board import encrypted_board

# set up the board, randomly placing the mines
def set_board(r, c, n):
    board = []
    for rr in range(r):
        board.append([])
    M_dic = {}
    random_list_x = random.sample(range(0, c), n)
    random_list_y = random.sample(range(0, r), n)
    for p in range(len(random_list_x)):
        M_dic[random_list_x[p]] = random_list_y[p]
    for rr in range(r):
        for cc in range(c):
            if rr in M_dic and M_dic[rr] == cc:
                board[rr].append('M')
            else:
                board[rr].append('E')
    return board

class Solution:
    def __init__(self, board, click, numFlags, endGame = False):
        self.board = board
        self.click = click
        self.numFlags = numFlags
        self.endGame = endGame

    def updateBoard(self, board, click):
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
        self.m, self.n = len(board), len(board[0])

        # count the mines around certain position
        def check(i, j):
            cnt = 0
            for x, y in direction:
                x, y = x + i, y + j
                if 0 <= x < self.m and 0 <= y < self.n and self.board[x][y] == 'M':
                    cnt += 1
            return cnt

        # changing the states of posisitions without mines
        def dfs(i, j):
            cnt = check(i, j)
            if not cnt:
                self.board[i][j] = 'B'
                for x, y in direction:
                    x, y = x + i, y + j
                    if 0 <= x < self.m and 0 <= y < self.n and self.board[x][y] == 'E': dfs(x, y)
            else:
                self.board[i][j] = str(cnt)
                
        # placing a flag
        if self.click[2] == 0:
            self.numFlags -= 1
            # if there is a mine, state changes to 'X'
            if self.board[self.click[0]][self.click[1]] == 'M':
                self.board[self.click[0]][self.click[1]] = 'X'
            elif self.board[self.click[0]][self.click[1]] == 'E':
                self.board[self.click[0]][self.click[1]]= 'e'
            return self.board
            # if there is not a mine, state doesn't change, but number of flags remaining declines

        # digging
        elif self.click[2] == 1:
            # if there is a mine, game over
            if self.board[self.click[0]][self.click[1]] == 'M':
                self.board[self.click[0]][self.click[1]] = 'm'
                print(encrypted_board(self.board))
                self.endGame = True

            else:
                # change states for positions without mines
                dfs(self.click[0], self.click[1])
                return self.board

    def play(self):
        print(encrypted_board(self.board))
        print('Now is your turn')
        print('---------------------')
        user_input_x = int(input('Input the x coordinate: '))
        user_input_y = int(input('Input the y coordinate: '))
        user_input_i = int(input('What do you want to do? (type 0 to place a flag; type 1 to dig): '))
        clicker = []
        clicker.append(user_input_x)
        clicker.append(user_input_y)
        clicker.append(user_input_i)
        self.click = clicker
        board = self.updateBoard(self.board, clicker)
        print("Number of Flags You Have:", self.numFlags)
        print(board)
        if self.endGame == True:
            print("Game Over")
        else:
            self.play()

# original settings
row = 16
column = 16
num_of_mines = 16
Flags = num_of_mines
bo = set_board(row, column, num_of_mines)



a = Solution(bo, [], Flags)
a.play()