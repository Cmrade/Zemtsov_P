class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Employee:
    def __init__(self, id, name, department_id):
        self.id = id
        self.name = name
        self.department_id = department_id


def get_departments_starting_with_A(departments):
    return [department for department in departments if department.name.startswith('А')]


def get_employees_by_department(department, employees):
    return [employee.name for employee in employees if employee.department_id == department.id]


def main(departments, employees):
    departments_starting_with_A = get_departments_starting_with_A(departments)
    result = {}
    
    for department in departments_starting_with_A:
        department_employees = get_employees_by_department(department, employees)
        result[department.name] = department_employees

    print('Отделы, начинающиеся с "А", и их сотрудники:')
    for dept, emp_list in result.items():
        print(f'{dept}: {", ".join(emp_list) if emp_list else "нет сотрудников"}')


if __name__ == '__main__':
    # Примеры данных
    departments = [
        Department(1, 'Отдел продаж'),
        Department(2, 'Отдел разработки'),
        Department(3, 'Аналитический отдел'),
        Department(4, 'Отдел маркетинга'),
    ]

    employees = [
        Employee(1, 'Иван', 3),
        Employee(2, 'Светлана', 1),
        Employee(3, 'Александр', 3),
        Employee(4, 'Мария', 2),
        Employee(5, 'Анастасия', 3),
    ]

    main(departments, employees)
