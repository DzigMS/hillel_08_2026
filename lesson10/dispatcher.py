class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        # super().__init__(self, name, salary)
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

print(TeamLead.mro())
print(Manager.mro())

team_lead = TeamLead('Sergey', 1000, 'Dev', 'Python', 2)
# team_lead = TeamLead.__init__('Sergey', 1000, 'Dev', 'Python', 2)
# print(team_lead.name, team_lead.salary, team_lead.department, team_lead.programming_language, team_lead.team_size)
# manager = Manager("Jora", 1000, 'Director')

print(f'class {team_lead.__class__.__name__}')
print(f'class {type(team_lead).__name__}')

