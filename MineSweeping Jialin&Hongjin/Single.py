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
    def __init__(self, board, numFlags, click,endGame = False):
        self.board = board
        self.click = click
        self.numFlags = numFlags
        self.endGame = endGame

        # changing the states of positions without mines
    def dfs(self,i, j):
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
        self.m, self.n = len(self.board), len(self.board[0])  
        
        cnt = 0
        for x, y in direction:
            x, y = x + i, y + j
            if 0 <= x < self.m and 0 <= y < self.n and self.board[x][y] == 'M':
                cnt += 1
                

        if cnt == 0:
            self.board[i][j] = 'B'
            for x, y in direction:
                x, y = x + i, y + j
                if 0 <= x < self.m and 0 <= y < self.n and  self.board[x][y] == 'E':
                    self.dfs(x, y)
        else:
            self.board[i][j] = str(cnt)

    def updateBoard(self):
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
                self.endGame = True
                return encrypted_board(self.board)

            else:
                # change states for positions without mines
                self.dfs(self.click[0], self.click[1])
                return self.board

    def set_click(self,new_click):
        self.click=new_click
    def get_flag(self):
        return self.numFlags
    def get_board(self):
        return self.board
    def get_game_status(self):
        return self.endGame

"""    def play(self):
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
        self.board = self.updateBoard()
        print("Number of Flags You Have:", self.numFlags)
        if self.endGame == True:
            print("Game Over")
        else:
            self.play()

# original settings (Will be commented out in online mode)
row = 16
column = 16
num_of_mines = 16
Flags = num_of_mines
bo = set_board(row, column, num_of_mines)



a = Solution(bo, Flags,[])
a.play()"""