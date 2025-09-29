def take_two_stone(i):

    """https://open.kattis.com/problems/twostones

    Returns:
        str: winner between Alice and Bob
    """
    i = int(i)
    if i%2 == 0:
        return 'Bob'
    else:
        return 'Alice'