def d_fyrir_dreki(a,b,c):

    """https://open.kattis.com/problems/dfyrirdreki

    Returns:
        int: number of roots for the polynomial ax² + bx + c
    """
    if b**2 - 4*a*c > 0:
        return 2
    elif b**2 - 4*a*c == 0:
        return 1
    else:
        return 0