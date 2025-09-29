def lvable(l,s):
    """https://open.kattis.com/problems/lvable

    Args:
        l (int): lenght of the string
        s (str): the string

    Returns:
        _type_: number of operation to make it lv-able
    """
    if l == 1:
        if s[0] == 'l' or s[0]=='v':
            return 1
        return 2
    
    for i in range(l-1):
        
        if s[i:i+2] == 'lv':
            return 0
    
    for i in range(l-1):
        if s[i] == 'l': 
            return 1
    
    for i in range(1,l):
        if s[i] == 'v':
            return 1
        
    return 2