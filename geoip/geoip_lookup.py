#!/usr/bin/python
# Stop copying stuff, and make your own tool!
import sys
import os
from time import sleep
from os import system,name
from ip2geotools.databases.noncommercial import DbIpCity

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def showinfo(ipinfo):
    clear()
    response = DbIpCity.get(ipinfo, api_key='free')
    long = response.longitude
    lati = response.latitude
    print(ipinfo+" |"+" Results: ")
    print("Country: "+response.country)
    print("Region: "+response.region)
    print("City: "+response.city)
    print(f"longitude: {long}")
    print(f"latitude: {lati}")

def gohelp():
    print("IP Geolocation Lookup v1.0 2020 by Exo")
    print("")
    print("")
    print("Only for legal activities | I'm not responsible for any")
    print("illegal activities performed by you! Keep it in mind pal!")
    print("")
    print("-h OR -help - Prints out this menu")
    print("-t OR -target - Prints out information about the ip.")
    print("-fs OR -fullscan - Performs a full scan about the ip.")
    print("")
    print("Examples:")
    print("geoip -h | geoip -help")
    print("geoip - 127.0.0.1")
    print("")
    print("If you have problems or you want to ask me about something, ")
    print("join this discord server: https://discord.gg/6PemAuJntx")

if __name__ == "__main__":
    prefix1 = sys.argv[1]
    if prefix1 == "geoip":
        prefix2 = sys.argv[2]
        if prefix2 == "-h":
            gohelp()
        elif prefix2 == "-help":
            gohelp()
        elif prefix2 == "-t":
            ipinfo = sys.argv[3]
            showinfo(ipinfo)
        elif prefix2 == "-target":
            ipinfo = sys.argv[3]
            showinfo(ipinfo)
        elif prefix2 == "-fs":
            print("In development!")
        elif prefix2 == "-fullscan":
            print("In development!")
        else:
            print("geoip: error: argument is missing/")
