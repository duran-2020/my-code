#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# python3 -m pip install crayons
import crayons
import json

# function to accept a list of IPs, iterate through the list, and print a special output
def devicereboot(devicecmd):

    print("Here's a list off all the IP addresses. They will each reboot.\n")
    for ip in devicecmd.keys(): #loop through the dict
        print(f'Connecting to.. {ip}. REBOOTING NOW! ')
    return None

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring with RED
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# start our main script
def main():
    """called at runtime"""
    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile) # decode the JSON from the file to pythonic data

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

    ## print connecting to, rebooting now function
    devicereboot(devicecmd) 

# call our main function
main()

