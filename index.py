inp = input('Pls enter your Array! (eg.1 ,2): ')
index = inp.split(',')
indexs = []
for idx in index:
    try:
        int(idx)
    except:
        raise Exception("Array must be Float or Integer")
    indexs.append(int(idx))

vals = 0
position = 0
for chk in range(len(indexs)):
    if indexs[chk] > vals:
        vals = indexs[chk]
        position = chk

print("Most value number in Array : %s , Index position : %s"%(vals, position))


