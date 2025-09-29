
def Dagatal(m):
    """https://open.kattis.com/problems/dagatal

    Args:
        m (int): month

    Returns:
        int: number of days
    """
    if m == 2:
        return 28

    if m <= 7:
        if m%2 == 1:
            return 31
        else :
            return 30
    
    if m >=8:
        if m%2 == 0:
            return 31
        else:
            return 30