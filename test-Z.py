import unittest

class TestDepartmentEmployeeFunctions(unittest.TestCase):

    def setUp(self):
        self.departments = [
            Department(1, 'Отдел продаж'),
            Department(2, 'Отдел разработки'),
            Department(3, 'Аналитический отдел'),
            Department(4, 'Отдел маркетинга'),
        ]
        self.employees = [
            Employee(1, 'Иван', 3),
            Employee(2, 'Светлана', 1),
            Employee(3, 'Александр', 3),
            Employee(4, 'Мария', 2),
            Employee(5, 'Анастасия', 3),
        ]

    def test_get_departments_starting_with_A(self):
        result = get_departments_starting_with_A(self.departments)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'Аналитический отдел')

    def test_get_employees_by_department(self):
        department = self.departments[2]  # Аналитический отдел
        result = get_employees_by_department(department, self.employees)
        self.assertEqual(len(result), 3)
        self.assertIn('Иван', result)
        self.assertIn('Александр', result)
        self.assertIn('Анастасия', result)

if __name__ == '__main__':
    unittest.main()
