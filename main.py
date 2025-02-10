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
    os.system('clear')  # स्क्रीन क्लियर करें (Linux/Mac के लिए) | Windows के लिए 'cls' इस्तेमाल करें
    for char in logo_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

# Animated Loading Effect
def loading_animation(text="Loading", dots=5, delay=0.3):
    for _ in range(dots):
        sys.stdout.write(Fore.YELLOW + text + "." * _ + " " * (dots - _) + "\r")
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

# Animated Welcome Logo
logo = f"""{Fore.CYAN}      
        ███╗   ██╗ █████╗ ██████╗ ██████╗ ███╗   ███╗     █████╗  ██████╗ 
        ████╗  ██║██╔══██╗██╔══██╗╚════██╗████╗ ████║    ██╔══██╗██╔════╝ 
        ██╔██╗ ██║███████║██║  ██║ █████╔╝██╔████╔██║    ███████║██║  ███╗
        ██║╚██╗██║██╔══██║██║  ██║ ╚═══██╗██║╚██╔╝██║    ██╔══██║██║   ██║
        ██║ ╚████║██║  ██║██████╔╝██████╔╝██║ ╚═╝ ██║    ██║  ██║╚██████╔╝
        ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝  ╚═╝ ╚═════╝  
"""

animated_logo(logo)  # Animated Logo
loading_animation("Initializing", dots=10)  # Loading Effect

# Country Information Box
info_box = f"""
{Fore.CYAN}╭───────────────────────── < ~ COUNTRY ~ > ───────────────────────────────╮
{Fore.CYAN}│ 【•】 YOUR COUNTRY  ➤ INDIA                                             │
{Fore.CYAN}│ 【•】 YOUR REGION   ➤ BIHAR                                             │
{Fore.CYAN}│ 【•】 YOUR CITY     ➤ PATNA                                             │
{Fore.CYAN}╰─────────────────────────────────────────────────────────────────────────╯
"""

animated_logo(info_box, delay=0.005)  # Animated Info Box

# Personal Information Box
personal_info = f"""
{Fore.YELLOW}╔═════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║  NAME                 : BROKEN-NADEEM           GOD ABBUS                ║
{Fore.GREEN}║  RULLEX               : PATNA ON FIRE          KARNE PE  SAB GOD        ║
{Fore.CYAN}║  FORM 🏠              : BIHAR-PATNA            APPEARED  ABBUS BANA      ║
{Fore.GREEN}║  BRAND                : MULTI CONVO            HATA DIYA  HAI BILKUL     ║
{Fore.CYAN}║  GitHub               : BROKEN NADEEM          JAAEGA YE  KOI BHI HO     ║
{Fore.GREEN}║  WHATSAPP             : +917209101285          BAAT YWAD  GOD ABBUS NO   ║
{Fore.YELLOW}╚═════════════════════════════════════════════════════════════════════════╝
"""

animated_logo(personal_info, delay=0.005)  # Animated Personal Info Box

# Start Time
print(f"{Fore.GREEN}START TIME : {time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"{Fore.CYAN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")

# Login System
def pas():
    print(f"{Fore.WHITE}{Fore.GREEN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")
    password = input(f"{Fore.GREEN}𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜  ") 
    print(f"{Fore.GREEN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")
    mmm = requests.get('https://pastebin.com/raw/8pEpSkpa').text

    if mmm not in password:
        print(f"{Fore.YELLOW}𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜ ")
        sys.exit()
        
pas()

# Prompt for token file
token_file = input(f"{Fore.BLACK}𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 ➜ ")
print(f"{Fore.GREEN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")

# Read access token IDs from file
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Prompt for the number of user IDs
num_user_ids = int(input(f"{Fore.GREEN}𝗕𝗦𝗗𝗞 𝗞𝗜𝗧𝗡𝗜 𝗣𝗢𝗦𝗧 𝗣𝗘 𝗧𝗢𝗢𝗟𝗦 𝗟𝗚𝗔𝗡𝗔 𝗖𝗛𝗔𝗛𝗜𝗧𝗘𝗡 𝗛𝗢 𝗪𝗢 𝗗𝗔𝗟𝗜 ➜ "))
print(f"{Fore.GREEN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")

user_messages = {}
haters_name = {} 

# Prompt for user IDs and message files
for i in range(num_user_ids):
    user_id = input(f"{Fore.GREEN}𝗘𝗡𝗧𝗘𝗥 𝗣0𝗦𝗧 𝗜𝗗 𝗡𝗨𝗠𝗕𝗘𝗥➜ ")
    hater_name = input(f"{Fore.GREEN}𝗘𝗡𝗧𝗘𝗥 𝗛𝗔𝗧𝗘𝗥𝗦 𝗡𝗔𝗠𝗘➜ ")
    message_file = input(f"{Fore.GREEN}𝗘𝗡𝗧𝗘𝗥 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗙𝗜𝗟𝗘➜  ")
    
    haters_name[user_id] = hater_name
    user_messages[user_id] = message_file

# Prompt for delay time in messages
delay_time = int(input(f"{Fore.GREEN}𝗘𝗡𝗧𝗘𝗥 𝗗𝗘𝗟𝗔𝗬 /𝗧𝗜𝗠𝗘 (in seconds) ➜ "))
repeat_delay = int(input(f"{Fore.GREEN}𝗘𝗡𝗧𝗘𝗥 𝗥𝗘𝗣𝗘𝗔𝗧 𝗧𝗜𝗠𝗘 (in seconds) ➜ "))

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
