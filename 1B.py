import re

lines = []

with open('1A.txt', encoding='utf-8') as file:
    for line in file:
        lines.append(line.replace('\n', ''))

sum = 0

number_dict = {'one': 1,
               'two': 2,
               'three': 3,
               'four': 4,
               'five': 5,
               'six': 6,
               'seven': 7,
               'eight': 8,
               'nine': 9}

number_list = ['1','2','3','4','5','6','7','8','9','0', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for text in lines:
    numbers_result = []
    for number in number_list:
        for m in re.finditer( number, text):
            numbers_result.append([number, m.start()])
    for result in numbers_result:
        try:
            result[0] = int(result[0])
        except:
            result[0] = number_dict[result[0]]

    numbers_result.sort(key=lambda x: x[1])
    number_to_save = str(numbers_result[0][0]) + str(numbers_result[-1][0])
    sum += int(number_to_save)

print(sum)
