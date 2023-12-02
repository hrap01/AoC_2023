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

count_sum = 0

for line in lines:

    highest_red = 0
    highest_blue = 0
    highest_green = 0
    for i in range(1, len(line)):

        red = 0
        green = 0
        blue = 0
        for j in range(len(line[i])):

            if 'red' in line[i][j]:
                red = int(line[i][j].lstrip()[:2])
            elif 'green' in line[i][j]:
                green = int(line[i][j].lstrip()[:2])
            elif 'blue' in line[i][j]:
                blue = int(line[i][j].lstrip()[:2])

            if red > highest_red:
                highest_red = red
            elif green > highest_green:
                highest_green = green
            elif blue > highest_blue:
                highest_blue = blue

    count_sum += (highest_red*highest_green*highest_blue)


print(count_sum)