# HyperFlex Edge Auto Deploy with Intersight (dCloud)

The HyperFlex Edge Auto Deploy script enables automated deployment of Cisco HyperFlex Edge clusters through the Cisco Intersight API.

The script is available for use in the following dCloud demonstrations debuting at Cisco Live Barcelona 2020:

1. _Cisco HyperFlex Edge with Intersight v1 (All Flash, 2 Node)_
2. _Cisco HyperFlex Edge with Intersight v1 (Hybrid, 2 Node)_

## How to Use:

Before proceeding with running the HyperFlex Auto Deploy script for dCloud, an API key must be generated. Here are the instructions:

1. Log into the jump server from wkst1 using the RDP shortcut on the desktop.
2. Log into the Intersight Account as specified in the demo guide.
3. In the Cisco Intersight menu, click the **Settings** icon, then select **Settings**.
4. In the Settings pane, go to the API section and click **API Keys**.
5. In the API keys pane, click **Generate API Key**.
6. In the **Generate API Key** window, give the API key a description (e.g. "Key01"), then click **Generate**.
7. In the **Generate API Key** window, download the Secret Key. It will automatically save to the correct location needed by the HX_Auto_Deploy script.
8. In the **Generate API Key** window, copy the **API Key ID**.
9. Minimize the jump server RDP window and return to the wkst1 desktop.
10. On the wkst1 desktop, right click the **HX_Auto_Deploy.py** file and select **Edit with IDLE 3.7 (64-bit)**.
11. In the HX_Auto_Deploy.py file, under the **MODULE REQUIREMENT 1** section, set the key_id variable by pasting in the **API Key ID** from step 8, in-between the quotes. For example:
    ```py
    key_id = "5c89885075646127773ec143/5c82fc477577712d3088eb2f/5c8987b17577712d302eaaff"
    ```
12. Enter **CTRL+S** to save the **API Key ID** to the HX_Auto_Deploy.py script.
13. Press **F5** to run the script.

Once the HX_Auto_Deploy script has completed running, you can return to the Cisco Intersight GUI to see the HyperFlex Edge cluster profile created and in a state of deployment.

## Use Cases:
A modified version of the script in this repository is a part of the automation used to support and enable the following Cisco Data Center product demonstrations on Cisco dCloud:

1. _Cisco HyperFlex Edge with Intersight v1 (All Flash, 2 Node)_
2. _Cisco HyperFlex Edge with Intersight v1 (Hybrid, 2 Node)_

Cisco dCloud is available at [https://dcloud.cisco.com](https://dcloud.cisco.com), where product demonstrations and labs can be found in the Catalog.


## Author:
Ugo Emekauwa


## Contact Information:
uemekauw@cisco.com or uemekauwa@gmail.com
