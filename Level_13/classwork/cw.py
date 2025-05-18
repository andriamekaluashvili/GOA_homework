#1) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა და დაითვლის სიგრძეს  len() ფუნქციის გარეშე.
def calculator_lenght(andria):
    count = 0
    for _ in andria:
        count += 1
    return count


user_input = input("შეიყვანეთ სიტყვა: ")
length = calculator_lenght(user_input)
print("სიტყვის სიგრძეა:", length)
