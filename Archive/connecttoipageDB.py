#!/usr/bin/python
print "Content-type:text/html\n\n"
import sys
import MySQLdb

try:
 conn = MySQLdb.connect (
  host = "bilkaloocom.ipagemysql.com",
  user = "goTigOg19a1hB2f",
  passwd = "1234chapo",
  db = "wordpress_2lh6323eig",
  port = 3306)

except MySQLdb.Error, e:
 print "Error %d: %s" % (e.args[0], e.args[1])
 sys.exit (1)

print "connected to the database"