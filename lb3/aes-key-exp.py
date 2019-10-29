from pprint import pprint

def keyexp(key):
    temp = []
    w = []

    for k in range(0, 44):
        w.append([])
 

    for i in range(0,4):
        w[i] = (key[4*i] + key[4*i+1], key[4*i+2] + key[4*i+3])
        for i in range(4, 44):
            temp = w[i-1]
            if i%4 == 0:
                pass
            w[i] = w[i-4] + temp
    
    return w

pprint(keyexp("0f1571c947d9e8590cb7add6af7f6798"))