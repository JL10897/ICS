import random
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        '''
        [['E','E','E','E','E'],
        ['E','E','E','E','E'],
        ['E','E','E','E','E'],
        ['E','E','E','E','E']]
        '''
        dic=[[-1,0],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        def search_around(self,x,y):
          count=0
          for i,j in dic:
            if 0<=x+i<=n-1 or 0<=y+j<=m-1:
              if board[[x+i][y+i]]=='M':
                count+=1
          return count
        def searching(self,x,y):
          if x<0 or x>n-1 or y<0 or y>m-1: #不要超边界
            return
          if board[x][y]!='E':  #如果不是空方快
            return
          count=self.search_around(x,y)
          if count!=0:
            board[x][y]=str(count)  #如果是一个至少与一个地雷相邻的空方块E被挖出，修改为数字，表示相邻地雷的数量
            return
          else:
            board[x][y]='B'    #如果是一个没有相邻地雷的空方块E被挖出，修改为B
            for i,j in dic:
              self.searching(x+i,y+j)     #Recursion
        n=len(board)
        m=len(board[0])
        #click=[a,b]
        print(type(click[0]))
        print(type(click[1]))
        print(type(board))
        if board[click[0]][click[1]]=='M':
          board[click[0]][click[1]]='X'
          return board
        else:
          self.searching(click[0],click[1])
          return board
    def set_board(self,r,c,n):        
        board=[]
        for rr in range(r):
          board.append([])
        M_dic={}
        random_list_x = random.sample(range(0, c), n)
        random_list_y = random.sample(range(0, r), n) 
        for p in range(len(random_list_x)):
            M_dic[random_list_x[p]]=random_list_y[p]
        for rr in range(r):
            for cc in range(c):
                if rr in M_dic and M_dic[rr]==cc:
                    board[rr].append('M')
                else:
                    board[rr].append('E')
        return board
    def start_game(self):
      row=16
      column=16
      num_of_mines=4
      board=self.set_board(row,column,num_of_mines)
      return board
    def play(self):
      board=self.start_game()
      print(board)
      print('Now is your turn')
      print('---------------------')
      user_input_x=input('Input the x coordinate: ')
      user_input_y=input('Input the y coordinate: ')
      clicker=[]
      clicker.append(user_input_x)
      clicker.append(user_input_y)
      board=self.updateBoard(board,clicker)
      

a=Solution()
a.play()
            
          
          

