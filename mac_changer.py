import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="To select an interface")
    parser.add_option("-m","--mac",dest="mac",help="Set MAC address of an interface")
    (value,arg) = parser.parse_args()
    if not value.interface or not value.mac:
        print("[-] please specifiy options properly ,use --help for info")
    else:
        return value 
       

def change_mac(interface,mac):
    print("[+] Changing MAC for "+interface+" To"+" "+mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])

def current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",values.interface])
    search_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if search_mac:
       return search_mac.group(0)
    else:
        print("[-] Cannot Find MAC Address ")    

values = get_args()
curr_mac = current_mac(values.interface)
print("[+] Current MAC Address is : "+str(curr_mac))
change_mac(values.interface,values.mac)
curr_mac = current_mac(values.interface)
 
if curr_mac == values.mac:
    print("[+] Mac address successfully changed to : "+str(curr_mac))



    




   
