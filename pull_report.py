#!/usr/bin/env python
import os

# Runs the report tool to produce a json file of 
# the latest recon scan and the activity report,
# and names the file with a date/time stamp.
os.system("""report_tool -f `date '+%Y%m%d_%H:%M:%S'`_report.json -m json""")
