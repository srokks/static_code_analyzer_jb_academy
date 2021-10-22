# write your code here
# file_name = input()
file_name = 'test_file.py'


def check_line_lenght(line: str):
    if len(line) > 79:
        return True


def check_indentation(line):
    pass


def check_spaces_before(line):
    pass


def check_semicol_end(line):
    pass


def todo_found(line):
    pass


def check_blank_preciding(line):
    pass


def check_for_errors(line: str):
    error_list = []
    if check_line_lenght(line):
        error_list.append({'S001': 'Too long'})
    if check_indentation(line):
        error_list.append({'S002': 'Indentation is not a multiple of four;'})
    if check_semicol_end(line):
        error_list.append({'S003': 'Unnecessary semicolon after a statement (note that semicolons are acceptable in '
                                   'comments);'})
    if check_spaces_before(line):
        error_list.append({'S004': 'Less than two spaces before inline comments;'})
    if todo_found(line):
        error_list.append({'S005': 'TODO found (in comments only and case-insensitive);'})
    if check_blank_preciding(line):
        error_list.append({'S006': "More than two blank lines preceding a code line (applies to the first "
                                   "non-empty line)."})

    return error_list


with open(file_name, 'r') as f:
    for line_no, line in enumerate(f.readlines(), 1):
        error_list = check_for_errors(line)
        if len(error_list) > 0:
            print(f"Line {line_no}:", error_list)
