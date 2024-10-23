def read_file(filename):
    with open(filename,'r') as file:
        return file.readlines()

def write_file(filename,lines):
    with open(filename,'w') as file:
        file.writelines(lines)

def add_HRA(filename):
    lines=read_file(filename)

    first_line=lines[0].strip() + ',HRA\n'
    new_lines=[first_line]

    for i in range(1,len(lines)):
        parts=lines[i].strip().split(',')
        salary=int(parts[2])
        HRA=0.18*salary
        new_line=f"{parts[0]},{parts[1]},{parts[2]},{parts[3]},{HRA:.2f}\n"
        new_lines.append(new_line)

    write_file('WEEK9/hra_week9_prob5.txt',new_lines)
    print("File saved as WEEK9/hra_week9_prob5.txt")

add_HRA('WEEK9/file_week9_problem7.txt')