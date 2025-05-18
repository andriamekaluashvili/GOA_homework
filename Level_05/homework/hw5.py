#6)მომხმარებელს შემოატანინე ათზე მაღალი რიცხვი,for loop ის გამოყენებით იპოვეთ 5 დან მომხმარებლის შემოტანილ რიცხვამდე ყველა რიცხვის ჯამი,იგივე გააკეთეთ while loop ითაც

num = int(input("შემოიტანე რიცხვი"))
count = 0
for i in range(5,num):
     count += i
print(count) 



num = int(input("შემოიტანე რიცხვი"))
count = 0 
sum = 0
while num > count :
     count += 1
     sum += count
print(sum)     
     
