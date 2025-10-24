from virl2_client import ClientLibrary

client = ClientLibrary("https://172.30.33.224","admin", "P@ssw0rd!", ssl_verify=False)
lab = client.create_lab(title='Two Routers')

r1 = lab.create_node("R1", "iosv", 50, 100)
r2 = lab.create_node("R2", "iosv", 250, 100)
r1.config = "hostname router1"
r2.config = "hostname router2"

# create a link between R1 and R2
r1_i1 = r1.create_interface()
r2_i1 = r2.create_interface()
lab.create_link(r1_i1, r2_i1)

# start the lab
lab.start()

# print nodes and interfaces states:
for node in lab.nodes():
    print(node, node.state, node.cpu_usage)
    for interface in node.interfaces():
        print(interface, interface.readpackets, interface.writepackets)