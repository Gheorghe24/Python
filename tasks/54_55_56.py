# 54. Write a Python program to get the current username. 

import os
print(os.environ['USER'])

# 55. Write a Python to find local IP addresses using Python's stdlib.
 
import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

print(get_ip())

# 56. Write a Python program to get height and width of the console window. 
  
# Get the size
# of the terminal
size = os.get_terminal_size()
  
  
# Print the size
# of the terminal
print(size)