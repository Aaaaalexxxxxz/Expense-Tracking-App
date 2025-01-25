#installed mysql
#install mysql connector/python


import mysql.connector

database = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "20050807"
)

curserObject = database.cursor()

curserObject.execute("CREATE DATABASE expenseapp")

print("Expense app database created successfully...")