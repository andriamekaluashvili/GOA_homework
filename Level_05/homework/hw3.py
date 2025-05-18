#4)მომხმარებელს შემოატანინე მისი საყვარელი ფერი,თუ საყვარელი ფერი ემთხვევა წითელს ტერმინალში გამოუტანე red is favorite color,თუ შემოტანილი ფერი ემთხვევა ყვითელს დაუპტინტე favorite color is yellow,თუ შემოტანილი ფერი ემთხვევა ლურჯს დაუპრინტე favorite color is blue,ყველა სხვა დანარჩენ შემთხვევაში დაუპტინტე other color
color = input("შემოიტანე შენი საყვარელი ფერი")
if color == "წითელს":
    print("red is favorite color")
elif color == "ყვითელს":
    print("favorite color is yellow")
elif color == "ლურჯი":
    print("favorite color is blue")
else:
    print("other color")    
    

