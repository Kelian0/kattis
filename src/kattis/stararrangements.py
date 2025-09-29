def star_arrangements(nb_s):
    """https://open.kattis.com/problems/stararrangements

    Args:
        nb_s (int): number of star

    Returns:
        list: star arrangement
    """
    L = []

    for i in range(1,nb_s//2 + 2):
        for j in range(0,2):
            x = i + j 
            y = i 

            # Cas 1: nb_s = k * (x + y) 
            if nb_s % (x +y) == 0:
                L.append([x,y])

            # Cas 2: nb_s = k * (x + y) + x

            if (nb_s - x) % (x+y) == 0:
                L.append([x,y])
        


    return L 