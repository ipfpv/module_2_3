my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_numbers = []

index = 0

while index < len(my_list):
    number = my_list[index]
    if number < 0:
        break
    if number > 0:
        positive_numbers.append(number)
    index += 1

print(positive_numbers)