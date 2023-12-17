#
# python step_2_0.py
#


def create_empty_board(edge_size):
    """辺の長さを指定して、盤を生成
    
    Parameters
    ----------
    edge_size : int
        一辺の長さ
    """
    return ["."] * (edge_size * edge_size)


def scan_board(board, edge_size, on_cell, on_line_end):
    """盤を走査します"""
    for y in range(0,edge_size):
        for x in range(0,edge_size):
            on_cell(x, y, board[y*edge_size+x])
        on_line_end()


def print_board(edge_size, board):
    """盤の表示
    
    Parameters
    ----------
    edge_size : int
        一辺の長さ
    board : list
        盤
    """
    scan_board(
        board,
        edge_size,
        lambda x, y, color: print(color, end=""),
        lambda: print(""))


def overwrite_4_boards(src_board, src_edge_size, dst_board, dst_edge_size):
    """srcテーブルを４つ、dstテーブルへ上書きコピーしたい"""

    def on_cell_top_left(x, y, color):
        # 元のテーブルの x, y を、列、行へ変換、先のテーブルの x, y に変換
        src_col = x % src_edge_size
        src_row = x // src_edge_size

        dst_x = src_col
        dst_y = src_row * dst_edge_size

        dst_board[dst_y + dst_x] = color

    def on_cell_bottom_right(x, y, color):
        # 元のテーブルの x, y を、列、行へ変換、先のテーブルの x, y に変換
        src_col = x % src_edge_size
        src_row = x // src_edge_size

        dst_x = src_col + (edge_size2//2)
        dst_y = (src_row+ (edge_size2//2)) * dst_edge_size

        dst_board[dst_y + dst_x] = color

    # TODO 左上へコピー
    scan_board(
        board=src_board,
        edge_size=src_edge_size,
        on_cell=on_cell_top_left,
        on_line_end=lambda: print(""))

    # TODO 右下へコピー
    scan_board(
        board=src_board,
        edge_size=src_edge_size,
        on_cell=on_cell_bottom_right,
        on_line_end=lambda: print(""))

    # TODO ３回目のコピー
    # TODO ４回目のコピー

    pass

if __name__ == "__main__":

    print("Start. Please enter key.")
    input()

    # ラウンド数
    round_size = 1

    # 辺の長さを指定して、盤を生成
    edge_size = 1
    board = create_empty_board(edge_size)

    # 基準点に 0 を入れる
    board[0] = 0

    # 表示
    print_board(edge_size, board)

    print("Please enter key.")
    input()

    # 辺の長さを指定して、盤を生成
    edge_size2 = 2
    board2 = create_empty_board(edge_size2)

    # １つ前の盤を４か所に上書きコピーしたい
    overwrite_4_boards(
        src_board=board,
        src_edge_size=edge_size,
        dst_board=board2,
        dst_edge_size=edge_size2)

    # 表示
    print_board(edge_size2, board2)

    print("Finished.")
