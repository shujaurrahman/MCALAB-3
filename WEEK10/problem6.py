import csv

def merge_files(employee_file,department_file,output_file):
    department_data={}

    with open(department_file,'r') as dept_file:
        reader=csv.reader(dept_file)
        for row in reader:
            DID, DName, DLocation=row
            department_data[DID]={'DName' : DName, 'DLocation' : DLocation}

    with open(employee_file,'r') as emp_file, open(output_file,'w',newline='') as out_file:
        emp_reader=csv.reader(emp_file)
        writer=csv.writer(out_file)

        writer.writerow(['Ename','EId','Esalary','EDID','DName',"DLocation"])

        for row in emp_reader:
            Ename,EId,Esalary,EDID = row
            if EDID in department_data:
                DName=department_data[EDID]['DName']
                DLocation=department_data[EDID]['DLocation']
                writer.writerow([Ename,EId,Esalary,EDID,DName,DLocation])
        
    print("File merged successfully as per the requirement.")

employee_file='WEEK10/week10_prob6_employee.txt'
department_file='WEEK10/week10_prob6_department.txt'
output_file='WEEK10/week10_prob6_output.txt'

merge_files(employee_file,department_file,output_file)