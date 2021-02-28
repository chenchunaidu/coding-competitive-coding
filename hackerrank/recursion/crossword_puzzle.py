def  fill_crossword_puzzle(board,words,row,col):
    pass

board = []
for i in range(10):
    line = input()
    board.append(list(line))
words = input().split(";")

fill_crossword_puzzle(board,words,0,0)