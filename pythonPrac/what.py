def lang_model():
    res = dict()
    f = open("count_number.txt")
    strL = f.readlines()
    for str in strL:
        spL = str.split()
        for word in spL:
            if(word in res):
                res[word] += 1
            else:
                res[word] = 1
    f.close()
    return res

def lang_model2():
    res = dict()
    f = open("count_number.txt")
    cont = f.read()
    cont.replace('\n', ' ')
    for word in cont.split():
        if(word in res):
            res[word] += 1
        else:
            res[word] = 1
    f.close()
    return res
