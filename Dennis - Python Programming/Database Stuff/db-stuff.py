# step 1 -> import sqlite3
# step 2 -> create a connection object (connection to the db)
# step 3 -> create cursor - cursor allows you to execute queries
# step 4 -> execute the queries
# step 5 -> commit changes - save changes you've made to the disk
# step 6 -> close the connection


# demo:
import sqlite3


def create_table():
    # create a connection
    connection = sqlite3.connect("data.db")

    # create a cursor
    cursor = connection.cursor()

    # create your statements/queries
    query = "CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY NOT NULL UNIQUE, name TEXT, address TEXT, age INTEGER)"

    # execute statements
    cursor.execute(query)

    # commit changes
    connection.commit()

    # close the connection
    connection.close()


def insert_data():
    # create a connection
    connection = sqlite3.connect("data.db")
    # create a cursor
    cursor = connection.cursor()
    # create your statements/queries
    query = "INSERT INTO customers (id,name,address,age) VALUES(?, ?, ?, ?)"
    data = (105, 'Web Developer', 'Taveta', 22)
    # execute query
    cursor.execute(query, data)
    # commit changes
    connection.commit()
    # close the connection
    connection.close()


def update_data():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    # recommended way
    query = "UPDATE customers SET address = ? WHERE id = ?"
    # not recommended
    # address = 'Kiambu, Kenya'
    # id = 102
    # query = f"UPDATE customers SET address = '{address}' WHERE id = {id}"
    cursor.execute(query, ('Kenya', 100))
    connection.commit()
    connection.close()


def delete_data():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "DELETE FROM customers WHERE id = ?"
    cursor.execute(query, (100,))
    connection.commit()
    connection.close()


def read_all_data():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    syntax = 'SELECT column_name(s) FROM table_name WHERE column_name = some_value'
    query = "SELECT * FROM customers"
    cursor.execute(query)
    customers = cursor.fetchall()

    with open('customers.txt', 'w') as file:
        for customer in customers:
            file.write(f"{customer[0]},{customer[1]},{customer[2]},{customer[3]}\n")

    for idx, customer in enumerate(customers, start=1):
        print(f"{idx}. {customer[0]} {customer[1]} {customer[2]} {customer[3]}")
    connection.close()


def read_single_record():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    query = "SELECT id, address, age FROM customers WHERE id = 102"
    cursor.execute(query)
    record = cursor.fetchone()
    return record


def read_many_records():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    query = "SELECT id, address, age FROM customers"
    cursor.execute(query)
    record = cursor.fetchmany(4)
    return record


# create_table()
# insert_data()
# update_data()
# delete_data()
# read_all_data()
print(read_many_records())
# CRUD
# C - Create
# R - Retrieve/read
# U - Update
# D - Delete
