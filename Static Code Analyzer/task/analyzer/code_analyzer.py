# write your code here
# file_name = input()
file_name = 'test_file.py'

with open(file_name,'r') as f:
    for line_no,line in enumerate(f.readlines(),1):
        if len(line)>79:
            print(f"Line {line_no}: S001 Too long")
