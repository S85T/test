#!/usr/bin/python
import sys
import time
import ConfigParser
import os.path
import os
import MySQLdb

VERSION = 0.2
dbuser = ''
dbpass = ''
dbhost = ''
dbname = ''


print "#### Demonstrator Version %s ####"%(VERSION)

curtime = (time.strftime("%d.%m.%Y %H:%M:%S"))
print curtime
conffile = '/var/lib/univention-appcenter/apps/littledemoapp/data/config/config.ini'
config = ConfigParser.RawConfigParser()
if not (os.path.isfile(conffile)):
 print('Pfad noch nicht vorhanden, lege ihn an...')
 try:
  os.makedirs(os.path.dirname(conffile))
 except:
  print('Ordner konnte nicht angelegt werden...')
 f = open(conffile,'w')
else:
 f = open(conffile,'r')
 config.read(conffile)

if not (config.has_section('Database')):
 #Anlegen der Configdatei
 config.add_section('Database')
 config.set('Database','DB','DefaultDB')
 config.set('Database','DBUser','DefaultDBUser')
 config.set('Database','DBPass','DefaultDBPass')
 config.set('Database','CREATED',curtime)
 with open('config.cfg','wb') as configfile:
  config.write(configfile)
 print "Configdatei mit Defaultwerten geschrieben"
else:
 dbname = config.get('Database','dbname')
 dbuser = config.get('Database','dbuser')
 dbpass = config.get('Database','dbpass')
 dbhost = config.get('Database','dbhost')

print("%s %s %s %s ")%(dbname,dbuser,dbpass,dbhost)

#Database-Connection
try:
 try:
  db = MySQLdb.connect(dbhost,dbuser,dbpass,dbname)
 except:
  print("=> No Connection possible!")
 print("DB-Connection successful: ",db) 
 
 cur = db.cursor()
 cur.execute("select * from testappdata")
 for row in cur.fetchall():
  print row[0]
  
 cur.execute("create table testappdata (ID INT NOT NULL AUTO_INCREMENT, Dataname VARCHAR2(50))")

 db.close()
except:
 print("Unexpected error:",sys.exc_info()[0])
