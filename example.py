import mysql.connector

con = mysql.connector.connect(
    user = "root",
    password = "Debashish@902",
    host = "localhost",
    port = 3306,
    database = "giet"
)

if con.is_connected():
    print("connected")

cur = con.cursor()
cur.execute("SHOW DATABASES")
for x in cur:
    print(x)

print("\n")

cur.execute("SHOW TABLES")
for Y in cur:
    print(Y)
print("\n")
#Q.1
cur.execute("SELECT * FROM gietu")
print("Q.1")
for Y in cur:
    print(Y)
print("\n")
#Q.2
cur.execute("select name from Gietu")
print("Q.2")
for Y in cur:
    print(Y)
print("\n")
#Q.3
cur.execute("select name from Gietu")
print("Q.3")
for Y in cur:
    print(Y)
print("\n")
#Q.4
cur.execute("select name,address from Gietu")
print("Q.4")
for Y in cur:
    print(Y)
print("\n")
#Q.5
cur.execute("select roll,salary from Gietu")
print("Q.5")
for Y in cur:
    print(Y)
print("\n")
#Q.6
cur.execute("select name from gietu where name = 'aman'")
print("Q.6")
for Y in cur:
    print(Y)
print("\n")
#Q.7
cur.execute("select name from Gietu where address = 'delhi'")
print("Q.7")
for Y in cur:
    print(Y)
print("\n")
#Q.8
cur.execute("select name from Gietu where gender = 'M'")
print("Q.8")
for Y in cur:
    print(Y)
print("\n")
#Q.9
cur.execute(" select name from Gietu where desig = 'doctor'")
print("Q.9")
for Y in cur:
    print(Y)
print("\n")
#Q.10
cur.execute("select name from Gietu where salary>15000")
print("Q.10")
for Y in cur:
    print(Y)
print("\n")
#Q.11
cur.execute("select name from Gietu where salary>20000")
print("Q.11")
for Y in cur:
    print(Y)
print("\n")
#Q.12
cur.execute("select name from Gietu where salary<30000")
print("Q.12")
for Y in cur:
    print(Y)
print("\n")
#Q.13
cur.execute("select name from Gietu where gender = 'M' and salary>20000")
print("Q.13")
for Y in cur:
    print(Y)
print("\n")
#Q.14
cur.execute("select name from Gietu where gender = 'F' or address = 'raipur'")
print("Q.14")
for Y in cur:
    print(Y)
print("\n")
#Q.15
cur.execute("select * FROM gietu WHERE LOWER(name) LIKE 'a%'")
print("Q.15")
for Y in cur:
    print(Y)
print("\n")
#Q.16
cur.execute("select * FROM gietu WHERE LOWER(name) LIKE '%h'")
print("Q.16")
for Y in cur:
    print(Y)
print("\n")
#Q.17
cur.execute("select * FROM gietu WHERE LOWER(address) LIKE '%pur%'")
print("Q.17")
for Y in cur:
    print(Y)
print("\n")
#Q.18
cur.execute("select * from gietu order by name asc")
print("Q.18")
for Y in cur:
    print(Y)
print("\n")
#Q.19
cur.execute("select * from gietu order by name desc")
print("Q.19")
for Y in cur:
    print(Y)
print("\n")
#Q.20
cur.execute("select count(*) as total_employees from gietu")
print("Q.20")
for Y in cur:
    print(Y)
print("\n")
#Q.21
cur.execute("select count(*) as total_male from gietu where gender = 'M'")
print("Q.21")
for Y in cur:
    print(Y)
print("\n")

cur.close()
con.close()