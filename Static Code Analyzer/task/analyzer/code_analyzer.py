# write your code here
import ast
import re


def check_line_length(line: str):
    """
    Returns True if line is longer than 79
    """
    if len(line) > 79:
        return True


def check_indentation(line):
    """
    Returns true if indentation in line is not a multiple of four; i
    """
    i = 0
    while True:
        if line[i] == ' ':
            i += 1
        else:
            break
    if i == 0 or i % 4 == 0:
        return False
    else:
        return True


def check_spaces_before_comment(line):
    """
    Returns True if there's less than two spaces before inline comments
    """
    if "#" in line and line[0] != '#':
        line = line.split('#')[0]
        if line[-2:] != '  ':
            return True


def check_semicolon_end(line):
    """
    Returns True if code line ends with ;
    """
    if '#' in line and line[0] != '#':
        line = line.split('#')[0].rstrip(' ')
        if line[-1] == ';':
            return True
    else:
        if line[0] != '#':
            if line.rstrip(' ')[-1] == ';':
                return True


def todo_found(line):
    """
    Returns True if #TODO: found
    """
    if '#' in line:
        line = line.split('#')[1].lower()
        if 'todo' in line:
            return True


def spaces_after_class(line):
    if re.match('class', line):
        if not re.match('class \w', line):
            return True


def spaces_after_def(line: str):
    line = line.lstrip(' ')
    if re.match('def', line):
        if not re.match('def \w', line):
            return True


def class_camel_check(line):
    if re.match('class', line):
        class_name = line[:-1].split()[-1]
        if not re.match('^[A-Z][A-Za-z()]*', class_name):
            return class_name


def function_snake_check(line):
    line = line.lstrip(' ')
    if re.match('def', line):
        def_name = line.split(' ')[1]
        if not re.match('^[a-z_][a-z_0-9]*.*$', def_name):
            return def_name


def check_for_errors(line: str, prev_blanks_error=False):
    """
    Checks line for errors and returns errors_list
    """
    error_list = []
    if len(line) == 0:
        pass
    else:
        if check_line_length(line):
            error_list.append(['S001', 'Too long'])
        if check_indentation(line):
            error_list.append(['S002', 'Indentation is not a multiple of four;'])
        if check_semicolon_end(line):
            error_list.append(['S003', 'Unnecessary semicolon'])
        if check_spaces_before_comment(line):
            error_list.append(['S004', 'Less than two spaces before inline comments'])
        if todo_found(line):
            error_list.append(['S005', 'TODO found'])
        if prev_blanks_error:
            error_list.append(['S006', 'More than two blank lines used before this line'])
        if spaces_after_class(line):
            error_list.append(['S007', "Too many spaces after 'class'"])
        if spaces_after_def(line):
            error_list.append(['S007', "Too many spaces after 'def'"])
        class_name = class_camel_check(line)
        if class_name:
            error_list.append(['S008', f"Class name '{class_name}' should use CamelCase"])
        def_name = function_snake_check(line)
        if def_name:
            error_list.append(['S009', f"Function name '{def_name}' should use snake_case"])



    return error_list


def print_errors(file_name):
    """
    With given file_name checks py file for PEP errors
    """
    with open(file_name, 'r') as f:
        blank_counter = 0
        for line_no, line in enumerate(f.read().splitlines(), 1):
            if blank_counter > 2 and line != '':
                error_list = check_for_errors(line, True)
            else:
                error_list = check_for_errors(line, False)
            if line == '':
                blank_counter += 1
            else:
                blank_counter = 0

            if len(error_list) > 0:
                for err_code, err_desc in error_list:
                    print(f'{file_name}: Line {line_no}: {err_code} {err_desc}')
                pass


def check_files(path):
    files_list = []
    if os.path.isdir(path):
        for el in sorted(os.listdir(path)):  # FIXME: without recursively scan
            if el[-3:] == '.py':
                files_list.append(path + '/' + el)
    elif os.path.isfile(path):
        if path[-3:] == '.py':
            files_list.append(path)
    for el in files_list:
        print_errors(el)


def check_args_snake(file_name):
    """
    Returns list with line numbers where error occured
    """
    with open(file_name, 'r') as f:
        script = f.read()
    tree = ast.parse(script)
    line_numbers = []
    for node in ast.walk(tree):
        if isinstance(node, ast.arg):
            arg_name = node.arg
            if not re.match('^[a-z_][a-z_0-9]*.*$', arg_name):
                line_numbers.append({'line_no':node.lineno,'arg_name':arg_name})
    return line_numbers


# file_name = input()
# file_name = 'test1.py'  #DEBUG


if __name__ == '__main__':
    import sys
    import os

    args = sys.argv
    path = args[1]
    check_files(path)
    # a =check_args_snake('/Users/srokks/PycharmProjects/Static Code Analyzer/Static Code Analyzer/task/analyzer/tests/test.py')
    # print(a)