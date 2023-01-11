def sum_numeric(limit = 10)-> int:
    s = 0
    for n in range(1, limit):
        if n % 3==0 or n % 5==0:
            s += n
    return s


def suma(seq: Sequence[int]) -> int:
    if len(seq) == 0:
        return 0
    return seq[0] + suma(seq[1:])

def until(
        limit: int,
        filter_func: Callable[[int], bool],
        v: int
) -> list[int]:
    if v == limit:
        return []
    elif filter_func(v):
        return [v] + until(limit, filter_func, v + 1)
    else:
        return until(limit, filter_func, v + 1)

wyniki = []
wyniki.append(sum_numeric(30))
wyniki.append(sum_numeric(49))
wyniki.append(sum_numeric(50))
wyniki.append(sum_numeric(60))
wyniki.append(sum_numeric(70))
wyniki.sort()
print(wyniki)
print(suma(wyniki))
