#
# python step_1_0.py
#

def get_opponent(me, round, player_size):
    """対戦相手の選手番号（基数）を取得

    Parameters
    ----------
    me : int
        自分の選手番号（基数）
    round : int
        ラウンド数（序数）
    player_size : int
        選手全員の数
    """
    if me % 2 == 0:
        return (me + player_size + round) % player_size
    else:
        return (me + player_size - round) % player_size


if __name__ == "__main__":

    print("hello")

    # 最終ラウンド
    max_round = 1

    # 辺の長さ。正方形とする
    edge_size = 8

    # 8x8 の配列
    board = [" "] * (edge_size * edge_size)

    # 対角線をプロット
    for y in range(0,edge_size):
        for x in range(0,edge_size):
            if y == x:
                board[y*edge_size+x] = "\\"


    for round in range(1,3):
        # 第nラウンド目をプロット
        for y in range(0,edge_size):
            x = get_opponent(y, round, edge_size)
            board[y*edge_size+x] = "*"

    # 表示
    for y in range(0,edge_size):
        for x in range(0,edge_size):
            print(board[y*edge_size+x], end="")
        print("")
