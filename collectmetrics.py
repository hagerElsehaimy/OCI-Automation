import oci
from datetime import datetime, timedelta
# # Create a default config using DEFAULT profile in default location
# # Refer to
# # https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# # for more info
config = oci.config.from_file("config")

# Initialize service client with default config file
monitoring_client = oci.monitoring.MonitoringClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
#

start_time = datetime.strftime(datetime.now() - timedelta(hours=2, minutes=1), "%Y-%m-%dT%H:%M:%S.%fZ")
end_time = datetime.strftime(datetime.now()-timedelta(hours=2), "%Y-%m-%dT%H:%M:%S.%fZ")

summarize_metrics_data_response = monitoring_client.summarize_metrics_data(
    compartment_id="ocid1.compartment.oc1..aaaaaaaa4vtosolddtixrwkdk43zpoyjehqbnbyy5wqfn4njzthbp3q74d6q",
    summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
        namespace="oci_computeagent",
        query='CpuUtilization[1m]{resourceDisplayName = "testvscalelinux"}.mean()',
        start_time=start_time,
        end_time=end_time
    ))

# Get the data from response
print(summarize_metrics_data_response.data)
# utilization = summarize_metrics_data_response.data[0].__dict__['_aggregated_datapoints'][0].__dict__['_value']
# print(utilization)
