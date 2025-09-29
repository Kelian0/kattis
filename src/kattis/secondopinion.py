def second_opinion(s):

    """https://open.kattis.com/problems/secondopinion

    Returns:
        str: time format {hours} : {minutes} : {seconds}
    """

    h = s // 3600
    m = (s % 3600) // 60
    sec = s % 60

    return f'{h} : {m} : {sec}'

    