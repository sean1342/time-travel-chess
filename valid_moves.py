def is_valid_move(board, piece_pos, end_pos):
    if piece_pos == end_pos:
        return False
    if piece_pos[0] < 0 or piece_pos[0] > 7 or piece_pos[1] < 0 or piece_pos[1] > 7:
        return False
    if end_pos[0] < 0 or end_pos[0] > 7 or end_pos[1] < 0 or end_pos[1] > 7:
        return False
    
    sx = int(round(piece_pos[0], 0))
    sy = int(round(piece_pos[1], 0))

    ex = int(round(end_pos[0], 0))
    ey = int(round(end_pos[1], 0))

    piece = board.board_state[sx][sy]
    if piece == '.':
        return False

    target_piece = board.board_state[ex][ey]

    if target_piece != '.' and target_piece.isupper() == piece.isupper():
        return False

    # code for all of the validity checks
    if piece == "P":
        if sy == ey and board.board_state[ex][ey] == '.':
            # move forward one square
            if ex == sx - 1:
                return True
            # move forward two squares
            if sx == 6 and ex == sx - 2 and board.board_state[sx-1][sy] == '.':
                return True
            else:
                return False
        elif abs(sy - ey) == 1 and ex == sx - 1 and board.board_state[ex][ey].islower():
            # capture diagonally
            return True
        else:
            return False

    if piece == "p":
        if sy == ey and board.board_state[ex][ey] == '.':
            # move forward one square
            if ex == sx + 1:
                return True
            # move forward two squares
            if sx == 1 and ex == sx + 2 and board.board_state[sx + 1][sy] == '.':
                return True
            else:
                return False
        elif abs(sy - ey) == 1 and ex == sx + 1 and board.board_state[ex][ey].isupper():
            # capture diagonally
            return True
        else:
            return False
    
    if piece.lower() == "r":
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

        # Move is valid
        return True
    
    if piece.lower() == "n":
        if abs(sx - ex) == 2 and abs(sy - ey) == 1:
            return True
        elif abs(sy - ey) == 2 and abs(sx - ex) == 1:
            return True
        else:
            return False
    
    if piece.lower() == "b":
        if abs(sx - ex) == abs(sy - ey):
            # Check if there are any pieces in the diagonal path
            x_dir = 1 if ex > sx else -1
            y_dir = 1 if ey > sy else -1
            x, y = sx + x_dir, sy + y_dir
            while x != ex and y != ey:
                if board.board_state[x][y] != ".":
                    return False  # there is a piece in the way
                x += x_dir
                y += y_dir
            return True
        return False
    
    if piece.lower() == "q":
        # check if move is vertical or horizontal like rook
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
        # check if move is diagonal like bishop
        elif abs(sx - ex) == abs(sy - ey):
            if abs(sx - ex) == abs(sy - ey):
                # Check if there are any pieces in the diagonal path
                x_dir = 1 if ex > sx else -1
                y_dir = 1 if ey > sy else -1
                x, y = sx + x_dir, sy + y_dir
                while x != ex and y != ey:
                    if board.board_state[x][y] != ".":
                        return False  # there is a piece in the way
                    x += x_dir
                    y += y_dir
                return True
            return False
    
    if piece.lower() == "k":
        if abs(sx - ex) <= 1 and abs(sy - ey) <= 1:
            return True
        return False