import ConfigParser


class ConfigWrapper:
    def __init__(self, path):
        self.cfg = ConfigParser.ConfigParser()
        self.cfg.read(path)
        
    def getSafe(self, section, var, result):
        try:
             result = self.cfg.get(section, var, 0)
        except Exception as e:
             pass
        return result             
         
    def getWorkerPort(self):
        return self.getSafe("worker", "port", 6000)
        
    def getWorkerHosts(self):
        str = self.getSafe("worker", "hosts", "")
        return str.split(",")
    def getWorkerAuth(self):
        return  self.getSafe("worker", "auth", "sharedkey")
    def getWorkerPass(self):
        return  self.getSafe("worker", "pass", "changeme")
