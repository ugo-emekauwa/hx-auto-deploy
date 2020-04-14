# HyperFlex Edge Auto Deploy with Cisco Intersight (dCloud)
The HyperFlex Edge Auto Deploy script enables automated deployment of Cisco HyperFlex Edge clusters through the Cisco Intersight API.

This script was initially available for use in Cisco dCloud HyperFlex demonstrations at Cisco Live 2020 in Barcelona. It is now publicly available on Cisco dCloud in the RTP (US East) datacenter in the following demos:

1. [_Cisco HyperFlex Edge 4.0 with Intersight v1 (All Flash, 2-Node)_](https://dcloud2-rtp.cisco.com/content/demo/669216)
2. [_Cisco HyperFlex Edge 4.0 with Intersight v1 (Hybrid, 2-Node)_](https://dcloud2-rtp.cisco.com/content/demo/669217)

Cisco dCloud is available at [https://dcloud.cisco.com](https://dcloud.cisco.com), where Cisco product demonstrations and labs can be found in the Catalog.

## How to Use:
Before proceeding with running the HyperFlex Auto Deploy script for dCloud, an API key must be generated. Here are the instructions:

1. Log into the jump server from wkst1 using the RDP shortcut on the desktop.
2. Log into the Intersight Account as specified in the demo guide.
3. In the Cisco Intersight menu, click the **Settings** icon, then select **Settings**.
4. In the Settings pane, go to the API section and click **API Keys**.
5. In the API keys pane, click **Generate API Key**.
6. In the **Generate API Key** window, under **Description**, fill-in the description field for the API key (e.g. _Key01_).
7. In the **Generate API Key** window, under **API Key Purpose**, select _API key for legacy Python SDK based on OpenAPI schema version 2_.
8. In the **Generate API Key** window, click the **Generate** button.
9. In the **Generate API Key** window, copy the **API Key ID**.
10. Minimize the jump server RDP window and return to the wkst1 desktop.
11. On the wkst1 desktop, right click the **HX_Auto_Deploy.py** file and select **Edit with IDLE 3.7 (64-bit)**.
12. In the **HX_Auto_Deploy.py** file, under the **MODULE REQUIREMENT 1** section, set the key_id variable by pasting in the **API Key ID** from step 9, in-between the quotes. For example:
    ```py
    key_id = "5c89885075646127773ec143/5c82fc477577712d3088eb2f/5c8987b17577712d302eaaff"
    ```
13. Enter **CTRL+S** to save the **API Key ID** to the HX_Auto_Deploy.py script.
14. Press **F5** to run the script.

Once the **HX_Auto_Deploy** script has completed running, you can return to the Cisco Intersight GUI to see the HyperFlex Edge cluster profile created and in a state of deployment in the **Profiles** section.

The **HyperFlex Notification Tool** located on the wkst1 desktop or available in the Github repository at [https://github.com/ugo-emekauwa/hyperflex-notification-tool](https://github.com/ugo-emekauwa/hyperflex-notification-tool) can be used to use auotmated updates on the status of the HyperFlex Edge deployment.

## Dependencies:
In order for the **HX_Auto_Deploy.py** script to work, the following types of Intersight HyperFlex policies must already be in place on the targeted Intersight account:

1. Cluster Network Configuration Policy
2. Node Configuration Policy (IP and Hostname)
3. Cluster Storage Configuration Policy
4. VMware vCenter Configuration Policy
5. System Configuration Policy (DNS, NTP and Timezone)
6. Local Credential Policy (Security)

In the dCloud HyperFlex Edge 2-Node demos, these Intersight HyperFlex policies have been pre-created with the required settings using a script named **hx_policy_maker.py**. The **hx_policy_maker.py** script is available in the GitHub repository named **HyperFlex Edge Policy Maker for Cisco Intersight (dCloud)** at [https://github.com/ugo-emekauwa/hx-policy-maker](https://github.com/ugo-emekauwa/hx-policy-maker).

## Author:
Ugo Emekauwa

## Contact Information:
uemekauw@cisco.com or uemekauwa@gmail.com
