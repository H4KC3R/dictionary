import os

import PyPDF2


def pdf_to_text(pdf_file_path):
    text = ""
    # Открываем PDF файл
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # # Создаем объект для записи текста в файл
        # with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
        # Проходим по всем страницам PDF
        for page_num in range(len(pdf_reader.pages)):
            # Получаем текст со страницы
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

            # # Записываем текст в файл
            # txt_file.write(text)

    print("PDF успешно сконвертирован в TXT.")

    return text


def process_articles(input_dir):
    # Создаем пустую строку для объединения текста из всех статей
    combined_text = ""

    # Проходим по всем файлам в директории
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            # Получаем путь к файлу
            file_path = os.path.join(input_dir, filename)

            # Преобразуем PDF в текст и добавляем его к общему тексту
            article_text = pdf_to_text(file_path)
            combined_text += article_text

    return combined_text


if __name__ == "__main__":
    # Путь к директории с PDF файлами
    input_dir = "articles"

    # Обрабатываем все статьи
    combined_text = process_articles(input_dir)

    # Путь для сохранения объединенного текста
    output_txt_file = "output/articles.txt"

    os.makedirs("output")

    # Сохраняем объединенный текст в файл
    with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(combined_text)

    print("Все статьи успешно сконвертированы в один TXT файл.")

