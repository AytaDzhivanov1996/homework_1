def solve(n, repeats):
    summa = []
    counter = 1
    while counter <= repeats:
        elem = str(n)*counter
        summa.append(int(elem))
        counter += 1
    return sum(summa)
