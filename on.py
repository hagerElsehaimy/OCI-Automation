import oci
import re

config = oci.config.from_file("config")

OCIDs_file = open('OCID.txt', 'r')
OCIDs = OCIDs_file.readlines()


for OCID in OCIDs:
    OCID = OCID.strip()
    if re.search("dbnode", OCID):
        database_client = oci.database.DatabaseClient(config)

        # Send the request to service, some parameters are not required, see API
        # doc for more info
        db_node_action_response = database_client.db_node_action(db_node_id=OCID, action="START")
    elif re.search("instance", OCID):
        core_client = oci.core.ComputeClient(config)
        instance_action_response = core_client.instance_action(instance_id=OCID, action="START")

# Send the request to service, some parameters are not required, see API
# doc for more info

# os.system("oci db node start ocid1.dbnode.oc1.me-jeddah-1.anvgkljrqvob4kyaqtp6ivivuc2ocbmnpeydfzqisls5qvdbnq4ix7qy7jgq")

