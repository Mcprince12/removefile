import os
import time

path = "/Users/sohumtripathi/Downloads"
now = time.time()

for filename in os.listdir(path):
    # if os.stat(os.path.join(path, filename)).st_mtime < now - 7 * 86400:
    if os.path.getmtime(os.path.join(path, filename)) < now - 7 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            os.remove(os.path.join(path, filename))
