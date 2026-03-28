import os
import hashlib
import time  
cmd = input()
cmd = cmd.split()
if cmd[0]=="com":
    if cmd[1]=="add":
        try:
            os.mkdir("commits")
        except FileExistsError:
            pass
        except FileNotFoundError:
            print(f"Parent directory does not exist. Use os.makedirs() for nested directories.")
        fle=cmd[2]
        sha1 = hashlib.sha1()
        with open(fle, 'rb') as f:
            while True:
                data = f.read(65536)
                if not data:
                    break
                sha1.update(data)
        hashed = sha1.hexdigest()
        fle_path = "commits\\"+str(hashed)+""+str(time.localtime().tm_mday())+str(time.localtime().tm_mon())+str(time.localtime().tm_year())+str(time.localtime().tm_hour())+str(time.localtime().tm_min())+str(time.localtime().tm_sec())
        newfile = open(fle_path,'w')
        fle = open(fle,'r')
        for line in fle:
            newfile.write(line)
        newfile.close()