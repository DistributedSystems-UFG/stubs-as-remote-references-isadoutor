import pickle
from client import Client
from constRPC import HOSTS, PORTS, PORTC2, STOP
c2 = Client(PORTC2)
data = c2.recvAny()
dbC2 = pickle.loads(data)
dbC2.appendData('Client 2')
print(dbC2.getValue())
c2.sendTo(HOSTS, PORTS, [STOP])