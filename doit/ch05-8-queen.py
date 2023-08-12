"""
8*8 체스판에 8개의 퀸을 두는 모든 경우의 수에서 시작하여 주어진 조건에 따라 가능성을 하나씩 줄여 나가는 작업을 수행해보자.
"""

pos = [0 for _ in range(8)]  # 각 열에 배치한 퀸의 위치
row_check = [True for _ in range(8)]
ne_check = [True for _ in range(8)]
se_check = [True for _ in range(8)]


def recur(col: int):
    """가능한 col 열에 퀸을 두는 경우"""
    if col >= 8:
        return
    for row in range(8):
        if row_check[row] and ne_check[row] and se_check[col - row + 3]:
            pass
