# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS. 

# For 32 bit it will return 32 and for 64 bit it will return 64
import struct,platform
print(struct.calcsize("P") * 8)
print(platform.architecture()[0])


# 43. Write a Python program to get OS name, platform and release information. 
import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())


# 44. Write a Python program to locate Python site-packages. 

import sysconfig
print(sysconfig.get_paths())
