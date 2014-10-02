import sys
from multiprocessing.connection import Listener, Client

import ConfigWrapper

address = ('localhost', 6000)

def worker(address, port, password):
    listener = Listener(address, authkey=password)
    conn = listener.accept()
    print 'connection accepted from', listener.last_accepted
    conn.send_bytes('hello')
    conn.close()
    listener.close()

if __name__ == '__main__':
   cfg=ConfigWrapper.ConfigWrapper("settings.ini")
   worker("localhost", cfg.getWorkerPort(), cfg.getWorkerPass())
