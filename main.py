import os
import hashlib
cmd = input()
if cmd[0]=="com":
    if cmd[1]=="add":
        try:
            os.mkdir("commits")
            print(f"Directory 'commits' created successfully.")
        except FileExistsError:
            print(f"Directory 'commits' already exists.")
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
        hashed = sha1.digest()
        fle_path = "commits//"+str(hashed)
        newfile = open(fle_path,'w')
        for line in fle:
            newfile.write(line)
