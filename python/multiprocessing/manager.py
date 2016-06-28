import sys
from multiprocessing.connection import Listener, Client

import ConfigWrapper

# TODO 
# TODO job scheduling
# TODO work management lifetime
# TODO timeouts
# TODO serialize python code
# TODO join and job queues.
# TODO worker continous monitoring
#


class ManagerConnection:
    def __init__(self, address, port, password):
        self.address  = address
        self.port     = port
        self.password = password
    def work(self):
        conn = Client(self.address, authkey=self.password)
        print conn.recv_bytes()
        conn.close()

	
if __name__ == '__main__':
   cfg=ConfigWrapper.ConfigWrapper("settings.ini")
   workerNames = cfg.getWorkerHosts()
   workers     = []
   for workerName in workerNames:
       connection = ManagerConnection(workerName, cfg.getWorkerPort(), cfg.getWorkerPass())
       workers.append(connection)

   for conn in workers:
       conn.work()
       


   print "this is the end"
    
