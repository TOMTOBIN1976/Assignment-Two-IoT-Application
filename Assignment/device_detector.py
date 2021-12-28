#!/usr/bin/env python3
#coding=utf-8
import logging
import subprocess

logging.basicConfig(filename='presence_detector.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

#dictionary of known devices 
devices = [{"name":"Katies iPhone", "mac":"9C:B6:D0:EA:89:BB"},
         {"name":"Chloes iPhone", "mac":"6A:A8:3E:12:9C:F8"},
         {"name":"Toms iPhone", "mac":"CA:DD:30:35:62:D8"},
        {"name":"Claires iPhone", "mac":"84:EA:97:6C:ED:54"}
        ]

# Returns the list of known devices found on the network
def find_devices():
    output = subprocess.check_output("sudo nmap -sn 192.168.1.0/24 | grep MAC", shell=True)
    devices_found=[]
    for dev in devices:   
        if dev["mac"].lower() in str(output).lower():
            logging.info(dev["name"] + " device is present")
            devices_found.append(dev)
        else:
            logging.info(dev["name"] + " device is NOT present")
    return(devices_found)

# Main program (prints the return of arp_scan )
def main():
    print(find_devices())

if __name__ == "__main__":
    main()