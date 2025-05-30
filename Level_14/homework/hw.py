#2) შექმენით ფუნქცია რომელიც მომხმარებელის შემოატანილ რიცხვის ფაქტორიალს დააბრუნებს.
def great(user):
    cvladi = 1
    for i in range(1,user + 1):
        cvladi *= i
    return cvladi    

