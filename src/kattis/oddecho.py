def odd_echo(s:str):
    """https://open.kattis.com/problems/oddecho

    Args:
        s (str): string

    Returns:
        str: odd index word
    """
    output = ''
    nb_line = int(s[0])
    s = s[2:]
    for i in range(nb_line):
        j=0
        while j<len(s) and (s[j] != '\n' or s[j] != ' ') :
            j=j+1
        if i%2==0:
            output = output + (s[:j])+'\n'

        s = s[j+1:]

    return output 
