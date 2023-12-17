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
    return [" "] * (edge_size * edge_size)


def print_board(edge_size, board):
    """盤の表示
    
    Parameters
    ----------
    edge_size : int
        一辺の長さ
    board : list
        盤
    """
    for y in range(0,edge_size):
        for x in range(0,edge_size):
            print(board[y*edge_size+x], end="")
        print("")
    pass


if __name__ == "__main__":

    print("Start. Please enter key.")
    input()

    # ラウンド数
    round_size = 1

    # 辺の長さを指定して、盤を生成
    edge_size = 1
    board = create_empty_board(edge_size)

    # 対角線をプロット
    for y in range(0,edge_size):
        for x in range(0,edge_size):
            if y == x:
                board[y*edge_size+x] = "\\"

    # 表示
    print_board(edge_size, board)

    print("Please enter key.")
    input()

    # 辺の長さを指定して、盤を生成
    edge_size = 2
    board2 = create_empty_board(edge_size)

    # 対角線をプロット
    for y in range(0,edge_size):
        for x in range(0,edge_size):
            if y == x:
                board2[y*edge_size+x] = "\\"

    # 表示
    print_board(edge_size, board2)

    print("Finished.")
