standard_input = "2 3 1"

from enum import Enum, auto


class Cmp(Enum):
    Less = auto()
    Greater = auto()
    Equal = auto()


def compare(lhs, rhs) -> Cmp:
    if lhs < rhs:
        return Cmp.Less
    elif lhs > rhs:
        return Cmp.Greater
    return Cmp.Equal


def sol_recur(n: int, dim: int, r: int, c: int, lo: int, hi: int) -> int:
    if dim == 0:
        return lo
    cell_area = 2 ** (2 * dim - 2)
    cell_side = 2 ** (dim - 1)
    match (compare(r, cell_side), compare(c, cell_side)):
        case (Cmp.Less, Cmp.Less):
            # 1분면에 있음
            hi = lo + cell_area
        case (Cmp.Less, Cmp.Greater):
            # 2분면에 있음
            lo += cell_area
            hi = lo + cell_area
            c -= cell_side
        case (Cmp.Greater, Cmp.Less):
            # 3분면에 있음
            lo += cell_area * 2
            hi = lo + cell_area
            r -= cell_side
        case _:
            # 4분면에 있음
            lo += cell_area * 3
            hi = lo + cell_area
            r -= cell_side
            c -= cell_side
    return sol_recur(n, dim - 1, r, c, lo, hi)


n, r, c = [int(e) for e in input().split()]

print(sol_recur(n, n, r, c, 0, 2 ** (2 * n)))
