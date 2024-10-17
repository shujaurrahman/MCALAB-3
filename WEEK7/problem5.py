def calculate_average_salary(employee_file, department_file):
    employees = {}
    with open(employee_file, 'r') as emp_file:
        for line in emp_file:
            name, eid, salary, did = line.strip().split(', ')
            eid, salary, did = int(eid), float(salary), int(did)
            if did not in employees:
                employees[did] = []
            employees[did].append(salary)


    departments = {}
    with open(department_file, 'r') as dept_file:
        for line in dept_file:
            did, dname, dlocation = line.strip().split(', ')
            departments[int(did)] = dname

    average_salaries = {}
    for did, salaries in employees.items():
        average_salaries[departments[did]] = sum(salaries) / len(salaries)

    return average_salaries

employee_file = 'WEEK7/employees.txt'
department_file = 'WEEK7/departments.txt'
average_salaries = calculate_average_salary(employee_file, department_file)

for department, avg_salary in average_salaries.items():
    print(f"Average salary in {department}: Rs: {avg_salary:.2f}")
