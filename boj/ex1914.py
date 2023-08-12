standard_input = "3"


def find_other_pile(x: int, y: int) -> int:
    return x ^ y


def hanoi(num: int, x: int, y: int, hook=None) -> int:
    """x 기둥에 박혀있는 원반 num개를 y 기둥으로 모두 옮기는 경우의 수"""
    if num == 1:
        if hook:
            hook((x, y))
        return 1
    z = find_other_pile(x, y)
    return (
        hanoi(num - 1, x, z, hook) + hanoi(1, x, y, hook) + hanoi(num - 1, z, y, hook)
    )


def solve(n):
    ls = []
    print(hanoi(n, 1, 3, ls.append if n <= 20 else None))
    for x, y in ls:
        print(x, y)


solve(int(input()))
