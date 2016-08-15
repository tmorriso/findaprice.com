#!/usr/bin/python
import MySQLdb
import cgi, cgitb

cgitb.enable()
print "Content-type: text/html"

print """
<html>
<body>
</body>
</html>
"""	

form = cgi.FieldStorage()
if form.getvalue("search"):
	search = form.getvalue("search")
	print '<h1> Searching For: ' + search + '!</h1><br />'


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

#############################################
# Stage 1:
# This is where the item being searched will
# query the listing database.
#  1. Search listings table (Services (this will include more eventually))
#  2. Return the ID number. 
#  3. Display the corresponding information
#     for the ID number.
#############################################
# Stage 2;
# After stage 1, stage 2 is to enable multiple
# matches to the search query.
#  1. Search the listings table (services)
#  2. Return the ID numbers
#  3. Display the corresponding values to 
#     the information corresponding to the
#     matches.
#############################################
# Stage 3;
# After stage 2, stage 3 is to add filtering
# capabilities (price). 
#  1. Retrieve price value for each ID
#  2. If staments to order the results
#     (Eventually this will be replaced with
#       merge sort or better)
#  4. Display the results in order.
#############################################
# Stage 4;
# After stage 3, stage 4 is to enable filtering
# by attributes. (Combination of searching several
# values in the table)
#
#############################################

sql = """ SELECT * FROM listings WHERE 
			CATEGORY LIKE "%DOGS%" """ 

        
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   # db.commit()
   for (CATEGORY) in cursor:
  	print(" The category is: {}".format(
    	CATEGORY))

except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

############################################
# Display the Results (this could be a new
# page)
#
#
############################################
