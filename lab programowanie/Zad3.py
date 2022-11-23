
keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
values = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]
slownik_1 = dict(zip(keys, values))
print(slownik_1)
klucz = [0,1,2,3,4,5,6,7,8,9,10]
wartosc = [1,2,4,8,16,32,64,128,256,512,1024]
slownik_2 = dict(zip(klucz , wartosc))
print(slownik_2)
"""
dict1 = {'data1':100, 'data2':-54, 'data3':247}
x = sum(dict1.values())
print(x)
print(slownik_1 | slownik_2)
newdict = slownik_1.copy()
newdict.update(slownik_2)
print(newdict)
"""
for keys in slownik_2:
    if keys in slownik_1:
        slownik_1[keys] += slownik_2[keys]
    else :
        slownik_1[keys] = slownik_2[keys]
print(slownik_1)
