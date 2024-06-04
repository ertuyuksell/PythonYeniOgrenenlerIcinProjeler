list = ["345","sadas","324a","14","kemal","1"]
newList=[]
for i in list:
    try:
        int(i)
        print(f"{i},sadece rakamdan oluşmaktadır.")
        newList.append(i)
    except:
        print(f"{i},sadece rakamdan oluşmamaktadır.")

print(newList)