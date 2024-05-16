def remove_extra_newlines_and_sort(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    words = [word.strip() for word in lines if word.strip()]

    sorted_words = sorted(words)

    with open(output_file_path, 'w') as output_file:
        for word in sorted_words:
            output_file.write(word + '\n')


if __name__ == "__main__":
    input_file_path = 'words.txt'
    output_file_path = 'words_radmir_thinned.txt'
    remove_extra_newlines_and_sort(input_file_path, output_file_path)
