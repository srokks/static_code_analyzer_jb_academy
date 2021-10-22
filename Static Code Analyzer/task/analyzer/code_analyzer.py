# write your code here
# file_name = input()
file_name = 'test_file.py'
def check_line_lenght(line:str):
    if len(line) > 79:
        return True
def check_indentation(line):
    pass
def check_for_errors(line:str):

    error_list = []
    if check_line_lenght(line):
        error_list.append({'S001':'Too long'})
    if check_indentation(line):
        error_list.append({'S001':'Too long'})
    return error_list
with open(file_name,'r') as f:
    for line_no,line in enumerate(f.readlines(),1):
        error_list = check_for_errors(line)
        if len(error_list) > 0:
            print(error_list)