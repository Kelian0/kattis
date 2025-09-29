def gluttonous_george(s:str):
    """https://open.kattis.com/problems/goggi

    Args:
        s (str): "number_1 ? number_2"

    Returns:
        str: operator ?
    """
    j=0
    while s[j] != '?':
        j += 1
    number_1 = int(s[:j-1])
    number_2 = int(s[j+1:])

    if number_1 > number_2:
        output = '>'
    elif number_1 < number_2:
        output = '<'
    else:
        output = 'Goggi svangur!'
    
    return output