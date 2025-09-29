def number_of_inv_for_list_of_seq(s):
    """Kattis problem from https://open.kattis.com/problems/sequences

    Args:
        s (string): sequence of 0, 1 and ? 

    Return: 
        (int): Number of inversion to sort the list with unknown '?' (0 or 1)
    """


    def sequence_01(s:str):
        
        list_01_sequence_0 = []
        list_01_sequence_1 = []
        
        if len(s) == 0:
            return [[]]
        else:
            for i,c in enumerate(s): 
                if c != '?':
                    list_01_sequence_0.append(int(c))
                    list_01_sequence_1.append(int(c))
                else:
                    list_01_sequence_0.append(0)
                    list_01_sequence_1.append(1)
                    list_01_sequence_rec = sequence_01(s[i+1:])
                    list_01_sequence_return = []
                    for seq in list_01_sequence_rec:
                        list_01_sequence_return.append(list_01_sequence_0 + seq)
                        list_01_sequence_return.append(list_01_sequence_1 + seq)
                    return list_01_sequence_return
            return [list_01_sequence_1]

    def number_of_inv(seq):
        counter_inv = 0
        counter_0 = 0
        for i,element in enumerate(seq):
            if element == 0:
                counter_inv = counter_inv + i - counter_0
                counter_0 += 1

        return counter_inv 

    L = sequence_01(s)
    total_inv = 0
    for seq in L : 
        total_inv = total_inv + number_of_inv(seq)

    return total_inv % 1000000007