str1=input("Bulmak istediğiniz değeri giriniz:")
frekans=dict()

for karakter in str1:
    if karakter in frekans:
        frekans[karakter] +=1
    else:
        frekans[karakter] = 1
 
for x,j in frekans.items():
    print(f"{x} harfi {j} defa geçiyor.")         