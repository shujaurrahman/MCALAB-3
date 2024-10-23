def number_of_courses(filename):
    program_course={}

    with open(filename,'r') as file:
        for line in file:
            program=line.strip().split(',')[0]

            if program in program_course:
                program_course[program]+=1
            else:
                program_course[program]=1
    
    return program_course

program_course=number_of_courses('WEEK9/courses.txt')
print(program_course)