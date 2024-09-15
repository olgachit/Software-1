import mysql.connector
connection = mysql.connector.connect(
    user="olgachit",
    password="OLga123!",
    host="localhost",
    port=3306,
    database="relationaldatabases",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)
print("connected successfully")

def get_employees_by_last_name(last_name):
    sql=f"SELECT Number, LastName, FirstName, Salary FROM employee1 WHERE LastName='{last_name}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0:
        for row in result:
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    return

connection=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='relationaldatabases',
    user='olgachit',
    password='OLga123!',
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
    )
last_name=input("Enter last name: ")
get_employees_by_last_name(last_name)
