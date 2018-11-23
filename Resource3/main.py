import sqlite3
import csv

f = open('iris.txt', 'r')  # open the csv data file
next(f, None)  # skip the header row
reader = csv.reader(f)

sql = sqlite3.connect('iris.db')
cur = sql.cursor()

# create the table if it doesn't already exist
cur.execute('''CREATE TABLE IF NOT EXISTS utterances
            (sepal_length DECIMAL, sepal_width DECIMAL, petal_length DECIMAL, petal_width DECIMAL, class integer)''')

for row in reader:
    cur.execute("INSERT INTO utterances VALUES (?, ?, ?, ?, ?)", row)

f.close()
sql.commit()
sql.close()
