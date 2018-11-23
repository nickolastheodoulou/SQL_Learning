import sqlite3
from Resource2.employee import Employee

# creates the data base in memory
conn = sqlite3.connect(':memory:')

c = conn.cursor()

# create a table called employees with 3 columns, first, last, pay
c.execute("""CREATE TABLE employees(
    first text,
    last text,
    pay integer
    )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO  employees VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
        # bad practice to insert python variables using this method
        #  c.execute("INSERT INTO  employees VALUES ('{}', '{}', '{}')".format(emp_1.first, emp_1.last, emp_1.pay))

        # other correct method that doesnt allow connection injection
        # c.execute("INSERT INTO  employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last =:last ", {'last': lastname})
    # other method to select names
    # c.execute("SELECT * FROM employees WHERE last =?", ('Schafer',))
    return  c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)


update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

'''
emps = get_emps_by_name('Doe')
print(emps)
'''

conn.close()
