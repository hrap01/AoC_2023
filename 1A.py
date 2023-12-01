lines = []

with open('1A.txt', encoding='utf-8') as file:
    for line in file:
        lines.append(line.replace('\n', ''))
sum = 0

for text in lines:
    number = ''
    for character in text:
        if character.isdigit():
            number += character
    number_to_save = number[0] + number[-1]
    sum += int(number_to_save)


print(sum)
