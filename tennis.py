def tennis(test):
    return True


def match(points):
    game = [15, 30, 40, "advantage"]
    scors = []
    scor_1 = 0
    scor_2 = 0
    ball_1 = 0
    ball_2 = 0

    for point in points:

        if point == "p1":
            if scor_1 == game[2] and point == "p2":
                scor_1 = game[2]
                ball_1 -= 2
            scor_1 = game[ball_1]
            ball_1 += 1

        if point == "p2":
            if scor_2 == game[2] and point == "p1":
                scor_2 = game[2]
                ball_2 -= 2
            scor_2 = game[ball_2]
            ball_2 += 1

    scors.append(scor_1)
    scors.append(scor_2)
    return scors
