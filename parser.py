import re

from bs4 import BeautifulSoup
import requests


def get_translation(word):
    # word = "wireless"
    url = f"https://www.multitran.com/m.exe?l1=1&l2=2&s={word}"
    response = requests.get(url)
    html_content = response.text

    # Создание объекта Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Поиск элемента <body> с определенным стилем
    body = soup.body
    container = body.find('div', class_='container')
    mclass_elements = container.find_all(class_='mclass160_10')[2]
    first_table = mclass_elements.find('table')
    rows = first_table.find_all('tr', recursive=False)

    # print(first_table)

    flag = 0

    all_trans = []

    a = 0

    for i, row in enumerate(rows):

        # if i < 3:
        #     continue

        if row.text.strip() == "English thesaurus":
            break

        if row.has_attr('height'):
            a = 2

        # Находим все элементы <td> в текущей строке
        cells = row.find_all('td')
        # Если в строке есть два элемента <td>, то это наши данные subj и trans
        # if len(cells) == 2:
        #     print(len(cells))
        # if not cells:
        #     continue

        # l = len(cells)

        if a > 0:
            flag = 1
            a -= 1
            # print("aaaaaaaa")
        else:
            if len(cells) == 2 and flag > 0:
                trans = cells[1].text.strip()
                trans = trans.split(';')
                trans = [re.sub(r'\s*\([^)]*\)', '', el) for el in trans]
                if len(trans) > 4:
                    trans = trans[:4]
                if len(all_trans) > 10:
                    trans = [trans[0]]
                # print("subj:", subj)
                # print("trans:", trans)
                all_trans.append(trans)
                # print("---------------------")
                flag -= 1


    all_trans = [el for sub in all_trans for el in sub]

    if 'stresses' in all_trans:
        all_trans.remove('stresses')
    return all_trans
    # print(all_trans)


if __name__ == "__main__":
    # Открываем файл для чтения
    all_res = []
    with open("words_thinned_wo_lines.txt", "r") as file:
        # Читаем все содержимое файла
        words = file.read().split()

        # Перебираем слова и вызываем для каждого get_translation
        for word in words:
            result = get_translation(word)
            all_res.append([word, result])
            print(result)

    with open('dictionary.txt', 'w') as file:
        for res in all_res:
            file.write(res[0] + ": " + ', '.join(res[1]) + '.\n')

# if __name__ == "__main__":
#     word = "wireless"
#     result = get_translation(word)
#     print(result)

# for tr_i in tr:
#     td = tr_i.find_all('td')
#     if len(td) == 2:
#         print("subj:")
#         print(td[0].find("a"))
# td1 = tr_i.find('td')
# print("=======\n", len(td))
# print(td1)

# print(tr0)
