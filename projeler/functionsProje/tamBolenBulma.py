print("""
*****************************
       Tam Bölen Bulma
*****************************      
""")

sayi=int(input("Bulmak İstediğiniz Sayıyı Giriniz:"))

def tamBolen(sayi):
    tamBolenList=[]
    for i in range(2,sayi):
        if sayi % i == 0:
            tamBolenList.append(i)
        else:
            continue
    print(tamBolenList)
    return tamBolenList    
tamBolen(sayi)            