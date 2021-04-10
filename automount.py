import os
import time 

time.sleep(2)
def mount_sdb1():
	os.system("sudo mount /dev/sdb1 /mnt" )
def mount_sdb2():
	os.system("sudo mount /dev/sdb2 /mnt")

os.system("sudo fdisk -l")
print("fdisk command run")

if True:
	
	mount_sdb1()
	print("sdb1 has mount")
else:
	mount_sdb2()
	print("sdb2 has mount")
