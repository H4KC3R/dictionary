import PyPDF2


def pdf_to_text(pdf_file_path, output_txt_file):
    # Открываем PDF файл
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Создаем объект для записи текста в файл
        with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
            # Проходим по всем страницам PDF
            for page_num in range(len(pdf_reader.pages)):
                # Получаем текст со страницы
                page = pdf_reader.pages[page_num]
                text = page.extract_text()

                # Записываем текст в файл
                txt_file.write(text)

    print("PDF успешно сконвертирован в TXT.")


if __name__ == "__main__":
    # Путь к PDF файлу
    pdf_file_path = "/home/ilya/PycharmProjects/dict/articles/статьи на зачет/Фукин_Analysis of the Impact of Atmospheric Models on the Orbit Prediction of Space Debris.pdf"

    # Имя файла для сохранения текста
    output_txt_file = "output/output.txt"

    # Вызываем функцию для конвертации
    pdf_to_text(pdf_file_path, output_txt_file)
