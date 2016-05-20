def calculScore (lancers):
    score = 0
    total_tour = 0

    for tour in lancers:
        total_tour_precedent = total_tour
        total_tour = 0

        for lancer in tour:
            if (total_tour_precedent == 10):
                total_tour += lancer
                score += lancer * 2
                total_tour_precedent = lancer
            else:
                total_tour += lancer
                score +=lancer
    return (score)
