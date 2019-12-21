# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:21:01 2019

@author: CEC
"""
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Riobamba"
dest = "Quito"
key = "DCuGa8AduAE1DmM4hNoSU5RuqGyKjtko"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")