import func as f



playing = True

while True:
	board = [' ']*10
	print('Welcome to Tick-Tack Toe')
	player_1 = f.choose_marker()
	player_2 = f.switch_player(player_1)
	current_player = f.go_first(player_1, player_2)

	while True:
		f.display_board(board)
		f.place_marker(current_player, board)
		if f.win_check(current_player, board):
			print(current_player, 'has won the game!')
			break
		elif f.tie_check(board):
			print('This game is a TIE!')
			break
		else:
			current_player = f.switch_player(current_player)
			continue

	if f.play_again():
		continue
	break

