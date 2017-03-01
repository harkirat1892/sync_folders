This is a basic Python script that helps in synchronizing two folders on different systems, accessible via SSH keys. This uses rsync, which is available on almost all Linux based systems.

Watchdog is used, which monitors the folder for any changes. If any change is done in the folder, the Handler is called which uses rsync to update files on the destination server if source has the same file with recent modification date. Also, any new files in source also get copied to the destination.



Requirements:
------------


Python 3+
---------

Watchdog
-------

    sudo pip3 install watchdog


More about rsync with tutorial:
-----------------------------

https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps
