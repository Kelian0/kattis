def quadrant_selection(x,y):
    """https://open.kattis.com/problems/quadrant

    Args:
        x (int): x coordinate (non zero)
        y (int): y coordinate (non zero)

    Returns:
        int: index of de quadrant
    """

    if x>=0:
        if y>=0:
            return 1
        else:
            return 4 
    else:
        if y>=0:
            return 2
        else:
            return 3