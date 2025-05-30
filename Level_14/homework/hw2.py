#3) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილი რიცხვის ჩათვლით დაგვიბრუნებს გამრავლების ტაბულას.
def great(user):
    list1 = []
    for i in range(1,user + 1):
        list1.append(i*user)
    return list1    
