from scapy.all import *
eth = Ether()
arp = ARP()

eth.dst = "ff:ff:ff:ff:ff:ff"

#arp.pdst = "192.168.244.125/130"
arp.pdst = ["192.168.244." + str(i) for i in range(125, 131)]

bcPckt = eth/arp

#bcPckt.show()

ans, unans = srp(bcPckt, timeout=5)

#ans.summary()
print("#"*30)
#unans.summary()

for snd, rcv in ans:
    rcv.show()
    print(rcv.src,rcv.psrc)