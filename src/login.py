from jproperties import Properties
import webbrowser
import urllib.parse
import os
import sys

url = "https://api.icicidirect.com/apiuser/login?api_key="
with open(os.path.join(sys.path[0], 'app.properties'), 'r+b') as prop:
    configs = Properties()
    configs.load(prop,"utf-8")
    if len(configs) == 0:
        print("Error while reading properties files")
    else :
        api_key = configs.get("APP_KEY").data if configs.get("APP_KEY") else None
        webbrowser.open(url+urllib.parse.quote_plus(api_key))

        configs["SESSION_TOKEN"] = input("Enter token value: ")
        prop.seek(0)
        prop.truncate(0)
        configs.store(prop, encoding="utf-8")