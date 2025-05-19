import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class RemoteDict(rpyc.Service):
  dictionary = {}

  def exposed_add_item(self, key, value):
    self.dictionary[key] = value

  def exposed_get_keys(self):
    return list(self.dictionary.keys())

  def exposed_get_values(self):
    return list(self.dictionary.values())

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

if __name__ == "__main__":
  server = ThreadedServer(RemoteDict(), port = PORT)
  server.start()

