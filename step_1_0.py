#
# python step_1_0.py
#

if __name__ == "__main__":

    # 辺の長さ。正方形とする
    edge_size = 8

    # 8x8 の配列
    board = ["*"] * (edge_size * edge_size)

    print("hello")

    for y in range(0,edge_size):
        for x in range(0,edge_size):
            print(board[y*edge_size+x], end="")
        print("")
