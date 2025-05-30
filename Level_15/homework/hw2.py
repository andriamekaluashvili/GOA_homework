#3)შექმენი ფუნქცია როომელსაც გადაეცემა სახელებით სავსე სია,თქვენი დავალებაა დააბრუნოთ თითოეული ელემენტის ინდექსი(არ გამოიყენოთ len ფუნქცია)
def filter_(userStr):
    result = ''
    for i in userStr:
        if i not in 'aeiou':
            result += i
    return result
print(filter_("hidroeleqtrosadguri"))
