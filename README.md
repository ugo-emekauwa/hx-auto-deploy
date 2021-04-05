# HyperFlex Edge Automated Deployment Tool for Cisco Intersight

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/ugo-emekauwa/hx-auto-deploy)

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
2. Install the Cisco Intersight SDK for Python by running the following command:
   ```
   python -m pip install git+https://github.com/CiscoUcs/intersight-python.git
   ```
   More information on the Cisco Intersight SDK for Python can be found at [https://github.com/CiscoUcs/intersight-python](https://github.com/CiscoUcs/intersight-python).
3. [_Optional_] If you already have the Cisco Intersight SDK for Python installed, you may need to upgrade. An upgrade can be performed by running the following command:
   ```
   python -m pip install git+https://github.com/CiscoUcs/intersight-python.git --upgrade --user
   ```
4. Clone or download the HyperFlex Edge Automated Deployment Tool for Cisco Intersight repository by using the ![GitHub Code Button](./assets/GitHub_Code_Button.png "GitHub Code Button") link on the main repository web page or by running the following command:
    ```
    git clone https://github.com/ugo-emekauwa/hx-auto-deploy
    ```
5. Generate a version 2 API key from your Intersight account.

    **(a).** Log into your Intersight account, click the Settings icon and select **Settings**.
    
      ![Figure 1 - Go to Settings](./assets/Figure_1_Go_to_Settings.png "Figure 1 - Go to Settings")
      
    **(b).** Under the API section in the work pane, click **API Keys**.
    
      ![Figure 2 - Go to API Keys](./assets/Figure_2_Go_to_API_Keys.png "Figure 2 - Go to API Keys")
      
    **(c).** In the API Keys section in the work pane, click the **Generate API Key** button.
    
      ![Figure 3 - Click the Generate API Key button](./assets/Figure_3_Click_the_Generate_API_Key_button.png "Figure 3 - Click the Generate API Key button")
      
    **(d).** In the Generate API Key window, enter a description or name for your API key.
    
      ![Figure 4 - Enter an API key description](./assets/Figure_4_Enter_an_API_key_description.png "Figure 4 - Enter an API key description")
      
    **(e).** In the Generate API Key window, under API Key Purpose, verify a version 2 API key is selected.
    
      ![Figure 5 - Verify version 2 API key selection](./assets/Figure_5_Verify_version_2_API_key_selection.png "Figure 5 - Verify version 2 API key selection")
      
    **(f).** In the Generate API Key window, click the **Generate** button.
    
      ![Figure 6 - Click the Generate button](./assets/Figure_6_Click_the_Generate_button.png "Figure 6 - Click the Generate button")
      
    **(g).** In the Generate API Key window, a new API key will be generated. Copy the API Key ID and download the Secret Key to a secure location.
    
      ![Figure 7 - Copy and save the API key data](./assets/Figure_7_Copy_and_save_the_API_key_data.png "Figure 7 - Copy and save the API key data")
6. Gather the CIMC/KVM IP address or serial number of the servers registered with Intersight that you plan on using in your HyperFlex Edge cluster. You can login to the Intersight GUI and find this information in the **ADMIN/Devices** section under the **Device IP** and **Device ID** columns. HyperFlex Edge with Intersight currently supports 2, 3 or 4 server node clusters.
    ![Figure 8 - Gather the server attributes](./assets/Figure_8_Gather_the_server_attributes.png "Figure 8 - Gather the server attributes")

## How to Use:
1. Please ensure that the above [**Prerequisites**](https://github.com/ugo-emekauwa/hx-auto-deploy#prerequisites) have been met.
2. Edit the HX_Auto_Deploy.py file to set the **`key_id`** variable using the following instructions:

    **(a).** Open the HX_Auto_Deploy.py file in an IDLE or text editor of choice.
    
    **(b).** Find the comment **`# MODULE REQUIREMENT 1 #`**.
     
      ![Figure 9 - MODULE REQUIREMENT 1 location](./assets/Figure_9_MODULE_REQUIREMENT_1_location.png "Figure 9 - MODULE REQUIREMENT 1 location")
      
    **(c).** Underneath, you will find the variable **`key_id`**. The variable is currently empty.
    
      ![Figure 10 - key_id variable location](./assets/Figure_10_key_id_variable_location.png "Figure 10 - key_id variable location")
      
    **(d).** Fill in between the quotes of the **`key_id`** variable value with the ID of your API key. For example:
      ```py
      key_id = "5c89885075646127773ec143/5c82fc477577712d3088eb2f/5c8987b17577712d302eaaff"
      ```
3. Edit the HX_Auto_Deploy.py file to set the **`key`** variable using the following instructions:

    **(a).** Open the HX_Auto_Deploy.py file in an IDLE or text editor of choice.
    
    **(b).** Find the comment **`# MODULE REQUIREMENT 2 #`**.
    
      ![Figure 11 - MODULE REQUIREMENT 2 location](./assets/Figure_11_MODULE_REQUIREMENT_2_location.png "Figure 11 - MODULE REQUIREMENT 2 location")
      
    **(c).** Underneath, you will find the variable **`key`**. The variable is currently empty.
    
      ![Figure 12 - key variable location](./assets/Figure_12_key_variable_location.png "Figure 12 - key variable location")
      
    **(d).** Fill in between the quotes of the **`key`** variable value with your system's file path to the SecretKey.txt file for your API key. For example:
      ```py
      key = "C:\\Keys\\Key1\\SecretKey.txt"
      ```
4. Edit the HX_Auto_Deploy.py file to set all the HyperFlex configuration variable values using the following instructions:

    **(a).** Open the HX_Auto_Deploy.py file in an IDLE or text editor of choice.

    **(b).** Find the comment **`# MODULE REQUIREMENT 3 #`**.
    
      ![Figure 13 - MODULE REQUIREMENT 3 location](./assets/Figure_13_MODULE_REQUIREMENT_3_location.png "Figure 13 - MODULE REQUIREMENT 3 location")
      
    **(c).** Underneath, you will find the instructions to edit the HyperFlex configuration variable values to match your environment. Each variable has a sample value for ease of use. The variable values to edit begin under the comment **`####### Start Configuration Settings - Provide values for the variables listed below. #######`**.
      
      ![Figure 14 - Start Configuration Settings location](./assets/Figure_14_Start_Configuration_Settings_location.png "Figure 14 - Start Configuration Settings location")
   
    Completion of editing the HyperFlex configuration variable values is marked by the comment **`####### Finish Configuration Settings - The required value entries are complete. #######`**.
      
      ![Figure 15 - Finish Configuration Settings location](./assets/Figure_15_Finish_Configuration_Settings_location.png "Figure 15 - Finish Configuration Settings location")
5. Save the changes you have made to the HX_Auto_Deploy.py file.
6. Run the HX_Auto_Deploy.py file. Upon a successful deployment, the **HX Auto Deploy Tool** will inform you that the new HyperFlex cluster profile has been deployed.
    ![Figure 16 - Completed HX_Auto_Deploy.py file execution](./assets/Figure_16_Completed_HX_Auto_Deploy.py_file_execution.png "Figure 16 - Completed HX_Auto_Deploy.py file execution")
7. Once the **HX Auto Deploy Tool** has completed running, you can login to the Intersight GUI to see the HyperFlex Edge cluster profile created and in a state of deployment in the **CONFIGURE/Profiles** section.
    ![Figure 17 - HyperFlex Cluster Profile Configuring state](./assets/Figure_17_HyperFlex_Cluster_Profile_Configuring_state.png "Figure 17 - HyperFlex Cluster Profile Configuring state")

The **HyperFlex Notification Tool** available on GitHub at [https://github.com/ugo-emekauwa/hyperflex-notification-tool](https://github.com/ugo-emekauwa/hyperflex-notification-tool) can be used to receive automated updates on the status of the HyperFlex Edge deployment.

## Use Cases:
The HyperFlex Edge Automated Deployment Tool for Cisco Intersight is featured on Cisco dCloud in the following labs:

1. [_Cisco HyperFlex Edge 4.5 with Intersight v1 (All Flash, 2-Node)_](https://dcloud2-rtp.cisco.com/content/demo/760975) - See the section **Deploy HyperFlex Using API**.
2. [_Cisco HyperFlex Edge 4.5 with Intersight v1 (Hybrid, 2-Node)_](https://dcloud2-rtp.cisco.com/content/demo/760974) - See the section **Deploy HyperFlex Using API**.
3. [_Cisco HyperFlex Edge 4.5 with Intersight v1 (All Flash, 3-Node)_](https://dcloud-cms.cisco.com/demo/cisco-hyperflex-edge-4-5-with-intersight-v1-all-flash-3-node) - See the section **Deploy HyperFlex Using API**.

dCloud is available at [https://dcloud.cisco.com](https://dcloud.cisco.com), where Cisco product demonstrations and labs can be found in the Catalog.

## Related Tools:
Here are similar tools to help administer and manage Cisco HyperFlex environments.
- [HyperFlex Notification Tool for Cisco Intersight](https://github.com/ugo-emekauwa/hyperflex-notification-tool)
- [Cisco HyperFlex API Token Manager](https://github.com/ugo-emekauwa/hx-api-token-manager)
- [HyperFlex HTML Plug-In Automated Installer](https://github.com/ugo-emekauwa/hx-html-plugin-auto-installer)

## Author:
Ugo Emekauwa

## Contact Information:
uemekauw@cisco.com or uemekauwa@gmail.com
