#6) მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტე ამ რიცხვის ჩათვლით ყველაფრის ჯამი.
number = int(input("შემოიტანე რიცხვი: "))
number1 = 0
for i in range(number):
    number1 = number1 + i
print(number1)