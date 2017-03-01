# this script will use rsync to sync files and folders

import os
import sys
import subprocess
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import src, dest


all_files = []

# Updating files in destination initially
cmd = "rsync -a --update "+src+" "+dest
p = subprocess.Popen(cmd, shell=True)
print("Destination synced with source")

class MyHandler(FileSystemEventHandler):

	def on_modified(self,event):
		flag = True
		global all_files
		current_files = []

		for root, dirs, files in os.walk(src):

			for filename in files:
				if "Untitled Document" in filename or filename.startswith("."):
					flag = False
					continue

				local_path = os.path.join(root, filename)
				current_files.append(local_path)

				if local_path not in all_files:
					all_files.append(local_path)


		# Assuming the process always runs on BOTH the machines,
		# this will work as expected
		if flag:
			# updates files in destination only if source has recent modified timestamp
			cmd = "rsync -a --update "+src+" "+dest
			process = subprocess.Popen(cmd, shell=True)
			# out, err = process.communicate()
			# print(out)

			# deletes files which are not in source
			cmd = "rsync -a --delete "+src+" "+dest
			process2 = subprocess.Popen(cmd, shell=True)

			print("Synchronized")



if __name__ == "__main__":    
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=src, recursive=True)
    observer.start()
    print('Watchdog is now watching "'+format(src)+'" for changes')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()