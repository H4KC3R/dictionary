def create_custom_dictionary(txt_file_path, output_dict_file):
    # Создаем пустой словарь для хранения переводов
    custom_dictionary = {}

    # Читаем текст из файла
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        text = txt_file.read()

    # Разбиваем текст на отдельные слова
    words = text.split()

    # Извлекаем уникальные слова
    unique_words = set(words)

    # Определяем переводы для каждого слова
    for word in unique_words:
        translation = input(f"Введите перевод для слова '{word}': ")
        custom_dictionary[word] = translation
        if translation == "AAA":
            break

    # Сохраняем словарь в файл
    with open(output_dict_file, 'w', encoding='utf-8') as dict_file:
        for word, translation in custom_dictionary.items():
            dict_file.write(f"{word}: {translation}\n")

    print("Кастомный словарь успешно создан и сохранен.")


if __name__ == "__main__":
    # Путь к файлу с текстом
    txt_file_path = "text.txt"

    # Путь для сохранения кастомного словаря
    output_dict_file = "custom_dictionary.txt"

    # Создаем кастомный словарь
    create_custom_dictionary(txt_file_path, output_dict_file)