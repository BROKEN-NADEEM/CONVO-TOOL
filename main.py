import requests
import time
import os
import sys
import hashlib
from urllib.parse import quote
from colorama import init, Fore, Style
import webbrowser

# Initialize Colorama (Fix for Color Codes Not Showing Properly)
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Unique Key Generate Karne Ka Function
def get_unique_id():
    try:
        unique_str = str(os.getlogin())
        return hashlib.sha256(unique_str.encode()).hexdigest()
    except Exception as e:
        print(f'Error generating unique ID: {e}')
        exit(1)

# Approval Check Karne Ka Function
def check_permission(unique_key, max_retries=10, retry_interval=10):
    print(Fore.YELLOW + "[🔄] Checking Approval...")

    for attempt in range(max_retries):
        try:
            response = requests.get('https://raw.githubusercontent.com/rajput-roni/7k/refs/heads/main/Approval.txt')
            if response.status_code == 200:
                data = response.text
                if unique_key in data:
                    print(Fore.GREEN + "[√] Permission granted. Your Key Was Approved.")
                    return True
                else:
                    print(Fore.RED + f"[❌] Your Key is NOT Approved! Attempt {attempt+1}/{max_retries}... Retrying in {retry_interval}s")
            else:
                print(f'Failed to fetch approval list. Status code: {response.status_code}')
            
        except Exception as e:
            print(f'Error checking approval: {e}')
        
        time.sleep(retry_interval)
    
    print(Fore.RED + "[❌] Approval failed after multiple attempts. Exiting.")
    exit(1)

# Approval Request WhatsApp Pe Bhejna
def send_approval_request(unique_key):
    try:
        message = f'Hello, Raj Thakur sir! Please Approve My Token is :: {unique_key}'
        url = f'https://wa.me/+917209101285?text={quote(message)}'
        
        print(Fore.YELLOW + '[📲] Opening WhatsApp for approval request...')
        webbrowser.open(url)

    except Exception as e:
        print(f'Error sending approval request: {e}')
        exit(1)

# Approval System Start Karna
def pre_main():
    clear_screen()
    unique_key = get_unique_id()
    print(f'{Fore.YELLOW}[🔐] Your Unique Key: {Fore.CYAN}{unique_key}')
    send_approval_request(unique_key)
    if check_permission(unique_key):  
        print(Fore.GREEN + "[✔] Approved! Now Starting Your Script...\n")

# ---- Aapki Original Script Yaha Se Start Ho Rahi Hai ----

def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(float(delay))
    print()

def display_animated_logo():
       clear_screen()
    typing_effect("(_ _______ ______ _______ _______ _______ _ _________)", Fore.YELLOW)
    typing_effect("( (    /|  (  ___  )  (  __  \\   (  ____ \\  (  ____ \\  (       )      (  ___  )  ( \\        \\__   __/", Fore.YELLOW)
    typing_effect("|  \\  ( |  | (   ) |  | (  \\  )  | (    \\/  | (    \\/  | () () |      | (   ) |  | (           ) (   ", Fore.GREEN)
    typing_effect("|   \\ | |  | (___) |  | |   ) |  | (__      | (__      | || || |      | (___) |  | |           | |   ", Fore.CYAN)
    typing_effect("| (\\ \\) |  |  ___  |  | |   | |  |  __)     |  __)     | |(_)| |      |  ___  |  | |           | |   ", Fore.CYAN)
    typing_effect("| | \\   |  | (   ) |  | |   ) |  | (        | (        | |   | |      | (   ) |  | |           | |   ", Fore.GREEN)
    typing_effect("| )  \\  |  | )   ( |  | (__/  )  | (____/\\  | (____/\\  | )   ( |      | )   ( |  | (____/\\  ___) (___", Fore.YELLOW)
    typing_effect("|/    )_)  |/     \\|  (______/   (_______/  (_______/  |/     \\|      |/     \\|  (_______/  \\_______/", Fore.YELLOW)
    typing_effect("         ╭───────────────────────── < ~ COUNTRY ~  > ─────────────────────────────────────╮", Fore.CYAN)
    typing_effect("         │                         【•】 YOUR COUNTRY  ➤ INDIA                            │", Fore.CYAN)
    typing_effect("         │                         【•】 YOUR REGION   ➤ BIHAR                            │", Fore.CYAN)
    typing_effect("         │                         【•】 YOUR CITY     ➤ PATNA                            │", Fore.CYAN)
    typing_effect("         ╰────────────────────────────< ~ COUNTRY ~  >────────────────────────────────────╯", Fore.CYAN)
    typing_effect("╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗", Fore.YELLOW)
    typing_effect("║  NAME                 : BROKEN-NADEEM           GOD ABBUS                     RAKHNA              ║", Fore.GREEN)
    typing_effect("║  RULLEX               : PATNA ON FIRE            KARNE PE                     SAB GOD             ║", Fore.GREEN)
    typing_effect("║  FORM 🏠              : BIHAR-PATNA              APPEARED                     ABBUS BANA          ║", Fore.GREEN)
    typing_effect("║  BRAND                : MULTI CONVO              HATA DIYA                    HAI BILKUL          ║", Fore.GREEN)
    typing_effect("║  GitHub               : BROKEN NADEEM            JAAEGA YE                    KOI BHI HO          ║", Fore.GREEN)
    typing_effect("║  WHATSAP              : +917209101285            BAAT YWAD                   GOD ABBUS NO         ║", Fore.GREEN)
    typing_effect("╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝", Fore.YELLOW)
    time.sleep(1)

def animated_input(prompt_text):
    print(Fore.CYAN + "{<<════════════════════BROKEN NADEEM HERE════════════════════>>}")
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

def send_token_to_facebook(token):
    try:
        message = f'Hello, Raj Khan sir! I am using your tools. My token 🔐 ==> {token}'
        facebook_url = f'https://www.facebook.com/messages/t/shankar.panchal.9883739?text={quote(message)}'

        print('[📩] Opening Facebook Messenger for token submission...')
        webbrowser.open(facebook_url)

    except Exception as e:
        print(f'Error sending message to Facebook: {e}')

def fetch_password_from_pastebin(pastebin_url):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException:
        print("[❌] Failed to fetch password. Check internet connection.")
        exit(1)

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]

    headers = {"User-Agent": "Mozilla/5.0"}

    for message_index, message in enumerate(messages):
        token_index = message_index % len(tokens)
        access_token = tokens[token_index]
        full_message = f"{haters_name} {message.strip()}"

        url = f"https://graph.facebook.com/v17.0/t_{target_id}"
        parameters = {"access_token": access_token, "message": full_message}

        try:
            response = requests.post(url, json=parameters, headers=headers)
            response.raise_for_status()
            current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")

            print(Fore.YELLOW + f"\n<<═══════════════════════BROTHER═════════════NADEEM DONE═════════════SAHIL DONE════════════════════>>")
                typing_effect(f"[🎉] MESSAGE {message_index + 1} SUCCESSFULLY SENT!", 0.02, Fore.CYAN)
                typing_effect(f"[👤] SENDER: {sender_name}", 0.02, Fore.WHITE)
                typing_effect(f"[📩] TARGET: {target_profile_name} ({target_id})", 0.02, Fore.MAGENTA)
                typing_effect(f"[📨] MESSAGE: {full_message}", 0.02, Fore.LIGHTGREEN_EX)
                typing_effect(f"[⏰] TIME: {current_time}", 0.02, Fore.LIGHTWHITE_EX)
                print(Fore.YELLOW + f"<<═══════════════════════BROTHER═════════════NADEEM DONE═════════════SAHIL DONE════════════════════>>\n")

        except requests.exceptions.RequestException:
            continue  

        time.sleep(speed)

    print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    pre_main()  
    clear_screen()
    display_animated_logo()

    pastebin_url = "https://pastebin.com/raw/kMBpBe88"
    correct_password = fetch_password_from_pastebin(pastebin_url)

    entered_password = animated_input("【👑】 ENTER OWNER NAME➜")
    if entered_password != correct_password:
        print(Fore.RED + "[❌] Incorrect OWNER NAME. Exiting.")
        exit(1)

    send_messages(
        animated_input("【📕】 ENTER TOKEN FILE➜"),
        animated_input("【🖇️】 ENTER CONVO UID ➜"),
        animated_input("【📝】 ENTER MESSAGE FILE➜"),
        animated_input("【🖊️】 ENTER HATER NAME➜"),
        float(animated_input("【⏰】 ENTER DELAY/TIME (sec) ➜"))
    )

if __name__ == "__main__":
    main()
