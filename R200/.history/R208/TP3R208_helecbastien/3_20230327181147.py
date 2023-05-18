def anonymize_mac_address(mac_address, counter):
    """
    Anonymize MAC address by replacing last 3 octets with a counter.
    """
    mac_regex = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    if not re.match(mac_regex, mac_address):
        raise ValueError("Invalid MAC address")
    return "{}:{:02x}:{:02x}:{:02x}".format(mac_address[:9], (counter >> 16) & 0xff, (counter >> 8) & 0xff, counter & 0xff)

# Example usage
mac_address = "00:11:22:33:44:55"
for i in range(3):
    print(anonymize_mac_address(mac_addres))