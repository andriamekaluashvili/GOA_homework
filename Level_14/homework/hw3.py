#4) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ სტრინგს დაფარავს *-ით
def great(user):
    cvladi = ""
    for i in user:
        cvladi = cvladi + "*"
    return cvladi    