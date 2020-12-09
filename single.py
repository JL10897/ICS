import random

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

        def check(i, j):
            cnt = 0
            for x, y in direction:
                x, y = x + i, y + j
                if 0 <= x < self.m and 0 <= y < self.n and board[x][y] == 'M':
                    cnt += 1
            return cnt

        def dfs(i, j):
            cnt = check(i, j)
            if not cnt:
                board[i][j] = 'B'
                for x, y in direction:
                    x, y = x + i, y + j
                    if 0 <= x < self.m and 0 <= y < self.n and board[x][y] == 'E': dfs(x, y)
            else:
                board[i][j] = str(cnt)

        # click=[a,b]
        # 如果input标记而不是直接点击
        if click[2] == 0:
            self.numFlags -= 1
            if board[click[0]][click[1]] == 'M':
                board[click[0]][click[1]] = 'X'
            return board

        # 直接点击
        elif click[2] == 1:
            if board[click[0]][click[1]] == 'M':
                self.endGame = True
            else:
                dfs(click[0], click[1])
                return board

    def play(self):
        print(self.board)
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


row = 16
column = 16
num_of_mines = 16
Flags = num_of_mines
bo = set_board(row, column, num_of_mines)

a = Solution(bo, [], Flags)
a.play()