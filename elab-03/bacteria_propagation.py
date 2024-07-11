def nb_year(p0, percent, aug, p):
    day = 0
    while 1:
        p0 = int(p0 * (1 + 1 * percent / 100) + aug)
        day += 1
        if p0 >= p:
            return day
