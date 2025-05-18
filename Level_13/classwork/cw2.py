#3) შექმენით ფუნქცია რომელსაც არგუმენტად სია, ამ სიაში უნდა იყოს სხვადასხვა ტიპის მონაცემები და დაითვალოს რამდენი სტრინგ ტიპის მონაცემი არის 
def count_strings(lst):
    count = 0
    for item in lst:
        if isinstance(item, str):
            count += 1
    return count

mixed_list = [123, "hello", True, "world", 3.14, "!", None]
string_count = count_strings(mixed_list)
print("სტრინგი ელემენტების რაოდენობაა:", string_count)
