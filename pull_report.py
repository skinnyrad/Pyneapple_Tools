#!/usr/bin/env python
import os

# Runs the report tool to produce a json file of 
# the latest recon scan and the activity report.
os.system("""report_tool -m plaintext""")

# Moves that report to the Pyneapple_Tools folder
# and appends a date-time stamp to the filename.
os.system("""mv /tmp/report-output.txt /pineapple/Pyneapple_Tools/`date '+%Y%m%d_%H:%M:%S'`_report.json""")
