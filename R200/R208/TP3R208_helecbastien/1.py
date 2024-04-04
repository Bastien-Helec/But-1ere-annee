import json



data=json.loads(open("tp3.json").read())
data=list(data)
#question 1.3 :
print(f"il y a {len(data)} paquets")
#question 1.4 :

eth=["eth.dst_raw", "eth.src_raw", "eth.type_raw"]
arp=["arp.hw.type_raw", "arp.proto.type_raw", "arp.hw.size_raw", "arp.proto.size_raw", "arp.opcode_raw" , "arp.src.hw_mac_raw", "arp.src.proto_ipv4_raw", "arp.dst.hw_mac_raw", "arp.dst.proto_ipv4_raw"]
final=[]
for x in range(len(eth)):
    final.append(data[13]['_source']['layers']['eth'][eth[x]][0])
for x in range(len(arp)):
    final.append(data[13]['_source']['layers']['arp'][arp[x]][0])

final=" ".join(final)
print(final)
