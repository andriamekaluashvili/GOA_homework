#5)შექმენი ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა სიიდან ამოშალოთ მხოლოდ ის სიტყვები რომლის სიგრძეც ნაკლებია 5 ზე
def list1(cvladi):
    list2 = []
    for i in cvladi:
        if len(i) > 5:
            list2.append(i)
    return list2
print(list1(["gela" "gela2" "gela3"]))
 