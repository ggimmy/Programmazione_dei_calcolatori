def anagramma(a,b):

    a_dict = {}
    b_dict = {}
    

    for c in a:
        if c == ' ':
            continue
        if c in a_dict:
            a_dict[c] += 1
        else:
            a_dict[c] = 1
    
    for c in b:
        if c == ' ':
            continue
        if c in b_dict:
            b_dict[c] += 1
        else:
            b_dict[c] = 1
    
    print(a_dict)
    print(b_dict)
    return a_dict == b_dict

    

a = "astronomers"
b = "no more stars"
print(anagramma(a,b))




