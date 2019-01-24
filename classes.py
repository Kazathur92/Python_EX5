class Company(object):
    # """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

    def get_company_name(self):
        # """Returns the name of the company"""

        return self.company_name

    # Add the remaining methods to fill the requirements above

class Employee:
  def __init__(self, name, age, department, company):
    self.employee_name = name
    self.employee_age = age
    self.employee_department = department
    self.employee_company = company

  def __str__(self):
    return f"{self.employee_name} is a {self.employee_age} year old professional and an Employee of {self.employee_company.get_company_name()} from the {self.employee_department} department"

PythonFury = Company("PythonFury", 2019)
employee1 = Employee("Alfonso Miranda", 26, "Software Development", PythonFury)
employee2 = Employee("Bryan Nilsen", "N/A", "Software Development", PythonFury)
employee3 = Employee("Andy Herring", "N/A", "Software Development", PythonFury)
print(employee1)
print(employee2)
print(employee3)