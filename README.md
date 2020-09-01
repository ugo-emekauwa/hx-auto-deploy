# HyperFlex Edge Automated Deployment Tool for Cisco Intersight
The Cisco HyperFlex Edge Automated Deployment Tool (HX Auto Deploy) for Cisco Intersight enables automated deployment of HyperFlex Edge cluster installations through the Intersight API.

## What's New:
The **HX Auto Deploy Tool**, which was originally built for Cisco dCloud, has been re-designed and upgraded to work in any environment due to popular demand.
Here are a few of the new features:
  - Easily modifiable variable values for use in any environment.
  - Built-in HyperFlex policy creation and configuration on Intersight. No more dependencies on other scripts.
  - Dynamic support for all HyperFlex Edge cluster sizes on Intersight.
  - Advanced error-checking for HyperFlex configuration requirements similar to the Intersight GUI, in order to avoid unnecessary troubleshooting.

## Prerequisites:
1. Python 3 installed, which can be downloaded from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. The Cisco Intersight SDK for Python, which can be installed by running the following command:
   ```py
   python -m pip install git+https://github.com/CiscoUcs/intersight-python.git
   ```
   More information on the Cisco Intersight SDK for Python can be found at [https://github.com/CiscoUcs/intersight-python](https://github.com/CiscoUcs/intersight-python).
3. [_Optional_] If you already have the Cisco Intersight SDK for Python installed, you may need to upgrade. An upgrade can be performed by running the following command:
   ```py
   python -m pip install git+https://github.com/CiscoUcs/intersight-python.git --upgrade --user
   ```
4. A version 2 API key from your Intersight account. To learn how to generate an API key for your Intersight account, more information can be found at [https://intersight.com/help/features#rest_apis](https://intersight.com/help/features#rest_apis).
5. The CIMC/KVM IP address or serial number of the servers registered with Intersight that you plan on using in your HyperFlex Edge cluster. You can login to the Intersight GUI and find this information in the **ADMIN/Devices** section under the **Device IP** and **Device ID** columns. HyperFlex Edge with Intersight currently supports 2, 3 or 4 server node clusters.

## Getting Started:

1. Please ensure that the above prerequisites have been met.
2. Download the HX_Auto_Deploy.py file for the HyperFlex Edge Automated Deployment Tool from here on GitHub.
3. Edit the HX_Auto_Deploy.py file to set the **key_id** variable using the following instructions:
   - Open the HX_Auto_Deploy.py file in an IDLE or text editor of choice.
   - Find the comment:
     ```py
     ########################
     # MODULE REQUIREMENT 1 #
     ########################
     ```
   - Underneath, you will find the variable **key_id = ""**. The variable is currently empty.
   - Fill in between the quotes of the **key_id** variable value with the ID of your API key. For example: 
     ```py
     key_id = "5c89885075646127773ec143/5c82fc477577712d3088eb2f/5c8987b17577712d302eaaff"
     ```
4. Edit the HX_Auto_Deploy.py file to set the **key** variable using the following instructions:
   - Open the HX_Auto_Deploy.py file in an IDLE or text editor of choice.
   - Find the comment:
     ```py
     ########################
     # MODULE REQUIREMENT 2 #
     ########################
     ```
   - Underneath, you will find the variable **key = ""**. The variable is currently empty.
   - Fill in between the quotes of the **key** variable value with your system's file path to the SecretKey.txt file for your API key. For example: 
     ```py
     key = "C:\\Keys\\Key1\\SecretKey.txt"
     ```
5. Edit the HX_Auto_Deploy.py file to set all the HyperFlex configuration variable values using the following instructions:
   - Open the HX_Auto_Deploy.py file in an IDLE or text editor of choice.
   - Find the comment:
     ```py
     ########################
     # MODULE REQUIREMENT 3 #
     ########################
     ```
   - Underneath, you will find the instructions to edit the HyperFlex configuration variable values to match your environment. Each variable has a sample value for ease of use. The variable values to edit begin under the comment:
     ```py
     ####### Start Configuration Settings - Provide values for the variables listed below. #######
     ```
     Completion of editing the HyperFlex configuration variable values is marked by the comment:
     ```py
     ####### Finish Configuration Settings - The required value entries are complete. #######
     ```
6. Save the changes you have made to the HX_Auto_Deploy.py file.
7. Run the HX_Auto_Deploy.py file.

Once the **HX Auto Deploy Tool** has completed running, you can login to the Intersight GUI to see the HyperFlex Edge cluster profile created and in a state of deployment in the **CONFIGURE/Profiles** section.

The **HyperFlex Notification Tool** available on GitHub at [https://github.com/ugo-emekauwa/hyperflex-notification-tool](https://github.com/ugo-emekauwa/hyperflex-notification-tool) can be used to receive automated updates on the status of the HyperFlex Edge deployment.

## Use Cases:
The HyperFlex Edge Automated Deployment Tool for Cisco Intersight is featured on Cisco dCloud in the following labs:

1. [_Cisco HyperFlex Edge 4.0 with Intersight v1 (All Flash, 2-Node)_](https://dcloud2-rtp.cisco.com/content/demo/669216)
2. [_Cisco HyperFlex Edge 4.0 with Intersight v1 (Hybrid, 2-Node)_](https://dcloud2-rtp.cisco.com/content/demo/669217)

dCloud is available at [https://dcloud.cisco.com](https://dcloud.cisco.com), where Cisco product demonstrations and labs can be found in the Catalog.

## Author:
Ugo Emekauwa

## Contact Information:
uemekauw@cisco.com or uemekauwa@gmail.com
