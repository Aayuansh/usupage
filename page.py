##------------------------------------#
__DEVOLPER__ = '___USU___'
__FACEBOOK__ =' USU-KINGS'
__DEVOLPER__ = '___MR AAYUNASH___'
__FACEBOOK__ =  'AAYU'
___V___= 1
__WHATSAPP___=+916280137565 
# YOU Must RUN pip install mahdix Beafore Run THIS 
#------------------------------------------------------#
import os
try:
    import requests,re,json,random,sys
    from mahdix import *
    from datetime import datetime
    from mahdix import html as bs
    from concurrent.futures import ThreadPoolExecutor
    from time import sleep as slp
    from time import time as tim
except:
    os.system('pip insatll mahdix')
    os.system('pip insatll requests')
    os.system('pip insatll bs4')

global syed
global ok
global cp
import requests
import re
import threading
import os
import sys
import random
import uuid
import base64
from datetime import datetime
from platform import uname,system
from hashlib import md5
from time import sleep, gmtime, strftime
rd='\033[38;5;208m'
grnh='\033[1;32m'
grn='\033[38;5;42m'
rdh='\033[1;31m'
yl='\033[38;5;220m'
bl='\033[38;5;38m'
bk1='\033[38;5;235m'
bk2='\033[38;5;238m'
bk3='\033[38;5;250m'
bk4='\033[38;5;255m';en='\033[0m'
unk=f'\033[38;5;{random.randint(1,200)}m'
line="-"*63
token  = str(md5(str(uname()).encode()).hexdigest())
def approval():
    try:
        token  = str(md5(str(uname()).encode()).hexdigest())
        response = requests.get("https://raw.githubusercontent.com/Aayuansh/aprroval/main/approval.txt")
        if token in response.text:return {"status":"ok"}
        else:return {"status":"no"}
    except:return {"status":"bad"}

def tele():
    return

def banner():
    os.system('cls')
    print(f"""{grnh}
 {line}
 
██╗   ██╗███████╗██╗   ██╗
██║   ██║██╔════╝██║   ██║
██║   ██║███████╗██║   ██║
██║   ██║╚════██║██║   ██║
╚██████╔╝███████║╚██████╔╝
 ╚═════╝ ╚══════╝ ╚═════╝ 
                          
    ------------------------------------------------------------
 [ Owners Name    : Aayu x Prince x Azhar x Sakib              ]
 [ Status         : Active                                     ]
 [ WhatsApp       : +916280137565                              ]
 [ Address        : India                                      ]
 [ Website        : www.usu.kings.com                          ]
 [ Time & Date    : {datetime.now()}                 ]
    ------------------------------------------------------------{en}""")
banner()      




def create(coki,user_agent):
        uid_me=coki.split('c_user=')[1].split(';')[0]
        try:
            headers_global = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '0.9',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.109", "Google Chrome";v="120.0.6099.109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user_agent,
    'viewport-width': '983',
}
            r = requests.Session()
            req = bs(r.get('https://www.facebook.com/pages/creation/?ref_type=launch_point', headers=headers_global, cookies={'cookie': coki}).content, 'html.parser')
            usr = re.search('__user=(.*?)&', str(req)).group(1)
            rev = re.search('{"rev":(.*?)}', str(req)).group(1)
            dts = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', str(req)).group(1)
            jzt = re.search('&jazoest=(.*?)",', str(req)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"', str(req)).group(1)
            spr = re.search('"__spin_r":(.*?),', str(req)).group(1)
            spt = re.search('"__spin_t":(.*?),', str(req)).group(1)
            name_p=str(f"{rc(names_fast)} {rc(last_names)}")
            bio_p='PAGE CREATED BY SYED FR TOOL'
            data = {'av': usr,'__user': usr,'__a': '1','__req': '1i','__hs': '19666.HYP:comet_pkg.2.1..2.1','dpr': '1','__ccg': 'MODERATE','__rev':rev,'__s': 'qvdp97:zb23lw:givv21','__comet_req': '15','fb_dtsg': dts,'jazoest': jzt,'lsd': lsd,'__aaid': '0','__spin_r': spr,'__spin_b': 'trunk','__spin_t': spt,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation','variables': '{"input":{"bio":"%s","categories":["1350536325044173","200597389954350","123377808095874"],"creation_source":"comet","name":"%s","page_referrer":"launch_point","actor_id":"%s","client_mutation_id":"3"}}'%(bio_p,name_p,usr),'server_timestamps': 'true','doc_id': '5296879960418435',}
            response = requests.post('https://www.facebook.com/api/graphql/', cookies={'cookie': coki}, headers=headers_global, data=data)
            parsed_data = json.loads(response.text)
            try:
                additional_profile_id = parsed_data['data']['additional_profile_plus_create']['additional_profile']['id']
                page_id = parsed_data['data']['additional_profile_plus_create']['page']['id']
                print(mahdilinx())
                print(f"{LI_MAGENTA}Page Name : {LI_YELLOW} {name_p}   | {uid_me}")
                print(f"[{len(page_total)}]{LI_GREEN} Profile ID: {LI_WHITE} {additional_profile_id}" )
                cokip=coki+'i_user='+additional_profile_id
                page_total.append(additional_profile_id)
            except:print(mahdilinx());print(f'You have created too many Pages recently. Please try again later : {LI_YELLOW}{uid_me}')
        except:print(mahdilinx());print(f'Something Wrong : {LI_YELLOW}{uid_me}');pass
        

names_fast = [
"ʋsʋ Kɩŋʛs Eŋtɘʀ", "ʋsʋ ʌɭwʌƴs oŋ ʆɩʀɘ", "ʋsʋ ɓʀʌŋɗ ɘŋtɘʀ", "ʋsʋ ʋŋɓɘʌtʌɓɭɘ ʀoɱʌŋtɩc ĸɩŋʛ"

]
last_names = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", 
    "10", "11", "12", "13", "14", "15", "16", "17", "18", 
    "19", "20", "21", "22", "23", "24", "25", "26", "27", 
    "28", "28", "29", "30", "31", "32", "33", "34", "35", 
    "36", "37", "38", "39", "40", "41", "42", "43", "44", 
    "45", "46", "47", "48", "49", "50", "51", "52", "53", 
    "54", "55", "56", "57", "58", "59", "60", "61", "62", 
    "63", "64", "65", "66", "67", "68", "69", "70", "71", 
    "72", "73", "74", "75", "76", "77", "78", "79", "80", 
    "81", "82", "83", "84", "85", "86", "87", "88", "89", 
    "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"
]
#logo=mahdi_logo
def main():
        
    clear()
    #print(logo)
    #print(mahdilinx())
    response = approval()
    if response['status']=='ok':pass
    else:input(f"\033[1;31mACCESS DENIED, NEED APPROVAL\033[0m: \033[32m{token}\033[0m");sys.exit()
    user_agent=input('past you user agent: ')
    if not user_agent:
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

    coki_f=input('cookes file : ')
    try:
        f_cokis=open(coki_f,'r').read().splitlines()
    except:print(f'{LI_RED}File not Found')
    with ThreadPoolExecutor(max_workers=15) as sub:
        for coki in f_cokis:
            #coki=coki.split('|')[2]
            #create(coki.replace(' ',''))
            sub.submit(create,coki.replace(' ',''),user_agent)
    print(mahdilinx())
    print(f'{LI_GREEN}       All Cookes use done      ')
    print(mahdilinx())
    slp(15)

page_total=[]

main()