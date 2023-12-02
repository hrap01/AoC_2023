lines = []

with open(r'C:\Users\PavlaHrabcova\Documents\python\AoC\2A.txt', encoding='utf-8') as file:
    for line in file:
        text = line.replace('\n', '').split(':')
        insert_list = []
        text_1 = text[0]
        insert_list.append(text_1)
        text_2 = text[1].split(';')
        for text in text_2:
            insert_list.append(text.split(','))
        lines.append(insert_list)

red_comp = 12
green_comp = 13
blue_comp = 14
id_sum = 0

for line in lines:
    id = int(line[0].split(' ')[1])
    flag = 0
    for i in range(1, len(line)):
        red = 0
        green = 0
        blue = 0
        for j in range(len(line[i])):

            if 'red' in line[i][j]:
                red += int(line[i][j].lstrip()[:2])
            elif 'green' in line[i][j]:
                green += int(line[i][j].lstrip()[:2])
            elif 'blue' in line[i][j]:
                blue += int(line[i][j].lstrip()[:2])

        if red <= red_comp and green <= green_comp and blue <= blue_comp:
            pass
        else:
            flag += 1
    if flag == 0:

        id_sum += id


print(id_sum)