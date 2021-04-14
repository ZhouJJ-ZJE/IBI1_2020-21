def Reverse(seq):
    # creat a dictionary
    dict = {"A": "T",
            "T": "A",
            "G": "C",
            "C": "G",
            "a": "t",
            "t": "a",
            "g": "c",
            "c": "g", }
    seq_list = list(seq)
    seq_list = [dict[base] for base in seq_list]
    string = ''.join(seq_list)  # change list into string
    result = string[::-1]  # reverse the string
    return result


print(Reverse('ATCG'))  # print result
