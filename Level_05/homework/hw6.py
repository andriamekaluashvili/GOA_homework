#7)მომხმარებელს შემოატანინე 50 ზე მაღალი რიცხვი for loop გამოყენებით ერთიდან მომხმარებლის შემოტანილ რიცხვამდეე დაბეჭდეთ ყველა რიცხვი 5 step ის გამოყენებით,იგივე გაააკეთეთ while loop ითაც
num = int(input("შემოიტანე რიცხვი"))
for i in range(1,num,5):
    print(i)

num = int(input("შემოიტანე რიცხვი"))
count = 0
while num > count:
    count += 5
print(count)    


