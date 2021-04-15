import os
import time

path = "/Users/sohumtripathi/Downloads"
now = time.time()

for filename in os.listdir(path):
    filestamp = os.stat(os.path.join(path, filename)).st_mtime
    filecompare = now - 7 * 86400
    if filestamp < filecompare:
        print(filename)
