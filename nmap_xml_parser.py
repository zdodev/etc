import xml.etree.ElementTree as et

tree = et.parse("skb_portscan_20191017.xml")

root = tree.getroot()
for host in root:
    if host.tag == "host":
        for address in host:
            if address.tag == "address":
                print(address.get("addr"))
        for ports in host:
            if ports.tag == "ports":
                for port in ports:
                    if port.tag == "port":
                        print(port.get("portid"), port.get("protocol"), end=" ")
                        for info in port:
                            if info.tag == "state":
                                if port.find("service") == None:
                                    print(info.get("state"))
                                else:
                                    print(info.get("state"), end=" ")
                            if info.tag == "service":
                                if info.get("product") != None:
                                    print(info.get("name"), info.get("product"), info.get("version"))
                                else:
                                    print(info.get("name"))

        print("")
        ###