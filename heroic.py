l = []

a, b = 1, 1

done = False

while not done:
    l.append([a, b])

    if b < 6:
        b += 1
    else:
        if a < 6:
            a += 1
            b = 1
        else:
            done = True

totals = []

for i in range(len(l)):
    total = 0

    for j in range(len(l[i])):
        total += l[i][j]

    total += 6

    totals.append(total)

eights, nines, tens, elevens, twelves, thirteens, fourteens, fifteens, sixteens, seventeens, eighteens = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for i in range(len(totals)):
    if totals[i] == 8:
        eights += 1
    elif totals[i] == 9:
        nines += 1
    elif totals[i] == 10:
        tens += 1
    elif totals[i] == 11:
        elevens += 1
    elif totals[i] == 12:
        twelves += 1
    elif totals[i] == 13:
        thirteens += 1
    elif totals[i] == 14:
        fourteens += 1
    elif totals[i] == 15:
        fifteens += 1
    elif totals[i] == 16:
        sixteens += 1
    elif totals[i] == 17:
        seventeens += 1
    elif totals[i] == 18:
        eighteens += 1

print(eights, nines, tens, elevens, twelves, thirteens, fourteens, fifteens, sixteens, seventeens, eighteens)
