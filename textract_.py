# import os
#
# import textract
#
#
# def pdf_to_txt(pdf_path):
#     """
#     Конвертирует PDF-файл в текстовый файл.
#
#     :param pdf_path: Путь к PDF-файлу.
#     """
#
#     try:
#         return textract.process(pdf_path).decode('utf-8')
#     except Exception as e:
#         print(f"Ошибка при конвертации PDF в текст: {e}")
#
#
# def process_articles(input_dir):
#     # Создаем пустую строку для объединения текста из всех статей
#     combined_text = ""
#
#     # Проходим по всем файлам в директории
#     for filename in os.listdir(input_dir):
#         if filename.endswith(".pdf"):
#             # Получаем путь к файлу
#             file_path = os.path.join(input_dir, filename)
#
#             # Преобразуем PDF в текст и добавляем его к общему тексту
#             article_text = pdf_to_txt(file_path)
#             if article_text:
#                 combined_text += article_text
#
#     return combined_text
#
#
# if __name__ == "__main__":
#     # Путь к директории с PDF файлами
#     input_dir = "/home/fukin/github_projects/dictionary/articles_radmir"
#
#     # Обрабатываем все статьи
#     combined_text = process_articles(input_dir)
#
#     # Путь для сохранения объединенного текста
#     output_txt_file = "articles_radmir.txt"
#     #
#     # os.makedirs("output")
#
#     # Сохраняем объединенный текст в файл
#     with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
#         txt_file.write(combined_text)
#
#     print("Все статьи успешно сконвертированы в один TXT файл.")
