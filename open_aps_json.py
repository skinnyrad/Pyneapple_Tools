import json
import sys

extraction = []

#gather name of input json file and output file
filename = sys.argv[1]
outfile = sys.argv [2]

#get data out of json file
with open(filename, "r") as results:
    data = json.load(results)

#if json file came from recon download
try:
    for keyval in data["APResults"]:
        if keyval['encryption']==0:
             extraction.append(keyval['ssid'])

#if json file came from report_tool
except:
    for keyval in data["ReconResult"]["APResults"]:
        if keyval['encryption']==0:
             extraction.append(keyval['ssid'])

#get rid of duplicate open APs
extraction = list(set(extraction))

#write list to output file
with open(outfile, 'w') as output:
    for extract in extraction:
        output.write(extract + "\n")
