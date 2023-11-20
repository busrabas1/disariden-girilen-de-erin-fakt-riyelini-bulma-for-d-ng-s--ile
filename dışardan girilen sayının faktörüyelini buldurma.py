fak=int(input("faktöriyelini bulmak istediğin sayiyi gir"))
i=1
carpim=1
if i < fak:
    for i in range (1,fak):
        i=i+1
        carpim=i*carpim
print(carpim)
