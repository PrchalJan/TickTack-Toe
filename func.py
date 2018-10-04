import random



def choose_marker():

	while True:
		player_1 = input('Player_1, choose marker: x or o  ')
		if player_1.lower() == 'x':
			print('Player_1 is X')
			print('Player_2 is O')
			return 'X'
		elif player_1.lower() == 'o':
			print('Player_1 is O')
			print('Player_2 is X')
			return 'O'
		else:
			print('\n'*100)
			print('Welcome to the tic tac toe.')
			print('\n'*2)
			print('Please try again!')
			print('\n')

def switch_player(player):
	if player == 'X':
		return 'O'
	elif player == 'O':
		return 'X'
	else:
		print('VoleError')


def go_first(player_1, player_2):
	first_player = random.choice((player_1, player_2))
	print(first_player, 'will go first!')
	return first_player



def display_board(board):
	print('\n')
	print(' ', board[7], '|', board[8],'|', board[9])
	print('----|---|----')
	print(' ', board[4], '|', board[5],'|', board[6])
	print('----|---|----')
	print(' ', board[1], '|', board[2],'|', board[3])



def space_check(board, position):
	'''returns true if board[position] == ' '''
	return board[position] == ' '

def place_marker(player, board):
	while True:
		try:
			position = int(input(f'{player}, Place Marker 1-9: '))
		except:
			print('must be a number')
		else:
			if position in range(1,10) and space_check(board, position):
				board[position] = player
				print('\n'*100)
				break
			else:
				continue

def win_check(player, board):
	return ((board[1] == board[2] == board[3] == player) or
			(board[4] == board[5] == board[6] == player) or
			(board[7] == board[8] == board[9] == player) or
			(board[1] == board[4] == board[7] == player) or
			(board[2] == board[5] == board[8] == player) or
			(board[3] == board[6] == board[9] == player) or
			(board[1] == board[5] == board[9] == player) or
			(board[3] == board[5] == board[7] == player))

def tie_check(board):
	return ' ' not in board[1:]

def play_again():

	while True:
		play_again = input('Would you like to play again? y or n: ')
		if play_again[0].lower() == 'y':
			return True
		elif play_again[0].lower() == 'n':
			return False
		else:
			print('Try again!')
			continue






