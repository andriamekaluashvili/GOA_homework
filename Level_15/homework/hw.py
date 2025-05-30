#1)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი,შენი დავალებაა ამ სტრინგიდან ამოშალო კენტ იდექსზე მდგომი ასოები და დააბრუნო სტრინგი მათ გარეშე
def remove_odd(User_string):
    result = ''
    for index in range(len(User_string)):
        if index % 2 != 0:
           result += User_string[index]
    return result      

        




print(remove_odd('Goa Academy'))    
