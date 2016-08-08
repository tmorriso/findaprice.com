#import MySQLdb
# Old stuff
#conn = MySQLdb.connect("localhost","root","1234chapo","listings")


print "Content-type:text/html\n\n"
import MySQLdb
import sys

try:
 conn = MySQLdb.connect (
  host = "localhost",
  user = "root",
  passwd = "1234chapo",
  db = "listings")

except MySQLdb.Error, e:
 print "Error %d: %s" % (e.args[0], e.args[1])
 sys.exit (1)

print "connected to the database"
c = conn.cursor()

c.execute("SELECT * FROM houseChores")

rows = c.fetchall()

for eachRow in rows:
	print eachRow

#######################Bunch a crap####################
#!/usr/bin/python
import MySQLdb
import cgi, cgitb

form = cgi.FieldStorage()

name = form.getvalue('name')
email = form.getvalue('email')
plate = form.getvalue('plate')

# Avoid script injection escaping the user input
name = cgi.escape(name)
email = cgi.escape(email)
plate = cgi.escape(plate)

db = MySQLdb.connect(host="mysql.example.com", port=3306, user="l", passwd="l", db="l")
cursor = db.cursor()

add_driver = ("INSERT INTO Users "
           "(UsersName, UsersEmail, UsersPlate) "
           "VALUES (%s, %s, %s)")

cursor.execute(add_driver, (name, email, plate))
db.commit()
cursor.close()
db.close()

print "Content-type: text/html\n\n"
print 
print """\
