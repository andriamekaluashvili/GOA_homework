#2)შექმენი ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია,თქვენი დავალებაა დააბრუნოთ ახალი სია სადაც გექნებათ მხოლოდ ლუწი რიცხვები
def list1(cvladi):
    list2 = []
    for i in cvladi:
        if i % 2 == 0:
            list2.append(i)
    return list2
    


        
    