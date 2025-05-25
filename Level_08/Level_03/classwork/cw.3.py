#4) მომხმარებელს შემოატანინე ორი სტრინგი და for loop-ის საშუალებით დაითვალე  ორივეში სიმბოლოების რაოდენობა. შემდეგ დაპრინტეთ არის თუ არა ერთმანეთის ტოლი
# სიმბოლოების რაოდენობა. 
num = input("enter your num")
num1 = input("enter your num1")
count = 0
count1 = 0
for i in num:
    count = count+1

for i in num1:
    count1 = count+1
        

print(count == count1)