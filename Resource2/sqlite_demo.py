import sqlite3
from Resource2.employee import Employee

# creates the data base
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# create a table called employees with 3 columns, first, last, pay
'''
c.execute("""CREATE TABLE employees(
    first text,
    last text,
    pay integer
    )""")
'''

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

print(emp_1.first)

# bad practice to insert python variables using this method
#  c.execute("INSERT INTO  employees VALUES ('{}', '{}', '{}')".format(emp_1.first, emp_1.last, emp_1.pay))

# correct method that doesnt allow sql injection
# c.execute("INSERT INTO  employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

# other correct method using a dictionary instead of a tuple
# c.execute("INSERT INTO  employees VALUES (:first, :last, :pay)",
#          {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

# inserts a column into the table once it has been created
# c.execute("INSERT INTO employees VALUES('Corey', 'Schafer',50000) ")
# c.execute("INSERT INTO employees VALUES('Mary', 'Schafer',70000) ")
# conn.commit()

# method to select names
c.execute("SELECT * FROM employees WHERE last =?", ('Schafer',))
print(c.fetchall())

# other method to select names
c.execute("SELECT * FROM employees WHERE last =:last ", {'last': 'Doe'})
# print all values
print(c.fetchall())


# prints one value
# print(c.fetchone())

conn.commit()

# close connection to the database
conn.close()
