#6) მომხმარებელს შემოატანინეთ რიცხვი. შემდეგ სიტყვა სანამ არ შემოიტანს 'გაჩერდი!', ეგ ყველაფერი დაამატეთ ახალ სიაში და ამ სიიდან მომხმარებლის შემოტანილი რიცხვი რაც არის, იმაზე მდგომი სიტყვის ჩათვლით გამოიტანეთ ამ სიიდან სიტყვები. 
num = int(input("შემოიტანე რიცხვი"))
cvaldi = input("შემოიტანე ტექსტი")
list1 = []
while cvaldi != "გაჩერდი":
    list1.append(cvaldi)
    cvaldi1 = input("შემოიტანე ტექსტი")
print(list1 [num])

