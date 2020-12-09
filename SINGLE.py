import random


class Solution(object):
    def __init__(self, board=[[]], click = [], numFlags = 0, endGame = False):
        self.board = board
        self.click = click
        self.numFlags = numFlags
        self.endGame = endGame

    def search_around(self, x, y):
        count = 0
        for i, j in dic:
            if 0 <= x + i <= n - 1 or 0 <= y + j <= m - 1:
                if self.board[[x + i][y + i]] == 'M':
                    count += 1
        return count

    def searching(self, x, y):
        if x < 0 or x > n - 1 or y < 0 or y > m - 1:  # 不要超边界
            return
        if self.board[x][y] != 'E':  # 如果不是空方快
            return
        count = self.search_around(x, y)
        if count != 0:
            self.board[x][y] = str(count)  # 如果是一个至少与一个地雷相邻的空方块E被挖出，修改为数字，表示相邻地雷的数量
            return
        else:
            self.board[x][y] = 'B'  # 如果是一个没有相邻地雷的空方块E被挖出，修改为B
            for i, j in dic:
                self.searching(x + i, y + j)  # Recursion

    def updateBoard(self, board, click):
        dic = [[-1, 0], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        n = len(board)
        m = len(board[0])
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
                self.searching(click[0], click[1])
                return board

    def set_board(self, r, c, n):
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

    def start_game(self):
        row = 16
        column = 16
        num_of_mines = 16
        self.numFlags = num_of_mines
        board = self.set_board(row, column, num_of_mines)
        return board

    def play(self):
        board = self.start_game()
        print(board)
        print('Now is your turn')
        print('---------------------')
        user_input_x = int(input('Input the x coordinate: '))
        user_input_y = int(input('Input the y coordinate: '))
        user_input_i = int(input('What do you want to do? (type 0 to place a flag; type 1 to dig): '))
        clicker = []
        clicker.append(user_input_x)
        clicker.append(user_input_y)
        clicker.append(user_input_i)
        board = self.updateBoard(board, clicker)
        if self.endGame == True:
            print("Game Over")
        print("Number of Flags You Have:", self.numFlags)
        print(board)


a = Solution()
a.play()