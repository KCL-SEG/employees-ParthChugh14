"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
    def get_pay(self):
        pass
    def __str__(self):
        return self.name

class Monthly_Employee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return super().__str__() + f" works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."

class Hourly_Employee(Employee):
    def __init__(self, name, hours, sal_per_hour):
        super().__init__(name)
        self.hours = hours
        self.sal_per_hour = sal_per_hour
    
    def get_pay(self):
        return self.hours * self.sal_per_hour

    def __str__(self):
        return super().__str__() + f" works on a contract of {self.hours} hours at {self.sal_per_hour}/hour. Their total pay is {self.get_pay()}."

class Monthly_Contract_Employee(Monthly_Employee):
    def __init__(self, name, salary, num_of_contracts, sal_per_contract):
        super().__init__(name, salary)
        self.num_of_contracts = num_of_contracts
        self.sal_per_contract = sal_per_contract

    def get_pay(self):
        return super().get_pay() + (self.num_of_contracts * self.sal_per_contract)
    
    def __str__(self):
        return super().__str__().replace(f". Their total pay is {self.get_pay()}", f" and receives a commission for {self.num_of_contracts} contract(s) at {self.sal_per_contract}/contract. Their total pay is {self.get_pay()}")

class Hourly_Contract_Employee(Hourly_Employee):
    def __init__(self, name, hours, sal_per_hour, num_of_contracts, sal_per_contract):
        super().__init__(name, hours, sal_per_hour)
        self.num_of_contracts = num_of_contracts
        self.sal_per_contract = sal_per_contract

    def get_pay(self):
        return super().get_pay() + (self.num_of_contracts * self.sal_per_contract)
    
    def __str__(self):
        return super().__str__().replace(f". Their total pay is {self.get_pay()}", f" and receives a commission for {self.num_of_contracts} contract(s) at {self.sal_per_contract}/contract. Their total pay is {self.get_pay()}")


class Monthly_Fixed_Employee(Monthly_Employee):
    def __init__(self, name, salary, fixed_commission):
        super().__init__(name, salary)
        self.fixed_commission = fixed_commission

    def get_pay(self):
        return super().get_pay() + self.fixed_commission
    
    def __str__(self):
        return super().__str__().replace(f". Their total pay is {self.get_pay()}", f" and receives a bonus commission of {self.fixed_commission}. Their total pay is {self.get_pay()}")


class Hourly_Fixed_Employee(Hourly_Employee):
    def __init__(self, name, hours, sal_per_hour, fixed_commission):
        super().__init__(name, hours, sal_per_hour)
        self.fixed_commission = fixed_commission
    
    def get_pay(self):
        return super().get_pay() + self.fixed_commission
    
    def __str__(self):
        return super().__str__().replace(f". Their total pay is {self.get_pay()}", f" and receives a bonus commission of {self.fixed_commission}. Their total pay is {self.get_pay()}")

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Monthly_Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Employee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Monthly_Contract_Employee('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly_Contract_Employee('Jan', 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Monthly_Fixed_Employee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly_Fixed_Employee('Ariel', 120, 30, 600)