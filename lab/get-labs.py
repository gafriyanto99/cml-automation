from virl2_client import ClientLibrary
client = ClientLibrary("https://172.30.33.224", "admin", "P@ssw0rd!", ssl_verify=False)
all_lab_names = []

# Retrieve all lab details from CML
labs = client.all_labs(show_all=True)

# Loop over each CML lab
for lab in labs:
 # Update the list of lab names
  all_lab_names.append(lab.title)
print (all_lab_names)