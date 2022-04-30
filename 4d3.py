l = []

a, b, c, d = 1, 1, 1, 1

done = False

while not done:
    print(a, b, c, d)
    l.append([a, b, c, d])

    if d < 3:
        d += 1
    else:
        if c < 3:
            c += 1
            d = 1
        else:
            if b < 3:
                b += 1
                c = 1
                d = 1
            else:
                if a < 3:
                    a += 1
                    b = 1
                    c = 1
                    d = 1
                else:
                    done = True

editedL = []

for i in range(len(l)):
    minim = 4
    pos = 4
    for j in range(len(l[i])):
        if l[i][j] < minim:
            minim = l[i][j]
            pos = j

    temp = []

    for j in range(len(l[i])):
        if j != pos:
            temp.append(l[i][j])

    editedL.append(temp)

totals = []

for i in range(len(editedL)):
    total = 0

    for j in range(len(editedL[i])):
        total += editedL[i][j]

    totals.append(total)

print(len(totals))

threes, fours, fives, sixes, sevens, eights, nines = 0, 0, 0, 0, 0, 0, 0

for i in range(len(totals)):
    if totals[i] == 3:
        threes += 1
    elif totals[i] == 4:
        fours += 1
    elif totals[i] == 5:
        fives += 1
    elif totals[i] == 6:
        sixes += 1
    elif totals[i] == 7:
        sevens += 1
    elif totals[i] == 8:
        eights += 1
    elif totals[i] == 9:
        nines += 1

print(threes, fours, fives, sixes, sevens, eights, nines)
