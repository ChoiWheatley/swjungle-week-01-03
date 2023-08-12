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
    cell_size = 2 ** (2 * dim - 2)
    match (compare(r, 2 ** (dim - 1)), compare(c, 2 ** (dim - 1))):
        case (Cmp.Less, Cmp.Less):
            # 1분면에 있음
            hi = lo + cell_size
        case (Cmp.Less, Cmp.Greater):
            # 2분면에 있음
            lo += cell_size
            hi = lo + cell_size
        case (Cmp.Greater, Cmp.Less):
            # 3분면에 있음
            lo += cell_size * 2
            hi = lo + cell_size
        case _:
            # 4분면에 있음
            lo += cell_size * 3
            hi = lo + cell_size
    return sol_recur(n, dim - 1, r, c, lo, hi)


n, r, c = [int(e) for e in input().split()]

print(sol_recur(n, n, r, c, 0, 2 ** (2 * n)))
