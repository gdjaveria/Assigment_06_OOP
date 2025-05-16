# 4. Class Variables and Class Methods
 # Assignment:
# Create a class Bank with a class variable bank_name. 
# Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# Show that it affects all instances.

class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Create instances of Bank
b1 = Bank()
print(b1.bank_name)
Bank.change_bank_name("XYZ Bank")
print(b1.bank_name)  # Accessing the class variable through an instance
        

