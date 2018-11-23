import sqlite3
import csv

my_file = open('iris.txt', 'r')  # open the csv data file
# next(my_file, None)  # skip the header row if applicable
reader = csv.reader(my_file)

connection = sqlite3.connect('iris.db')
cursor = connection.cursor()

# create the table if it doesn't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS iris
            (sepal_length DECIMAL, sepal_width DECIMAL, petal_length DECIMAL, petal_width DECIMAL, class integer)''')


for row in reader:
    cursor.execute("INSERT INTO iris VALUES (?, ?, ?, ?, ?)", row)

my_file.close()
connection.commit()
connection.close()
