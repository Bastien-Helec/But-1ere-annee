from struct import pack
fileName='arp-cb.pcap'
pcap=open(fileName,'wb')
pcap_hdr=pack('=IHHiIII',
               0xA1B2C3D4,  # magic_number
               2,           # version_major
               4,           # version_minor
               0,           # timezone
               0,           # sigfigs
               0x40000,     # snaplen
               1)           # ethernet
pcap.write(pcap_hdr)

pkt_hexa='b07b25269ad93c5282ea5bd2080600010800060400013c5282ea5bd20acb00660000000000000acb0501'
ts_sec,ts_usec,pkt_len=0,0,len(pkt_hexa)//2
inc_len=pkt_len if pkt_len <= 65535 else 65535
pkt_hdr=pack('=IIII',
               ts_sec,      # ts_sec
               ts_usec,     # ts_usec
               inc_len,     # number of octets of packet saved in file
               pkt_len)     # actual length of packet
pcap.write(pkt_hdr)
pcap.write(bytes.fromhex(pkt_hexa))
pcap.close()
print(f'PCAP {fileName} created.')
