import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target",help="Specify an IP address or the whole subnet")
    value = parser.parse_args()

    if not value.target:
        print("[-] Please specfiy an IP or Subnet")
    else:    
        return value

def scan(ip):
    # message for ARP request for asking IP address
    arp_request = scapy.ARP(pdst=ip) 

    #sending boradcast packet for MAC address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 

    #combinig ARP & MAC boradcast packet 
    arp_request_broadcast = broadcast/arp_request

    # boradcasting packet and saving only answered responses
    answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0] 
    client_list = [] # Making List of scanned clients
    for element in answered_list:
        client_dict = {'ip':element[1].psrc,'mac':element[1].hwsrc} #dictionary with scanned ip & MAC of clients
        client_list.append(client_dict) # adding dictionary to list
    return client_list # returning client list with scanned dictionary of IP & MAC

def print_result(captured_list):
        # iterating through the answered list and only printing IP & MAC addresses
        print('IP\t\t\tMAC\n----------------------------------')
        for client in captured_list:
            print(client["ip"]+"\t\t"+client["mac"]) # printing clients IP & MAC

target_value = get_arguments()
scan_result = scan(target_value.target)
print_result(scan_result)
