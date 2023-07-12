#!/usr/bin/python3
## Try a real world test with getpass

## import Paramiko so we can talk SSH
import paramiko # allows Python to ssh
import os # low level operating system commands
import getpass # we need this to accept passwords


def movethemfiles(sftp, target_directory):
    # Check if the target directory exists
    parent_directory = os.path.dirname(target_directory)
    directory_contents = sftp.listdir(parent_directory)
    if os.path.basename(target_directory) not in directory_contents:
        print(f"Target directory '{target_directory}' does not exist.")
        return
    
    # iterate across the files within directory
    directory = "/path/to/source/directory"
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # filter files with a specific extension, like ".txt"
            source_path = os.path.join(directory, filename)
            target_path = os.path.join(target_directory, filename)
            sftp.put(source_path, target_path)
            print(f"Moved {filename} to {target_directory}")

def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender
    
    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass
    
    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    ## Get target directory from user
    target_directory = input("Enter the target directory path on the host: ")
    
    ## call movethemfiles() function
    movethemfiles(sftp, target_directory)
    
    ## close the connection
    sftp.close() # close the connection

if __name__ == "__main__":
    main()

