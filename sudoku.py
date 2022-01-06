#!/usr/bin/env python3
# sudoku solver in python

info_text = '''
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗ 
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝ 
                                                                                    
███████╗██╗   ██╗██████╗  ██████╗ ██╗  ██╗██╗   ██╗    ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗     ██╗   ██╗ ██████╗    ██╗
██╔════╝██║   ██║██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║    ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗    ██║   ██║██╔═████╗  ███║
███████╗██║   ██║██║  ██║██║   ██║█████╔╝ ██║   ██║    ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝    ██║   ██║██║██╔██║  ╚██║
╚════██║██║   ██║██║  ██║██║   ██║██╔═██╗ ██║   ██║    ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗    ╚██╗ ██╔╝████╔╝██║   ██║
███████║╚██████╔╝██████╔╝╚██████╔╝██║  ██╗╚██████╔╝    ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║     ╚████╔╝ ╚██████╔╝██╗██║
╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝      ╚═══╝   ╚═════╝ ╚═╝╚═╝
                                                                                                                                    
██████╗ ██╗   ██╗    ███████╗██╗██╗  ██╗ █████╗ ██╗    ██╗     ██╗   ██╗██╗
██╔══██╗╚██╗ ██╔╝    ██╔════╝██║██║ ██╔╝██╔══██╗██║    ██║     ██║   ██║██║
██████╔╝ ╚████╔╝     ███████╗██║█████╔╝ ███████║██║    ██║     ██║   ██║██║
██╔══██╗  ╚██╔╝      ╚════██║██║██╔═██╗ ██╔══██║██║    ██║     ██║   ██║╚═╝
██████╔╝   ██║       ███████║██║██║  ██╗██║  ██║██║    ███████╗╚██████╔╝██╗
╚═════╝    ╚═╝       ╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝    ╚══════╝ ╚═════╝ ╚═╝
                                                                           
'''

import sys

# load .sudoku file
def load_board_from_disk(file_path):
	lines = [] # all the lines in the file
	with open(file_path, "r") as file:
		lines = file.readlines() # read all the lines to "lines"
	
	board = [] # board
	for line in lines:
		l = [] # current line in integer format
		for char in line:
			if (char != " " and char != "\n"):
				l.append(int(char)) # append all the integers
		board.append(l) # append the integer line to the board
	
	return board # return
				
def draw_board(board):
	if board == None:
		print("board is empty!")
		return
	print("+-------------------+")
	for box in board:
		print("|", end=" ") # start box
		for cell in box:
			print(cell, end=" ")
		print("|") # print new line and end box
	print("+-------------------+")

# check if a number is possible to put in a certain position
def possible(b, y, x, n):
	for i in range(0, 9):
		if b[y][i] == n: # check horizontal
			return False
		if b[i][x] == n: # check vertical
			return False
	
	# check position based in a box
	x0 = (x//3) * 3
	y0 = (y//3) * 3

	# check box
	for i in range(0, 3):
		for j in range(0, 3):
			if b[y0+i][x0+j] == n:
				return False
	
	return True

# solve the problem
def solve(board):
	for y in range(0, 9): # loop rows
		for x in range(0, 9): # loop columns
			if board[y][x] == 0: # check if the cell is empty
				for n in range(1, 10): # try all the possible number
					if possible(board, y, x, n):
						board[y][x] = n
						solve(board) # solve again
						board[y][x] = 0 # if all not, keep it empty for now
				return # finish
	# draw the solved board
	print("solved:")
	draw_board(board)
	input("ENTER TO EXIT")

# main
def main():
	# command line args
	if len(sys.argv) != 2:
		print("Only one argument is allowed!")
		return
	if (sys.argv[1] == "-info"):
		print(info_text)
		return
	
	# logo
	print()
	print("################################################")
	print("## Welcome to sudoku solver v0.1 by Sikai Lu! ##")
	print("################################################")
	print()

	# print original board
	print("original:")
	board = load_board_from_disk(sys.argv[1])
	draw_board(board)
	print()

	# solve board
	solve(board)

# if __name__ == "__main__":
if __name__ == "__main__":
	main()
