def parcours_fourmi(position, orientation, cases_blanches):
    _nouvelle_orientation = nouvelle_orientation(position, orientation, cases_blanches)
    return [1, 3], _nouvelle_orientation, [[1, 3]]


def nouvelle_orientation(position, orientation, cases_blanches):
    if position in cases_blanches:
        if orientation == [0, -1]:
            return [-1, 0]
        if orientation == [1, 0]:
            return [0, -1]
        if orientation == [0, 1]:
            return [1, 0]
        if orientation == [-1, 0]:
            return [0, 1]
    else:
        if orientation == [0, -1]:
            return [1, 0]
        if orientation == [1, 0]:
            return [0, 1]
        if orientation == [0, 1]:
            return [-1, 0]
        if orientation == [-1, 0]:
            return [0, -1]
