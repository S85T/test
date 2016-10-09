#!/usr/bin/python
import time
import ConfigParser
print "Hallo Welt!"
print (time.strftime("%d.%m.%Y %H:%M:%S"))
f = open('config.ini','r')
config = ConfigParser.RawConfigParser()
#config.add_section('Database')
#config.set('Database','DB','DefaultDB')
#config.set('Database','DBUser','DefaultDBUser')
#config.set('Database','DBPass','DefaultDBPass')

#with open('config.cfg','wb') as configfile:
# config.write(configfile)

config.read('config.cfg')
print config.get('Database','db')
print config.get('Database','dbuser')
print config.get('Database','dbpass')
