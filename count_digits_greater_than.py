def count_digits_greater_than(n, t):
    if n < 0:
        return -1
    if t not in range(0, 10):
        return -1
    
    n_str = str(n)

    count = 0
    for a in n_str:
        if int(a) > t:
            count += 1
    return count