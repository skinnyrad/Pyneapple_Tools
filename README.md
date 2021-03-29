# Pyneapple_Tools

Pyneapple_Tools currently consists of three python scripts for the Wifi Pineapple Mark VII. These are helpful little quality of life tools that range from saving recon scans locally to understanding what clients are probing.

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

## open_aps.py
Used after recon is run at least once. This script retrieves the results of your Recon activity from recon.db and pulls out all of the open access point SSIDs. These SSIDs are placed into a file called open_aps.txt. This file can be found the the Pyneapple_Tools directory after installation.

To run open_aps.py use python3 while in the Pyneapple_Tools directory.

        python3 open_aps.py
        
The output will be placed in open_aps.txt in the same directory.

## open_aps_json.py
Like open_aps.py this script retrieves the results of recon activity and pulls out all open access point SSIDs. However this script is intended to be run on the json files produced by the reporting functions on the WiFi Pineapple. You can retrieve these json files by either downloading your results of a recon scan from the Recon GUI of the Pineapple or by running report_tool from the console interface.

***Unlike the other tools, this script can be run in both Windows and Linux.***

Execution on the Pineapple is as follows:

        python3 open_aps_json.py <filename_of_json_file.json> <output_filename>

For Windows you probably will start the command with just "python" instead of "python3".

## top_ssids.py
Can be run after logging PineAP activity. This script pulls the entries out of the PineAP Activity Log from log.db. It will create a list that ranks the most probed for SSIDs. If a single MAC address probes for an SSID 50 times, that will only be counted as 1 probe request. The intent is to use this script is to find out how many unique MAC addresses probe for a particular SSID. The output of the script is put into top_ssids.txt. The contents of the file lists the number of unique probe requests followed by the SSID.

The intention is that these scripts be used in tandem. First, gather all of the open SSIDs in a particular geographic region (using open_aps.py) and load those into the SSID pool of the Pineapple. Next, broadcast out those SSIDs and see which ones in the list elicit the greatest response from client devices (using top_ssids.py). Finally, elimate unproductive SSIDs from your pool list.

Likewise, run top_ssids.py in the same manner.

        python3 top_ssids.py
        
The output will be placed in top_ssids.txt.

## pull_reports.py

The script pulls the latest recon scan data and the current Pineap Activity Log and stores this data in a json file in the Pyneapple_Tools folder. The file is stored in the form of date_time_report.json. 

        python3 pull_reports.py
