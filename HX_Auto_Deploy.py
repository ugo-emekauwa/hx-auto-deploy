"""
HyperFlex Edge Auto Deploy Script for dCloud (All Flash/Hybrid, 2-Node), v1.0
Author: Ugo Emekauwa
Contact: uemekauw@cisco.com, uemekauwa@gmail.com
Summary: The HyperFlex Edge Auto Deploy Script enables automated deployment
          of Cisco HyperFlex Edge clusters through the Cisco Intersight API.
"""

########################
# MODULE REQUIREMENT 1 #
########################
"""
For the following variable below named key_id, please fill in between
the quotes your Intersight API Key ID.

Here is an example: key_id = "5c89885075646127773ec143/5c82fc477577712d3088eb2f/5c8987b17577712d302eaaff"
"""
key_id = ""


# MODULE REQUIREMENT 2
"""
For the following variable below named key, please fill in between
the quotes your system's file path to your Intersight API key "SecretKey.txt" file.

Here is an example: key = "J:\\SecretKey.txt"
"""
key = "J:\\SecretKey.txt"


# Import needed Python modules
import sys
import os
import datetime
import intersight
from intersight.intersight_api_client import IntersightApiClient

# Define time variable
get_date = datetime.datetime.now()
date = get_date.strftime("%m/%d/%Y %H:%M:%S")

# Starting the HyperFlex Cluster Profile Deployment Script
print("Starting HyperFlex Cluster Profile Deployment Script.")

# Define Intersight SDK IntersightApiClient variables
# Tested on Cisco Intersight API Reference v1.0.9-1229
base_url = "https://intersight.com/api/v1"
api_instance = IntersightApiClient(host=base_url,private_key=key,api_key_id=key_id)

# Establish function to test for the availability of the Intersight API and Intersight account

def test_intersight_service():
  """This is a function to test the availability of the Intersight API and Intersight account. The Intersight account
  tested for is the owner of the provided Intersight API key and key ID.
  """
  try:
    # Check that Intersight Account is accessible
    print("Testing access to the Intersight API by verifying the Intersight account information...")
    check_account = intersight.IamAccountApi(api_instance)
    get_account = check_account.iam_accounts_get()
    if check_account.api_client.last_response.status is not 200:
      print("The Intersight API and Account Availability Test did not pass.")
      print("The Intersight account information could not be verified.")
      print("Exiting due to the Intersight account being unavailable.\n")
      print("Please verify that the correct API Key ID has been entered in the script.\n")
      sys.exit(0)
    else:
      account_name = get_account.results[0].name
      print("The Intersight API and Account Availability Test has passed.\n")
      print("The account named '" + account_name + "' has been found.\n")
      return account_name
  except Exception:
    print("Unable to access the Intersight API.")
    print("Exiting due to the Intersight API being unavailable.\n")
    print("Please verify that the correct API Key ID has been entered in the script.\n")
    sys.exit(0)


# Run the Intersight API and Account Availability Test
print("Running the Intersight API and Account Availability Test.")
intersight_api_test = test_intersight_service()
intersight_account_name = intersight_api_test

# Define required variables for HyperFlex Cluster Profile
hx_cluster_profile_name = "dcloud-hx-edge-cluster-1"
hx_software_version = "4.0(1b)"
hx_mgmt_platform_type = "EDGE"
hx_vlan_id = 100
hx_node1_attribute = "198.18.135.116"
hx_node2_attribute = "198.18.135.117"
hx_mgmt_ip_address = "198.18.135.100"
hx_mac_address_prefix = "00:25:B5:00"

# Pre-defined HyperFlex Policies
hx_local_credential_policy_name = "sample-local-credential-policy"
hx_sys_config_policy_name = "sample-sys-config-policy"
hx_vcenter_config_policy_name = "sample-vcenter-config-policy"
hx_cluster_storage_policy_name = "sample-cluster-storage-policy"
hx_node_config_policy_name = "sample-node-config-policy"
hx_cluster_network_policy_name = "sample-cluster-network-policy"

# Create the HyperFlex Software Version Policy
print("Attempting to create a new HyperFlex Software Version Policy for \nHyperFlex " + hx_software_version + "...")
hx_software_version_policy_name = hx_cluster_profile_name + "-software-version-policy"
print("Checking for the presence of pre-existing HyperFlex Software Version Policies...")
hx_software_version_policy = intersight.HyperflexSoftwareVersionPolicyApi(api_instance)
get_hx_software_version_policy = hx_software_version_policy.hyperflex_software_version_policies_get()
get_hx_software_version_policy_dict = get_hx_software_version_policy.to_dict()
hx_software_version_policy_name_list = []

if get_hx_software_version_policy_dict["results"] is not None:
  for policy in get_hx_software_version_policy_dict["results"]:
    hx_software_version_policy_name_list.append(policy["name"])
    if policy["name"] == hx_software_version_policy_name:
      print("A HyperFlex Software Version Policy named " + hx_software_version_policy_name + " already exists.")
      found_hx_software_version_policy = policy
      if found_hx_software_version_policy["hxdp_version"] == hx_software_version:
        print("The existing HyperFlex Software Version Policy is configured with the \nrequested software version, HyperFlex " + hx_software_version + ".\n")
      else:
        print("The required HyperFlex Software Version Policy cannot be created due to a pre-exisiting policy that does not meet the requested HyperFlex software version.")
        print("Please check the Intersight Account named " + intersight_account_name + " through the GUI")
        print("Verify that no pre-existing HyperFlex clusters with the name " + hx_cluster_profile_name + " are present.")
        print("If further help is needed, please contact dCloud support.")
        print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
        sys.exit(0)
      break
  if hx_software_version_policy_name not in hx_software_version_policy_name_list:
    print("Creating a new HyperFlex Software Version Policy named " + hx_software_version_policy_name + ".\n")
    hx_software_version_policy1_body = {
      "Name": hx_software_version_policy_name,
      "HxdpVersion": hx_software_version,
      }
    post_hx_software_version_policy1 = hx_software_version_policy.hyperflex_software_version_policies_post(hx_software_version_policy1_body)
else:
  print("Creating a new HyperFlex Software Version Policy named " + hx_software_version_policy_name + ".\n")
  hx_software_version_policy1_body = {
    "Name": hx_software_version_policy_name,
    "HxdpVersion": hx_software_version,
    }
  post_hx_software_version_policy1 = hx_software_version_policy.hyperflex_software_version_policies_post(hx_software_version_policy1_body)

# Retrieve the HyperFlex Software Version Policy
get_hx_software_version_policy = hx_software_version_policy.hyperflex_software_version_policies_get()
get_hx_software_version_policy_dict = get_hx_software_version_policy.to_dict()

if get_hx_software_version_policy_dict["results"] is not None:
  for policy in get_hx_software_version_policy_dict["results"]:
    if policy["name"] == hx_software_version_policy_name:
      hx_software_version_policy_moid = policy["moid"]
      print("The required HyperFlex Software Version Policy named " + hx_software_version_policy_name + " with the MOID of " + hx_software_version_policy_moid + " has been identified.\n")
else:
  print("The required HyperFlex Software Version Policy named " + hx_software_version_policy_name + " was not found.")
  print("Please check the Intersight Account named " + intersight_account_name + " through the GUI and verify that the needed resources are present.")
  print("If further help is needed, please contact dCloud support.")
  print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
  sys.exit(0)


# Retrieve available rack servers
print("Retrieving available rack unit servers...\n")
cmp_rack_unit = intersight.ComputeRackUnitApi(api_instance)
get_cmp_rack_unit = cmp_rack_unit.compute_rack_units_get()
get_cmp_rack_unit_dict = get_cmp_rack_unit.to_dict()
cmp_rack_unit_list = []

if get_cmp_rack_unit_dict["results"] is not None:
  for rack_unit in get_cmp_rack_unit_dict["results"]:
    if any(attribute in (hx_node1_attribute, hx_node2_attribute) for attribute in (rack_unit["kvm_ip_addresses"][0]["address"], rack_unit["serial"])):
      rack_unit_dict = {"MOID":rack_unit["moid"], "IP Address":rack_unit["kvm_ip_addresses"][0]["address"], "Serial":rack_unit["serial"]}
      cmp_rack_unit_list.append(rack_unit_dict)
else:
  print("There were no available rack servers found.")
  print("Please check the Intersight Account named " + intersight_account_name + " through the GUI \nand verify that the required rack server is present.")
  print("If further help is needed, please contact dCloud support.")
  print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
  sys.exit(0)

# Find pre-defined HX server nodes among retrieved rack servers
cmp_rack_unit_attribute_list = []
for selected_rack_unit in cmp_rack_unit_list:
  cmp_rack_unit_attribute_list.append(selected_rack_unit["IP Address"])
  cmp_rack_unit_attribute_list.append(selected_rack_unit["Serial"])

if not cmp_rack_unit_list:
  print("No pre-defined HyperFlex server nodes were found.")
  print("Please check the Intersight Account named " + intersight_account_name + " through the GUI \nand verify that the required rack servers are present.")
  print("If further help is needed, please contact dCloud support.")
  print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
  sys.exit(0)
else:
  for hx_node in cmp_rack_unit_list:
    if hx_node1_attribute in (hx_node["IP Address"], hx_node["Serial"]):
      hx_node1_moid = hx_node["MOID"]
      print("The HyperFlex server node with the pre-defined attribute " + hx_node1_attribute + " has been found.")
      print("The server has an IP address of " + hx_node["IP Address"] + ", the serial number " + hx_node["Serial"] + ", and the MOID of " + hx_node["MOID"] + ".\n")
    if hx_node2_attribute in (hx_node["IP Address"], hx_node["Serial"]):
      hx_node2_moid = hx_node["MOID"]
      print("The HyperFlex server node with the pre-defined attribute " + hx_node1_attribute + " has been found.")
      print("The server has an IP address of " + hx_node["IP Address"] + ", the serial number " + hx_node["Serial"] + ", and the MOID of " + hx_node["MOID"] + ".\n")

for hx_node_attribute in (hx_node1_attribute, hx_node2_attribute):
  if hx_node_attribute not in cmp_rack_unit_attribute_list:
    print("The required rack server with the assigned attribute " + hx_node_attribute + " \nwas not found.")
    print("Please check the Intersight Account named " + intersight_account_name + " through the GUI \nand verify that the required rack servers are present.")
    print("If further help is needed, please contact dCloud support.")
    print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
    sys.exit(0)
      
# Retrieve the HyperFlex Local Credential Policy for the Cluster Configuration "Security" policy type settings
hx_local_credential_policy = intersight.HyperflexLocalCredentialPolicyApi(api_instance)
get_hx_local_credential_policy = hx_local_credential_policy.hyperflex_local_credential_policies_get()
get_hx_local_credential_policy_dict = get_hx_local_credential_policy.to_dict()

if get_hx_local_credential_policy_dict["results"] is not None:
  for policy in get_hx_local_credential_policy_dict["results"]:
    if policy["name"] == hx_local_credential_policy_name:
      hx_local_credential_policy_moid = policy["moid"]
      print("The required HyperFlex Local Credential Policy named " + hx_local_credential_policy_name + " with the MOID of " + hx_local_credential_policy_moid + " has been identified.\n")
else:
  print("The required HyperFlex Local Credential Policy named " + hx_local_credential_policy_name + " was not found.")
  print("Please check the Intersight Account named " + intersight_account_name + " through the GUI and verify that the needed resources are present.")
  print("If further help is needed, please contact dCloud support.")
  print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
  sys.exit(0)

# Retrieve the HyperFlex System Configuration Policy for the Cluster Configuration "DNS, NTP, and Timezone" policy type settings
hx_sys_config_policy = intersight.HyperflexSysConfigPolicyApi(api_instance)
get_hx_sys_config_policy = hx_sys_config_policy.hyperflex_sys_config_policies_get()
get_hx_sys_config_policy_dict = get_hx_sys_config_policy.to_dict()

if get_hx_sys_config_policy_dict["results"] is not None:
  for policy in get_hx_sys_config_policy_dict["results"]:
    if policy["name"] == hx_sys_config_policy_name:
      hx_sys_config_policy_moid = policy["moid"]
      print("The required HyperFlex System Configuration Policy named " + hx_sys_config_policy_name + " with the MOID of " + hx_sys_config_policy_moid + " has been identified.\n")
else:
  print("The required HyperFlex System Configuration Policy named " + hx_sys_config_policy_name + " was not found.")
  print("Please check the Intersight Account named " + intersight_account_name + " through the GUI and verify that the needed resources are present.")
  print("If further help is needed, please contact dCloud support.")
  print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
  sys.exit(0)

# Retrieve the HyperFlex VMware vCenter Configuration Policy for the Cluster Configuration "vCenter (Optional)" policy type settings
hx_vcenter_config_policy = intersight.HyperflexVcenterConfigPolicyApi(api_instance)
get_hx_vcenter_config_policy = hx_vcenter_config_policy.hyperflex_vcenter_config_policies_get()
get_hx_vcenter_config_policy_dict = get_hx_vcenter_config_policy.to_dict()

if get_hx_vcenter_config_policy_dict["results"] is not None:
  for policy in get_hx_vcenter_config_policy_dict["results"]:
    if policy["name"] == hx_vcenter_config_policy_name:
      hx_vcenter_config_policy_moid = policy["moid"]
      print("The required HyperFlex VMware vCenter Configuration Policy named " + hx_vcenter_config_policy_name + " with the MOID of " + hx_vcenter_config_policy_moid + " has been identified.\n")
else:
  print("The required HyperFlex VMware vCenter Configuration Policy named " + hx_vcenter_config_policy_name + " was not found.")
  print("Please check the Intersight Account named " + intersight_account_name + " through the GUI and verify that the needed resources are present.")
  print("If further help is needed, please contact dCloud support.")
  print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
  sys.exit(0)

# Retrieve the HyperFlex Cluster Storage Configuration Policy for the Cluster Configuration "Storage Configuration (Optional)" policy type settings
hx_cluster_storage_policy = intersight.HyperflexClusterStoragePolicyApi(api_instance)
get_hx_cluster_storage_policy = hx_cluster_storage_policy.hyperflex_cluster_storage_policies_get()
get_hx_cluster_storage_policy_dict = get_hx_cluster_storage_policy.to_dict()

if get_hx_cluster_storage_policy_dict["results"] is not None:
  for policy in get_hx_cluster_storage_policy_dict["results"]:
    if policy["name"] == hx_cluster_storage_policy_name:
      hx_cluster_storage_policy_moid = policy["moid"]
      print("The required HyperFlex Cluster Storage Configuration Policy named " + hx_cluster_storage_policy_name + " with the MOID of " + hx_cluster_storage_policy_moid + " has been identified.\n")
else:
  print("The required HyperFlex Cluster Storage Configuration Policy named " + hx_cluster_storage_policy_name + " was not found.")
  print("Please check the Intersight Account named " + intersight_account_name + " through the GUI and verify that the needed resources are present.")
  print("If further help is needed, please contact dCloud support.")
  print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
  sys.exit(0)

# Retrieve the HyperFlex Node Configuration Policy for the Cluster Configuration "IP & Hostname" policy type settings
hx_node_config_policy = intersight.HyperflexNodeConfigPolicyApi(api_instance)
get_hx_node_config_policy = hx_node_config_policy.hyperflex_node_config_policies_get()
get_hx_node_config_policy_dict = get_hx_node_config_policy.to_dict()

if get_hx_node_config_policy_dict["results"] is not None:
  for policy in get_hx_node_config_policy_dict["results"]:
    if policy["name"] == hx_node_config_policy_name:
      hx_node_config_policy_moid = policy["moid"]
      print("The required HyperFlex Node Configuration Policy named " + hx_node_config_policy_name + " with the MOID of " + hx_node_config_policy_moid + " has been identified.\n")
else:
  print("The required HyperFlex Node Configuration Policy named " + hx_node_config_policy_name + " was not found.")
  print("Please check the Intersight Account named " + intersight_account_name + " through the GUI and verify that the needed resources are present.")
  print("If further help is needed, please contact dCloud support.")
  print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
  sys.exit(0)

# Retrieve the HyperFlex Cluster Network Configuration Policy for the Cluster Configuration "Network Configuration" policy type settings
hx_cluster_network_policy = intersight.HyperflexClusterNetworkPolicyApi(api_instance)
get_hx_cluster_network_policy = hx_cluster_network_policy.hyperflex_cluster_network_policies_get()
get_hx_cluster_network_policy_dict = get_hx_cluster_network_policy.to_dict()

if get_hx_cluster_network_policy_dict["results"] is not None:
  for policy in get_hx_cluster_network_policy_dict["results"]:
    if policy["name"] == hx_cluster_network_policy_name:
      hx_cluster_network_policy_moid = policy["moid"]
      print("The required HyperFlex Cluster Network Configuration Policy named " + hx_cluster_network_policy_name + " with the MOID of " + hx_cluster_network_policy_moid + " has been identified.\n")
else:
  print("The required HyperFlex Cluster Network Configuration Policy named " + hx_cluster_network_policy_name + " was not found.")
  print("Please check the Intersight Account named " + intersight_account_name + " through the GUI and verify that the needed resources are present.")
  print("If further help is needed, please contact dCloud support.")
  print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
  sys.exit(0)

# Create the HyperFlex Cluster Profile
print("Attempting to create a new HyperFlex Cluster Profile...")
print("Checking for the presence of pre-existing HyperFlex Cluster Profiles...")
hx_cluster_profile = intersight.HyperflexClusterProfileApi(api_instance)
get_hx_cluster_profile = hx_cluster_profile.hyperflex_cluster_profiles_get()
get_hx_cluster_profile_dict = get_hx_cluster_profile.to_dict()
hx_cluster_profile_name_list = []

if get_hx_cluster_profile_dict["results"] is not None:
  for profile in get_hx_cluster_profile_dict["results"]:
    hx_cluster_profile_name_list.append(policy["name"])
    if profile["name"] == hx_cluster_profile_name:
      print("A HyperFlex Cluster Profile named " + hx_cluster_profile_name + " already exists.")
      print("The new HyperFlex Cluster Profile cannot be created due to the pre-exisiting profile.")
      print("Please check the Intersight Account named " + intersight_account_name + " through the GUI.")
      print("Verify that no pre-existing HyperFlex clusters with the name " + hx_cluster_profile_name + " are present.")
      print("If further help is needed, please contact dCloud support.")
      print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
      sys.exit(0)
      break
  if hx_cluster_profile_name not in hx_cluster_profile_name_list:
    print("Creating a new HyperFlex Cluster Profile named " + hx_cluster_profile_name + ".\n")
    hx_cluster_profile1_body = {
      "Name": hx_cluster_profile_name,
      "MgmtPlatform": hx_mgmt_platform_type,
      "SoftwareVersion": {"Moid":hx_software_version_policy_moid},
      "LocalCredential": {"Moid":hx_local_credential_policy_moid },
      "SysConfig": {"Moid": hx_sys_config_policy_moid},
      "VcenterConfig": {"Moid": hx_vcenter_config_policy_moid},
      "ClusterStorage": {"Moid": hx_cluster_storage_policy_moid},
      "NodeConfig": {"Moid": hx_node_config_policy_moid},
      "ClusterNetwork": {"Moid": hx_cluster_network_policy_moid},    
      "StorageDataVlan":{"VlanId": hx_vlan_id},
      "MgmtIpAddress": hx_mgmt_ip_address,
      "MacAddressPrefix": hx_mac_address_prefix,
      }
    post_hx_cluster_profile1 = hx_cluster_profile.hyperflex_cluster_profiles_post(hx_cluster_profile1_body)
else:
  print("Creating a new HyperFlex Cluster Profile named " + hx_cluster_profile_name + ".\n")
  hx_cluster_profile1_body = {
    "Name": hx_cluster_profile_name,
    "MgmtPlatform": hx_mgmt_platform_type,
    "SoftwareVersion": {"Moid":hx_software_version_policy_moid},
    "LocalCredential": {"Moid":hx_local_credential_policy_moid },
    "SysConfig": {"Moid": hx_sys_config_policy_moid},
    "VcenterConfig": {"Moid": hx_vcenter_config_policy_moid},
    "ClusterStorage": {"Moid": hx_cluster_storage_policy_moid},
    "NodeConfig": {"Moid": hx_node_config_policy_moid},
    "ClusterNetwork": {"Moid": hx_cluster_network_policy_moid},    
    "StorageDataVlan":{"VlanId": hx_vlan_id},
    "MgmtIpAddress": hx_mgmt_ip_address,
    "MacAddressPrefix": hx_mac_address_prefix,
    }
  post_hx_cluster_profile1 = hx_cluster_profile.hyperflex_cluster_profiles_post(hx_cluster_profile1_body)


# Retrieve the HyperFlex Cluster Profile
get_hx_cluster_profile = hx_cluster_profile.hyperflex_cluster_profiles_get()
get_hx_cluster_profile_dict = get_hx_cluster_profile.to_dict()

if get_hx_cluster_profile_dict["results"] is not None:
  for profile in get_hx_cluster_profile_dict["results"]:
    if profile["name"] == hx_cluster_profile_name:
      hx_cluster_profile_moid = profile["moid"]
      print("The required HyperFlex Cluster Profile named " + hx_cluster_profile_name + " with the MOID of " + hx_cluster_profile_moid + " has been identified.\n")
else:
  print("The required HyperFlex Cluster Profile named " + hx_cluster_profile_name + " was not found.")
  print("Please check the Intersight Account named " + intersight_account_name + " through the GUI and verify that the needed resources are present.")
  print("If further help is needed, please contact dCloud support.")
  print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
  sys.exit(0)

# Create the HyperFlex Node Profiles
print("Attempting to create a new HyperFlex Node Profiles...")
hx_node_profile = intersight.HyperflexNodeProfileApi(api_instance)
hx_node_profile1_body = {
  "Name": "hx-edge-esxi-1",
  "HxdpMgmtIp": "198.18.135.103",
  "HypervisorMgmtIp": "198.18.135.101",
  "AssignedServer": {"Moid": hx_node1_moid},
  "ClusterProfile": {"Moid": hx_cluster_profile_moid}
  }
hx_node_profile2_body = {
  "Name": "hx-edge-esxi-2",
  "HxdpMgmtIp": "198.18.135.104",
  "HypervisorMgmtIp": "198.18.135.102",
  "AssignedServer": {"Moid": hx_node2_moid},
  "ClusterProfile": {"Moid": hx_cluster_profile_moid}
  }

post_hx_node_profile1 = hx_node_profile.hyperflex_node_profiles_post(hx_node_profile1_body)
post_hx_node_profile2 = hx_node_profile.hyperflex_node_profiles_post(hx_node_profile2_body)
print("New HyperFlex Node Profiles have been created.\n")

# Retrieve the HyperFlex Node Profiles
get_hx_node_profile = hx_node_profile.hyperflex_node_profiles_get()
get_hx_node_profile_dict = get_hx_node_profile.to_dict()

if get_hx_node_profile_dict["results"] is not None:
  for profile in get_hx_node_profile_dict["results"]:
    if profile["cluster_profile"]["moid"] == hx_cluster_profile_moid:
      print("The required HyperFlex Node Profile named " + profile["name"] + " with the MOID of " + profile["moid"] + " has been identified.\n")
else:
  print("Required HyperFlex Node Profiles were not found.")
  print("Please check the Intersight Account named " + intersight_account_name + " through the GUI and verify that the needed resources are present.")
  print("If further help is needed, please contact dCloud support.")
  print("Exiting the HyperFlex Cluster Profile Deployment Script.\n")
  sys.exit(0)

# Deploy HyperFlex Cluster Profile
print("Attempting to deploy the new HyperFlex Cluster Profile...")
hx_cluster_profile1_body_update1 = {"Action": "Deploy"}
patch_hx_cluster_profile1 = hx_cluster_profile.hyperflex_cluster_profiles_moid_patch(hx_cluster_profile_moid,hx_cluster_profile1_body_update1)
print("The new HyperFlex Cluster Profile named " + hx_cluster_profile_name + " \nhas been deployed!\n")
print("The HyperFlex Notification Tool on the wkst1 desktop can be used \nto receive email alerts on the progress.\n")
sys.exit(0)
