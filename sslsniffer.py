import socket
import ssl
import threading

def is_secure_port(port):
  """Returns True if the port is a secure port, False otherwise."""
  if port == 443:
    return True
  else:
    return False

def is_valid_ssl_certificate(host, port):
  """Returns True if the host has a valid SSL certificate for the port, False otherwise."""
  try:
    sock = socket.create_connection((host, port))
    ssl_sock = ssl.wrap_socket(sock)
    ssl_sock.do_handshake()
    return True
  except Exception as e:
    return False

def check_host(host):
  """Checks if the host has a valid SSL certificate for port 443."""
  if is_secure_port(443):
    if is_valid_ssl_certificate(host, 443):
      print("The host {} has a valid SSL certificate for port 443.".format(host))
    else:
      print("The host {} does not have a valid SSL certificate for port 443.".format(host))

def main():
  """Checks if the hosts in a list have valid SSL certificates for port 443."""
  banner = """
   ____  __  __ ____  _
  | __  |  \/  |  _ \| |
  |  _| | |\/| | |_) | |
  | |   | |  | |  __/| |
  |_|   |_|  |_|\___||_|

  SSL Sniffer
  """
  print(banner)
  hosts = ["www.example.com", "www.google.com", "www.yahoo.com"]

  threads = []
  for host in hosts:
    t = threading.Thread(target=check_host, args=(host,))
    t.start()
    threads.append(t)

  for t in threads:
    t.join()

if __name__ == "__main__":
  main()