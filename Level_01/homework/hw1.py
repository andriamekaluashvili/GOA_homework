user_name = "ნიკოლოზი"
user_age = 20
favorite_color = "მწვანე"

print(user_name)
print(user_age)
print(favorite_color)
 # დავუშვათ ფოტოზე ეს იყო გამოსახული:
# name = "Goga"
# age = 30
# height = 1.85

# აქ არის 3 ცვლადი:
# name - ინახავს სტრინგს
# age - ინახავს მთელ რიცხვს (integer)
# height - ინახავს ათწილადს (float)

# ახლა იგივე სტილში ვქმნი სამ ახალ ცვლადს:
user_city = "თბილისი"         # ინახავს სტრინგს - ქალაქის სახელს
user_height = 1.75            # ინახავს float-ს - სიმაღლეს
is_married = False            # ინახავს ბულეანს - არის თუ არა დაქორწინებული
# კონკატენაცია ნიშნავს სტრინგების შეერთებას ერთმანეთთან

# მაგალითი:
first_name = "Goga"
last_name = "Chalauri"
full_name = first_name + " " + last_name

print(full_name)  # გამოიტანს: Goga Chalauri

# სხვანაირი მაგალითიც:
print("სალამი " + "მეგობარო")  # გამოიტანს: სალამი მეგობარო
first_name = "გოგა"
last_name = "ჩალაური"
age = 30
height = 1.80
city = "თბილისი"

# ყველაფერი ვაქციოთ სტრინგად და გავაერთიანოთ
sentence = (
    "ჩემი სახელი არის " + first_name + " " + last_name +
    ", ვარ " + str(age) + " წლის, სიმაღლე მაქვს " + str(height) +
    " მეტრი და ვცხოვრობ ქალაქ " + city + "-ში."
)

print(sentence)
car_name = input("შეიყვანე ავტომობილის სახელი: ")
car_color = input("შეიყვანე ავტომობილის ფერი: ")
car_price = int(input("შეიყვანე ავტომობილის ფასი (რიცხვი): "))
car_year = int(input("შეიყვანე ავტომობილის გამოშვების თარიღი: "))

# კონკატენაცია
info = (
    "თქვენი ავტომობილია " + car_name + ", ფერი: " + car_color +
    ", ფასი: " + str(car_price) + " ლარი, გამოშვების წელი: " + str(car_year)
)

print(info)
my_age = 21              # integer
my_name = "თეკლა"        # string
my_height = 1.65         # float
is_student = True        # boolean
city = input("შეიყვანე შენი საცხოვრებელი ადგილი: ")
favorite_animal = input("შეიყვანე შენი საყვარელი ცხოველი: ")

print("შენ ცხოვრობ", city, "-ში და შენი საყვარელი ცხოველია:", favorite_animal)
# პირველი ცვლადი: int → str
my_number = 25
my_number_str = str(my_number)  # ფუნქცია str() გარდაქმნის int-ს სტრინგად

# მეორე ცვლადი: str → int
some_string_number = "40"
converted_number = int(some_string_number)  # ფუნქცია int() გარდაქმნის სტრინგს რიცხვად

# დავპრინტოთ, თუ არ გჯერა 😁
print("my_number_str:", my_number_str, type(my_number_str))         # <class 'str'>
print("converted_number:", converted_number, type(converted_number)) # <class 'int'>
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))

print("მიმატება (+):", num1 + num2)
print("გამოკლება (-):", num1 - num2)
print("გაყოფა (/):", num1 / num2)
print("მთელი გაყოფა (//):", num1 // num2)
print("გამრავლება (*):", num1 * num2)
print("შედარება (==):", num1 == num2)
print("ნაშთი (%):", num1 % num2)
# % ნიშნავს გაყოფის ნაშთს
# მაგ: 7 % 3 → 1  (რადგან 7-ს რომ გავყოთ 3-ზე, მივიღებთ 2*3 = 6 და დარჩება ნაშთი 1)
# კიდევ: 10 % 2 → 0 (რადგან 2-ზე სრულად იყოფა)
