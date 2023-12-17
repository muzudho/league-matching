#
# python step_2_0.py
#

if __name__ == "__main__":

    print("Start. Please enter key.")
    input()

    # ラウンド数
    round_size = 1

    # 辺の長さを指定して、盤を生成
    edge_size = 1
    board = [" "] * (edge_size * edge_size)

    # 対角線をプロット
    for y in range(0,edge_size):
        for x in range(0,edge_size):
            if y == x:
                board[y*edge_size+x] = "\\"

    # 表示
    for y in range(0,edge_size):
        for x in range(0,edge_size):
            print(board[y*edge_size+x], end="")
        print("")

    print("Please enter key.")
    input()

    # 辺の長さを指定して、盤を生成
    edge_size = 2
    board2 = [" "] * (edge_size * edge_size)

    # 対角線をプロット
    for y in range(0,edge_size):
        for x in range(0,edge_size):
            if y == x:
                board2[y*edge_size+x] = "\\"

    # 表示
    for y in range(0,edge_size):
        for x in range(0,edge_size):
            print(board2[y*edge_size+x], end="")
        print("")

    print("Finished.")
