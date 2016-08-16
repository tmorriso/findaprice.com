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
	#print '<h1> Searching For: ' + search + '!</h1><br />'


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

sql = """ SELECT * FROM listings WHERE \
		  CATEGORY = '%s' """ % \
		  (search)
			

        
try:
   # Execute the SQL command
   cursor.execute(sql)
   
   # Display Results
   results = cursor.fetchall()

   # Display number of results found	  
   print '<h1>' + str(cursor.rowcount) + ' Result(s) Found!</h1><br />'
   
   # Display values
   for row in results:
   	print '<h2> The category is:' + row[1] + '!</h2><br />'
   	print '<h2> The Subcategory is:' + row[2] + '!</h2><br />'
   	print '<h2> The service is:' + row[3] + '!</h2><br />'
   	print '<h2> The company is:' + row[4] + '!</h2><br />'
	# Link to website 
   	print '<a href= %s >Go to website</a>' % (row[7])


except:
   # Rollback in case there is any error
   db.rollback()
   print ("Error: unable to fetch data")
# disconnect from server
db.close()

############################################
# Display the Results (this could be a new
# page)
#
#
############################################
