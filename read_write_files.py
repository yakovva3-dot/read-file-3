def print_file_content(filename):
    with open(filename, 'r') as f:
        print(f.read())

def create_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dst:
        dst.write(src.read())

def count_lines(filename):
    with open(filename, 'r') as f:
        return len(f.readlines())

def count_word_occurrence(filename, word):
    with open(filename, 'r') as f:
        return f.read().count(word)

def py_to_txt(filename):
    new_filename = filename.replace('.py', '.txt')
    with open(filename, 'r') as src, open(new_filename, 'w') as dst:
        dst.write(src.read())

def replace_text_in_file(filename, search_str, replace_str):
    with open(filename, 'r') as f:
        content = f.read()
    content = content.replace(search_str, replace_str)
    with open(filename, 'w') as f:
        f.write(content)

def append_lines(filename, lines_list):
    with open(filename, 'a') as f:
        for line in lines_list:
            f.write(line + '\n')

def count_functions(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            if line.strip().startswith('def '):
                count += 1
    return count

def merge_files(file_list, destination):
    with open(destination, 'w') as dest:
        for filename in file_list:
            with open(filename, 'r') as src:
                dest.write(src.read())
                dest.write('\n\n')