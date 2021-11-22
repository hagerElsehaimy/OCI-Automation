import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file("config")


# Initialize service client with default config file
object_storage_client = oci.object_storage.ObjectStorageClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
# list_object_versions_response = object_storage_client.list_objects(
#     namespace_name="oracleoci",
#     bucket_name="backup-bucket-versioning-enabled",
#     fields="storageTier, size")

list_object_versions_response = object_storage_client.list_object_versions(
    namespace_name="oracleoci",
    bucket_name="backup-bucket-versioning-enabled",
    fields="storageTier, size")


# Get the data from response
response = list_object_versions_response.data.__dict__['_items']
print(response)

# print(response[0].__dict__["_storage_tier"])

Archive_size = 0
for object_summary in response:
    object_summary = object_summary.__dict__
    if object_summary["_storage_tier"] == "Archive":
        Archive_size += object_summary["_size"]

        # Get the data from response
        print(list_object_versions_response.data)

print("{} Bytes".format(Archive_size))


