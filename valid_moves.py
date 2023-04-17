def is_valid_move(boards, white_to_move, start_board, end_board, start_pos, end_pos):
    sx = int(round(start_pos[0], 0))
    sy = int(round(start_pos[1], 0))
    ex = int(round(end_pos[0], 0))
    ey = int(round(end_pos[1], 0))
    
    start_piece = start_board.board_state[sx][sy]
    if start_piece == '.':
        return False
    elif white_to_move and start_piece.lower() == start_piece:
        return False
    elif not white_to_move and start_piece.lower() != start_piece:
        return False

    target_piece = end_board.board_state[ex][ey]

    if target_piece != '.' and target_piece.isupper() == start_piece.isupper():
        return False

    if start_board == end_board:
        board = start_board
        if start_piece == "P":
            if sy == ey and board.board_state[ex][ey] == '.':
                if ex == sx - 1:
                    return True
                if sx == 6 and ex == sx - 2 and board.board_state[sx-1][sy] == '.':
                    return True
                else:
                    return False
            elif abs(sy - ey) == 1 and ex == sx - 1 and board.board_state[ex][ey].islower():
                return True
            else:
                return False

        if start_piece == "p":
            if sy == ey and board.board_state[ex][ey] == '.':
                if ex == sx + 1:
                    return True
                if sx == 1 and ex == sx + 2 and board.board_state[sx + 1][sy] == '.':
                    return True
                else:
                    return False
            elif abs(sy - ey) == 1 and ex == sx + 1 and board.board_state[ex][ey].isupper():
                return True
            else:
                return False
        
        if start_piece.lower() == "r":
            if sy == ey:
                for j in range(min(sx, ex) + 1, max(sx, ex)):
                    if board.board_state[j][sy] != '.':
                        return False
            elif sx == ex:
                for i in range(min(sy, ey) + 1, max(sy, ey)):
                    if board.board_state[sx][i] != '.':
                        return False
            else:
                return False

            return True
        
        if start_piece.lower() == "n":
            if abs(sx - ex) == 2 and abs(sy - ey) == 1:
                return True
            elif abs(sy - ey) == 2 and abs(sx - ex) == 1:
                return True
            else:
                return False
        
        if start_piece.lower() == "b":
            if abs(sx - ex) == abs(sy - ey):
                x_dir = 1 if ex > sx else -1
                y_dir = 1 if ey > sy else -1
                x, y = sx + x_dir, sy + y_dir
                while x != ex and y != ey:
                    if board.board_state[x][y] != ".":
                        return False
                    x += x_dir
                    y += y_dir
                return True
            return False
        
        if start_piece.lower() == "q":
            if sx == ex or sy == ey:
                if sy == ey:
                    for j in range(min(sx, ex) + 1, max(sx, ex)):
                        if board.board_state[j][sy] != '.':
                            return False
                elif sx == ex:
                    for i in range(min(sy, ey) + 1, max(sy, ey)):
                        if board.board_state[sx][i] != '.':
                            return False
                else:
                    return False
                return True
            elif abs(sx - ex) == abs(sy - ey):
                if abs(sx - ex) == abs(sy - ey):
                    x_dir = 1 if ex > sx else -1
                    y_dir = 1 if ey > sy else -1
                    x, y = sx + x_dir, sy + y_dir
                    while x != ex and y != ey:
                        if board.board_state[x][y] != ".":
                            return False
                        x += x_dir
                        y += y_dir
                    return True
                return False
        
        if start_piece.lower() == "k":
            if abs(sx - ex) <= 1 and abs(sy - ey) <= 1:
                return True
            return False
    else:
        if start_pos != end_pos:
                return False

        for i, l in enumerate(boards):
                if start_board in l:
                    start_index = i
                if end_board in l:
                    end_index = i

        if start_piece.lower() == "p":
            if start_index == end_index:
                if abs(boards[start_index].index(start_board) - boards[end_index].index(end_board)) == 1:
                    return True
            elif abs(start_index - end_index) == 1 and boards[start_index].index(start_board) == boards[end_index].index(end_board):
                return True
            else:
                return False
        
        if start_piece.lower() == "r":
            if start_index == end_index and boards[start_index].index(start_board) != boards[end_index].index(end_board):
                return True
            elif start_index != end_index and boards[start_index].index(start_board) == boards[end_index].index(end_board):
                return True
            else:
                return False

        if start_piece.lower() == "n":
            if abs(start_index - end_index) == 2 and abs(boards[start_index].index(start_board) - boards[end_index].index(end_board)) == 1:
                return True
            elif abs(start_index - end_index) == 1 and abs(boards[start_index].index(start_board) - boards[end_index].index(end_board)) == 2:
                return True
            else:
                return False

        if start_piece.lower() == "b":
            if abs(start_index - end_index) == abs(boards[start_index].index(start_board) - boards[end_index].index(end_board)):
                return True
            else:
                return False

        if start_piece.lower() == "q":
            if abs(start_index - end_index) == abs(boards[start_index].index(start_board) - boards[end_index].index(end_board)):
                return True
            elif start_index == end_index and boards[start_index].index(start_board) != boards[end_index].index(end_board):
                return True
            elif start_index != end_index and boards[start_index].index(start_board) == boards[end_index].index(end_board):
                return True
            else:
                return False

        if start_piece.lower() == "k":
            if abs(start_index - end_index) <= 1 and abs(boards[start_index].index(start_board) - boards[end_index].index(end_board)) <= 1:
                return True
            else:
                return False