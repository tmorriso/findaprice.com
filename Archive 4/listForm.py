#!/usr/bin/python
import MySQLdb
import cgi, cgitb

cgitb.enable()
print "Content-type: text/html"

print """
<html>
<body>
<h1> Results!</h1>
</body>
</html>
"""	

form = cgi.FieldStorage()
if form.getvalue("category"):
	category = form.getvalue("category")
	print '<h1> The category is: ' + category + '!</h1><br />'
if form.getvalue("subcategory"):
	subcategory = form.getvalue("subcategory")
	print '<h1> The subcategory is: ' + subcategory + '!</h1><br />'
if form.getvalue("service"):
	service = form.getvalue("service")
	print '<h1> The service is: ' + service + '!</h1><br />'
if form.getvalue("company"):
	company = form.getvalue("company")
	print '<h1> The company is: ' + company + '!</h1><br />'
if form.getvalue("price"):
	price = form.getvalue("price")
	print '<h1> The price is: ' + price + '!</h1><br />'
if form.getvalue("rating"):
	rating = form.getvalue("rating")
	print '<h1> The rating is: ' + rating + '!</h1><br />'
if form.getvalue("URL"):
	URL = form.getvalue("URL")
	print '<h1> The URL is: ' + URL + '!</h1><br />'
if form.getvalue("location"):
	location = form.getvalue("location")
	print '<h1> The location is: ' + location + '!</h1><br />'


# Attributes
if form.getvalue("atb_1"):
	atb_1 = form.getvalue("atb_1")
	print '<h1> Attribute 1 is: ' + atb_1 + '!</h1><br />'
if form.getvalue("atb_2"):
	atb_2 = form.getvalue("atb_2")
	print '<h1> Attribute 2 is: ' + atb_2 + '!</h1><br />'
if form.getvalue("atb_3"):
	atb_3 = form.getvalue("atb_3")
	print '<h1> Attribute 3 is: ' + atb_3 + '!</h1><br />'
if form.getvalue("atb_4"):
	atb_4 = form.getvalue("atb_4")
	print '<h1> Attribute 4 is: ' + atb_4 + '!</h1><br />'

  
###############################################
#        Connect to mySQL database 
#
#        Note: This should eventually be in a 
#        seperate file (for security reasons).
###############################################
try:
 db = MySQLdb.connect (
  host = "localhost",
  user = "root",
  passwd = "1234chapo",
  db = "listings")

except MySQLdb.Error, e:
 print "Error %d: %s" % (e.args[0], e.args[1])
 sys.exit (1)

print "connected to the database"
cursor = db.cursor()

# Drop table if it already exist using execute() method. This
# is for testing only
#cursor.execute("DROP TABLE IF EXISTS listings")

# Create table as per requirement
#sql = """CREATE TABLE listings (
#         ID INT,
#        CATEGORY VARCHAR(150),
#         SUB_CATEGORY  VARCHAR(150),
#         SERVICE VARCHAR(150),  
#         COMPANY VARCHAR(150),
#         PRICE FLOAT,
#         RATING INT,
#         URL VARCHAR(150),
#         LOCATION VARCHAR(150),
#         ATB_1 VARCHAR(150),
#         ATB_2 VARCHAR(150),
#         ATB_3 VARCHAR(150),
#         ATB_4 VARCHAR(150) )"""

# cursor.execute(sql)


#############################################
# This is where the inputs are added to
# the listing database.
#############################################
sql = """INSERT INTO LISTINGS(ID, CATEGORY, SUB_CATEGORY, 
         SERVICE, COMPANY, PRICE, RATING, URL, LOCATION, 
         ATB_1, ATB_2, ATB_3, ATB_4) 
         VALUES (1, '%s', '%s', '%s', 
         '%s', 100, '%d', '%s', '%s', 
         '%s', '%s', '%s', '%s')""" % \
         (category, subcategory, service, company, 5, URL,
         	location, atb_1, atb_2, atb_3, atb_4)
        

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

