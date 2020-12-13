import copy
'''这个file用来加密每个需要发给用户的board,使得雷对于他们不直接可见'''
# Printing the Minesweeper Layout
def encrypted_board(lst):
    llst = copy.deepcopy(lst)
    string = ''
    for i in range(len(llst)):
        for j in range(len(llst[i])):
            if llst[i][j] == 'E':
                llst[i][j] = '|_|'
            elif llst[i][j] == 'M':
                llst[i][j] = '|_|'
            elif llst[i][j] == 'e':
                llst[i][j] = '|F|'
            elif llst[i][j] =='X':
                llst[i][j] = '|F|'
            elif llst[i][j] == 'm':
                llst[i][j] = '|X|'
            elif llst[i][j] == 'B':
                llst[i][j] = '|O|'
            else:
                llst[i][j] = '|'+ llst[i][j]+ '|'

    for n in llst:
        string_col = ''
        for m in n:
            string_col += m
        string += string_col + '\n'

    return string
