standard_input = "110"

MAX = 1_000
hansu = [1 for _ in range(MAX + 1)]
hansu[0] = 0

for i in range(100):
    # 두 자리수까지는 전부 한수
    hansu[i] = i
