import oci
# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file("config")

DB_OCID = "ocid1.dbsystem.oc1.me-jeddah-1.anvgkljrqvob4kyapqbm3aa56zi6dnmjwjmjw432p4izuztsg6k64q6xhoka"
cpu_core_count = 2
shape = "VM.Standard2.4"
# Initialize service client with default config file
database_client = oci.database.DatabaseClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
update_db_system_response = database_client.update_db_system(
    db_system_id=DB_OCID,
    update_db_system_details=oci.database.models.UpdateDbSystemDetails(
        cpu_core_count=cpu_core_count,
        shape=shape))

# Get the data from response
print(update_db_system_response.data)