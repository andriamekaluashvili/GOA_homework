#4)შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია,თქვენი დავალებაა ამ სიიდან ამოშალოთ კენტი რიცხვები და დააბრუნოთ სია კენტი რიცხვების გარეშე
def num(user):
    list1 = []
    for i in user:
        if i % 2==0:
            list1.append(i)
    return list1

