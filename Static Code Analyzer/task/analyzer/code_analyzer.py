# write your code here
import re



def check_line_lenght(line: str):
    '''
    Returns True if line is longer than 79
    '''
    if len(line) > 79:
        return True


def check_indentation(line):
    '''
    Returns true if indentation in line is not a multiple of four; i
    '''
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
    if "#" in line and line[0]!='#':
        line = line.split('#')[0]
        if line[-2:] != '  ':
            return True


def check_semicol_end(line):
    '''
    Returns True if code line ends with ;
    '''
    if '#' in line and line[0] != '#':
        line = line.split('#')[0].rstrip(' ')
        if line[-1] == ';':
            return True
    else:
        if line[0] != '#':
            if line.rstrip(' ')[-1] == ';':
                return True


def todo_found(line):
    if '#' in line:
        line = line.split('#')[1].lower()
        if 'todo' in line:
            return True


def check_blank_preciding(line):
    error_list = []

    error_list.append({'S006': "More than two blank lines used before this line"})
    return error_list


def check_for_errors(line: str, prev_blanks_error=False):
    error_list = []
    if len(line) == 0:
        pass
    else:
        if check_line_lenght(line):
            error_list.append(['S001', 'Too long'])
        if check_indentation(line):
            error_list.append(['S002', 'Indentation is not a multiple of four;'])
        if check_semicol_end(line):
            error_list.append(['S003', 'Unnecessary semicolon'])
        if check_spaces_before_comment(line):
            error_list.append(['S004', 'Less than two spaces before inline comments'])
        if todo_found(line):
            error_list.append(['S005', 'TODO found'])
        if prev_blanks_error:
            error_list.append(['S006', 'More than two blank lines used before this line'])
    return error_list

def print_errors(file_name):
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

# file_name = input()
# file_name = 'test1.py'  #DEBUG

if __name__ == '__main__':
    import sys
    import os
    args = sys.argv
    path = args[1]
    files_list = []
    if os.path.isdir(path):
        for el in sorted(os.listdir(path)): # FIXME: without recoursive scan
            if el[-3:] == '.py':
                files_list.append(path+'/'+el)
    elif os.path.isfile(path):
        if path[-3:] == '.py':
            files_list.append(path)
    for el in files_list:
        print_errors(el)
    # print(files_list)