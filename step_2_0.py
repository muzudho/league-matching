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


def overwrite_4_boards(src, src_edge_size, dst, dst_edge_size):
    """srcテーブルを４つ、dstテーブルへ上書きコピーしたい"""

    # TODO １回目のコピー
    # TODO ２回目のコピー
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

    ## 対角線をプロット
    #for y in range(0,edge_size):
    #    for x in range(0,edge_size):
    #        if y == x:
    #            board[y*edge_size+x] = "\\"

    # 表示
    print_board(edge_size, board)

    print("Please enter key.")
    input()

    # 辺の長さを指定して、盤を生成
    edge_size = 2
    board2 = create_empty_board(edge_size)

    # １つ前の盤を４か所に上書きコピーしたい

    ## 対角線をプロット
    #for y in range(0,edge_size):
    #    for x in range(0,edge_size):
    #        if y == x:
    #            board2[y*edge_size+x] = "\\"

    # 表示
    print_board(edge_size, board2)

    print("Finished.")
