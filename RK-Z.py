class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Employee:
    def __init__(self, id, name, department_id):
        self.id = id
        self.name = name
        self.department_id = department_id


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


def main():
    # Фильтрация отделов, начинающихся с "А"
    departments_starting_with_A = [
        department for department in departments if department.name.startswith('А')
    ]

    result = {}
    for department in departments_starting_with_A:
        # Поиск сотрудников в соответствующем отделе
        department_employees = [
            employee.name for employee in employees if employee.department_id == department.id
        ]
        result[department.name] = department_employees

    # Вывод результатов
    print('Отделы, начинающиеся с "А", и их сотрудники:')
    for dept, emp_list in result.items():
        print(f'{dept}: {", ".join(emp_list) if emp_list else "нет сотрудников"}')


if __name__ == '__main__':
    main()
