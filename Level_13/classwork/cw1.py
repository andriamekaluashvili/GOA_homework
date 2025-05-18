#2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა და ამ სიტყვაში დაითვლის ასო "k'ს რაოდენობას. დააიგნოროს ქეის სენსიტიურობა.
def count_k(word):
    count = 0
    for char in word.lower():  
        if char == 'k':
            count += 1
    return count
user_input = input("შეიყვანეთ სიტყვა: ")
k_count = count_k(user_input)
print("'k' ასოს რაოდენობაა:", k_count)
