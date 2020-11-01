import sqlite3
import os

persons = [
    ("Hugo", "Boss"),
    ("Calvin", "Klein")
    ]

con = sqlite3.connect("shorcutDB.db")

# Create the table
con.execute("CREATE TABLE if not exists person(firstname, lastname)")

# Fill the table
con.executemany("INSERT INTO person(firstname, lastname) VALUES (?, ?)", persons)

# Print the table contents
for row in con.execute("SELECT firstname, lastname FROM person"):
    print(row)

# print("I just deleted", con.execute("DELETE FROM person").rowcount, "rows")

test1 = input("-->")
test2 = input("-->")

test = [(test1, test2)]

con.executemany("INSERT INTO person(firstname, lastname) VALUES (?, ?)", test)
print("---------------------")
for row in con.execute("SELECT firstname, lastname FROM person"):
    print(row)

# close is not a shortcut method and it's not called automatically,
# so the connection object should be closed manually
con.close()


os.system("pause")