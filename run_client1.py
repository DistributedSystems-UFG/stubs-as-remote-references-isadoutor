from time import sleep
from client import Client
from dbclient import DBClient
from constRPC import HOSTS, PORTS, HOSTC2, PORTC2, PORTC1
c1 = Client(PORTC1)
dbC1 = DBClient(HOSTS, PORTS)
dbC1.create()
dbC1.appendData('Client 1')
sleep(2)
c1.sendTo(HOSTC2, PORTC2, dbC1)