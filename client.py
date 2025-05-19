import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print("Chaves atuais do dicionário:", conn.root.get_keys())
  print("Valores atuais do dicionário:", conn.root.get_values())
  key = input("Digite uma chave para ser adicionada: ")
  value = input(f"Digite um valor para ser adicionado à chave '{key}': ")
  conn.root.add_item(key, value)
  print("Chaves atuais do dicionário:", conn.root.get_keys())
  print("Valores atuais do dicionário:", conn.root.get_values())
