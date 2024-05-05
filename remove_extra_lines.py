def remove_extra_newlines(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    cleaned_lines = '\n'.join(line.strip() for line in lines if line.strip())

    with open(output_file_path, 'w') as output_file:
        output_file.write(cleaned_lines)


input_file_path = 'words_thinned.txt'
output_file_path = 'words_thinned_wo_lines.txt'
remove_extra_newlines(input_file_path, output_file_path)
