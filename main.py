import requests
import os
import sys
import time
import random
from datetime import datetime
import colorama
from colorama import Fore, Style

# Initialize Colorama
colorama.init(autoreset=True)

# Function for Animated ASCII Art
def animated_logo(logo_text, delay=0.002):
    os.system('clear')  # स्क्रीन क्लियर करें
    for char in logo_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

# ASCII Logo (With Animation & Colors)
logo = f"""{Fore.CYAN}      
         _          _______    ______     _______    _______    _______      _______    _         _________
( (    /|  (  ___  )  (  __  \   (  ____ \  (  ____ \  (       )    (  ___  )  ( \        \__   __/
|  \  ( |  | (   ) |  | (  \  )  | (    \/  | (    \/  | () () |    | (   ) |  | (           ) (   
|   \ | |  | (___) |  | |   ) |  | (__      | (__      | || || |    | (___) |  | |           | |   
| (\ \) |  |  ___  |  | |   | |  |  __)     |  __)     | |(_)| |    |  ___  |  | |           | |   
| | \   |  | (   ) |  | |   ) |  | (        | (        | |   | |    | (   ) |  | |           | |   
| )  \  |  | )   ( |  | (__/  )  | (____/\  | (____/\  | )   ( |    | )   ( |  | (____/\  ___) (___
|/    )_)  |/     \|  (______/   (_______/  (_______/  |/     \|    |/     \|  (_______/  \_______/
"""

animated_logo(logo)  # Animated Logo

# Country Information Box
print(f"{Fore.CYAN}╭───────────────────────── < ~ COUNTRY ~ > ─────────────────────────────────────╮")
print(f"{Fore.CYAN}│                         【•】 YOUR COUNTRY  ➤ INDIA                            │")
print(f"{Fore.CYAN}│                         【•】 YOUR REGION   ➤ BIHAR                            │")
print(f"{Fore.CYAN}│                         【•】 YOUR CITY     ➤ PATNA                            │")
print(f"{Fore.CYAN}╰────────────────────────────< ~ COUNTRY ~ >────────────────────────────────────╯")

# Personal Information Box
print(f"{Fore.YELLOW}╔════════════════════════════════════════════════════════════════════════════════════╗")
print(f"{Fore.CYAN}║  NAME                 : BROKEN-NADEEM           GOD ABBUS                     RAKHNA  ║")
print(f"{Fore.GREEN}║  RULLEX               : PATNA ON FIRE            KARNE PE                     SAB GOD  ║")
print(f"{Fore.CYAN}║  FORM 🏠              : BIHAR-PATNA              APPEARED                     ABBUS BANA ║")
print(f"{Fore.GREEN}║  BRAND                : MULTI CONVO              HATA DIYA                    HAI BILKUL ║")
print(f"{Fore.CYAN}║  GitHub               : BROKEN NADEEM            JAAEGA YE                    KOI BHI HO ║")
print(f"{Fore.GREEN}║  WHATSAP              : +917209101285            BAAT YWAD                   GOD ABBUS NO ║")
print(f"{Fore.YELLOW}╚════════════════════════════════════════════════════════════════════════════════════╝")

# Start Time
print(f"{Fore.GREEN}START TIME : {time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"{Fore.CYAN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")

# Login System
def pas():
    print(f"{Fore.WHITE}{Fore.GREEN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")
    password = input(f"{Fore.LIGHTGREEN_EX}𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜  ") 
    print(f"{Fore.GREEN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")
    mmm = requests.get('https://pastebin.com/raw/8pEpSkpa').text

    if mmm not in password:
        print(f"{Fore.YELLOW}𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜ ")
        sys.exit()
        
pas()

# Prompt for token file
token_file = input(f"{Fore.LIGHTBLACK_EX}𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 ➜ ")
print(f"{Fore.GREEN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")

# Read access token IDs from file
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Prompt for the number of user IDs
num_user_ids = int(input(f"{Fore.LIGHTGREEN_EX}𝗕𝗦𝗗𝗞 𝗞𝗜𝗧𝗡𝗜 𝗣𝗢𝗦𝗧 𝗣𝗘 𝗧𝗢𝗢𝗟𝗦 𝗟𝗚𝗔𝗡𝗔 𝗖𝗛𝗔𝗛𝗜𝗧𝗘𝗡 𝗛𝗢 𝗪𝗢 𝗗𝗔𝗟𝗜 ➜ "))
print(f"{Fore.GREEN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")

user_messages = {}
haters_name = {} 

# Prompt for user IDs and message files
for i in range(num_user_ids):
    user_id = input(f"{Fore.LIGHTGREEN_EX}𝗘𝗡𝗧𝗘𝗥 𝗣0𝗦𝗧 𝗜𝗗 𝗡𝗨𝗠𝗕𝗘𝗥➜ ")
    hater_name = input(f"{Fore.LIGHTGREEN_EX}𝗘𝗡𝗧𝗘𝗥 𝗛𝗔𝗧𝗘𝗥𝗦 𝗡𝗔𝗠𝗘➜ ")
    message_file = input(f"{Fore.LIGHTGREEN_EX}𝗘𝗡𝗧𝗘𝗥 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗙𝗜𝗟𝗘➜  ")
    
    haters_name[user_id] = hater_name
    user_messages[user_id] = message_file

# Prompt for delay time in messages
delay_time = int(input(f"{Fore.LIGHTGREEN_EX}𝗘𝗡𝗧𝗘𝗥 𝗗𝗘𝗟𝗔𝗬 /𝗧𝗜𝗠𝗘 (in seconds) ➜ "))
repeat_delay = int(input(f"{Fore.LIGHTGREEN_EX}𝗘𝗡𝗧𝗘𝗥 𝗥𝗘𝗣𝗘𝗔𝗧 𝗧𝗜𝗠𝗘 (in seconds) ➜ "))

# Function to send messages
def send_message(user_id, message, token):
    url = f"https://graph.facebook.com/{user_id}/comments"
    payload = {"message": message, "access_token": token}
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print(f"{Fore.GREEN}[✔] Successfully commented on {user_id}")
    else:
        print(f"{Fore.RED}[✖] Failed to comment on {user_id}: {response.text}")

# Start commenting process
print(f"{Fore.BLUE}[🔄] Starting Commenting Process...")

for user_id, message_file in user_messages.items():
    try:
        with open(message_file, 'r') as mf:
            messages = mf.readlines()
    except FileNotFoundError:
        print(f"{Fore.RED}[✖] Error: File {message_file} not found!")
        continue

    while True:
        for token in access_tokens:
            message = random.choice(messages).strip()
            send_message(user_id, message, token)
            time.sleep(delay_time)

        print(f"{Fore.YELLOW}[🔄] Waiting {repeat_delay} seconds before repeating...")
        time.sleep(repeat_delay)
