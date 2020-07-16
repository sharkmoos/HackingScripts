# Tool to grab banners, hostname and IP lookup
# Script by sharkmoos available
# Thanks for Downloading

import sys
import requests
import socket
import json

#Script to grab banner
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>") #URL as command line argument
    sys.exit(1)

req = requests.get("https://"+sys.argv[1]) #use domain name provided
print ("\n"+str(req.headers))


gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + "is: "+gethostby_ + "\n")

#ipinfo.io is the API

req_two = requests.get("https://ipinfo.io/"+gethostby_+"/json") # requested in JSON fomat

resp_ = json.loads(req_two.text)

#print all location info
print("Location: " + resp_["loc"])
print("Region:"+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])
