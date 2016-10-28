#!/usr/bin/python
import time
import ConfigParser
import os.path
print "#### Demonstrator ####"
curtime = (time.strftime("%d.%m.%Y %H:%M:%S"))
print curtime
conffile = '/home/testapp/config.cfg'
config = ConfigParser.RawConfigParser()
if not (os.path.isfile(conffile)):
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
 config.read('config.cfg')
 print config.get('Database','db')
 print config.get('Database','dbuser')
 print config.get('Database','dbpass')
