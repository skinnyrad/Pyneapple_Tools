# Pyneapple_Tools

Pyneapple_Tools currently consists of two python scripts for the Wifi Pineapple Mark VII. 

The first, open_aps.py, is to be used after recon is run at least once. This script retrieves the results of your Recon activity from recon.db and pulls out all of the open access points. These access points are placed into a file called open_aps.txt. This file can be found the the Pyneapple_Tools directory after installation.

The second, top_ssids.py, can be run after logging PineAP activity. This script pulls the entries out of the activity log from log.db. It will create a list that ranks the most probed for SSIDs. If a single MAC address probes for an SSID 50 times, that will only be counted as 1 probe request. The intent is to use this script is to find out how many unique MAC addresses probe for a particular SSID. The output of the script is put into top_ssids.txt. The contents of the file lists the number of unique probe requests followed by the SSID.

The intention is that these scripts be used in tandem. First, gather all of the open SSIDs in a particular geographic region (using open_aps.py) and load those into the SSID pool of the Pineapple. Next, broadcast out those SSIDs and see which ones in the list elicit the greatest response from client devices (using top_ssids.py). Finally, elimate unproductive SSIDs from your pool list.

## Install
1. Acquire a [WiFi Pineapple Mark VII](https://shop.hak5.org/products/wifi-pineapple) from Hak5.
2. Go through the [setup process](https://docs.hak5.org/hc/en-us/articles/360053348994-1-Firmware-Install).
3. Click the terminal windows icon in the upper right corner of the Pineapple GUI.
4. At the terminal type:

        cd /pineapple
        opkg update
        opkg install git
        opkg install git-http
        opkg install python3-pip
        git clone https://github.com/skinnyrad/Pyneapple_Tools
        cd Pyneapple_Tools

## Execution
To run open_aps.py use python3 while in the Pyneapple_Tools directory.

        python3 open_aps.py
        
The output will be placed in open_aps.txt in the same directory.
Likewise, run top_ssids.py in the same manner.

        python3 top_ssids.py
        
The output will be placed in top_ssids.txt.
