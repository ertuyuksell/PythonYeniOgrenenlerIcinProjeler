newList=[]
def ciftMi(sayi):
    if sayi % 2 == 0:
        newList.append(sayi)
        return sayi
    else:
        raise ValueError

list = [34,2,1,3,33,100,61,1800]

for i in list:
    try:
        print(ciftMi(i))
    except ValueError:
        pass
print(newList)