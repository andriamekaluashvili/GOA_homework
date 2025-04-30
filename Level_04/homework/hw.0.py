#1) მომხმარებელს შემოატანინე რიცხვი და მომხმარებლის შემოტანილ რიცხვამდე გამოიტანეთ ყველა რიცხვის კვადრატების ჯამი.
number = int(input("შეიყვანე რიცხვი: "))
sum_of_squares = 0
for i in range(number):
    sum_of_squares += i ** 2
print("კვადრატების ჯამი არის:", sum_of_squares)
