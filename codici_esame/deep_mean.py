def deep_mean(a):
    risultato = 0
    count = 0

    for x in a:
        if type(x) == int:
            risultato += x
            count += 1
        elif type(x) == list:
            for e in x:
                if type(e)==int:
                    count += 1
            risultato += deep_mean(x)
        else:
            continue


    return risultato / count


a = [1,2,"ciao",[2,"dio"],3,[9]]

print(deep_mean(a))
