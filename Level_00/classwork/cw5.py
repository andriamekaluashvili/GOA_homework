
text = input("შეიყვანე ტექსტი: ")
times = int(input("რამდენჯერ დავბეჭდო ტექსტი? "))

print(text * times)  # ან ციკლით:
for i in range(times):
    print(text)
