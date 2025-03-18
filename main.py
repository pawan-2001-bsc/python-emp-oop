from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name, department):
        self._employee_id = employee_id
        self._name = name
        self._department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print("\n--- Employee Details ---")
        print(f"Employee ID: {self._employee_id}")
        print(f"Name: {self._name}")
        print(f"Department: {self._department}")

class PermanentEmployee(Employee):
    def __init__(self, employee_id, name, department, basic_salary, bonus):
        super().__init__(employee_id, name, department)
        self.__basic_salary = basic_salary
        self.__bonus = bonus

    def calculate_salary(self):
        return self.__basic_salary + self.__bonus

    def display_details(self):
        super().display_details()
        print(f"Basic Salary: ${self.__basic_salary:.2f}")
        print(f"Bonus: ${self.__bonus:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")

class ContractEmployee(Employee):
    def __init__(self, employee_id, name, department, hourly_rate, hours_worked):
        super().__init__(employee_id, name, department)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked

    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: ${self.__hourly_rate:.2f}")
        print(f"Hours Worked: {self.__hours_worked}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")

class Intern(Employee):
    def __init__(self, employee_id, name, department, stipend):
        super().__init__(employee_id, name, department)
        self.__stipend = stipend

    def calculate_salary(self):
        return self.__stipend

    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self.__stipend:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")

emp1 = PermanentEmployee("P123", "Alice Johnson", "IT", 60000, 5000)
emp2 = ContractEmployee("C456", "Bob Smith", "HR", 50, 160)
emp3 = Intern("I789", "Charlie Brown", "Finance", 1500)

emp1.display_details()
emp2.display_details()
emp3.display_details()

