#5) მომხმარებელს შემოატანინეთ თქვენი საყვარელი ფერი მანამ სანამ არ გამოიცნობს.
favorite_color = "orange"
while True:
    guess = input("გამოიცანით ჩემი საყვარელი ფერი: ")
    if guess == favorite_color:
        print("სწორია")
        break
    else:
        print("არასწორია,ცადეთ კიდევ ")
