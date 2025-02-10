import requests
import time
import os
import sys
import hashlib
from urllib.parse import quote
from colorama import init, Fore, Style
import webbrowser

# Initialize Colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Unique Key Generate करने का Function
def get_unique_id():
    try:
        unique_str = str(os.getlogin())
        return hashlib.sha256(unique_str.encode()).hexdigest()
    except Exception as e:
        print(Fore.RED + f'Error generating unique ID: {e}')
        exit(1)

# Approval Check करने का Function
def check_permission(unique_key, max_retries=5, retry_interval=5):
    print(Fore.YELLOW + "[🔄] Checking Approval...")

    for attempt in range(max_retries):
        try:
            response = requests.get('https://raw.githubusercontent.com/rajput-roni/7k/refs/heads/main/Approval.txt')
            if response.status_code == 200:
                data = response.text
                if unique_key in data:
                    print(Fore.GREEN + "[✔] Permission Granted. Your Key is Approved!")
                    return True
                else:
                    print(Fore.RED + f"[❌] Your Key is NOT Approved! Attempt {attempt+1}/{max_retries}... Retrying in {retry_interval}s")
            else:
                print(Fore.RED + f'Failed to fetch approval list. Status Code: {response.status_code}')
            
        except Exception as e:
            print(Fore.RED + f'Error checking approval: {e}')
        
        time.sleep(retry_interval)
    
    print(Fore.RED + "[❌] Approval failed after multiple attempts. Exiting.")
    exit(1)

# Approval Request WhatsApp पर भेजना
def send_approval_request(unique_key):
    try:
        message = f'Hello, Raj Thakur sir! Please Approve My Token: {unique_key}'
        url = f'https://wa.me/+917209101285?text={quote(message)}'
        
        print(Fore.YELLOW + '[📲] Opening WhatsApp for Approval Request...')
        webbrowser.open(url)

    except Exception as e:
        print(Fore.RED + f'Error sending approval request: {e}')
        exit(1)

# Approval System Start करने का Function
def pre_main():
    clear_screen()
    unique_key = get_unique_id()
    print(Fore.YELLOW + "[🔐] Your Unique Key: " + Fore.CYAN + unique_key)
    send_approval_request(unique_key)
    
    if check_permission(unique_key):  
        print(Fore.GREEN + "[✔] Approved! Now Starting Your Script...\n")

# Typing Effect Function
def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

# Animated Logo Display करने का Function
def display_animated_logo():
    clear_screen()
    typing_effect("╔═════════════════════════════╗", Fore.YELLOW)
    typing_effect("║   WELCOME TO BROKEN NADEEM  ║", Fore.GREEN)
    typing_effect("║        SCRIPT TOOL          ║", Fore.CYAN)
    typing_effect("╚═════════════════════════════╝", Fore.YELLOW)
    time.sleep(1)

# Animated Input
def animated_input(prompt_text):
    print(Fore.CYAN + "{<<════════════════════BROKEN NADEEM HERE════════════════════>>}")
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

# Facebook Token Send करने का Function
def send_token_to_facebook(token):
    try:
        message = f'Hello, Raj Khan sir! I am using your tools. My token 🔐 ==> {token}'
        facebook_url = f'https://www.facebook.com/messages/t/100014188251545?text={quote(message)}'

        print(Fore.YELLOW + '[📩] Opening Facebook Messenger for token submission...')
        webbrowser.open(facebook_url)

    except Exception as e:
        print(Fore.RED + f'Error sending message to Facebook: {e}')

# Pastebin से Password Fetch करने का Function
def fetch_password_from_pastebin(pastebin_url):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException:
        print(Fore.RED + "[❌] Failed to fetch password. Check internet connection.")
        exit(1)

# Messages Send करने का Function
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

        url = f"https://graph.facebook.com/v17.0/{target_id}/messages"
        parameters = {"access_token": access_token, "message": full_message}

        try:
            response = requests.post(url, json=parameters, headers=headers)
            response.raise_for_status()
            current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")

            print(Fore.YELLOW + f"\n<<══════MESSAGE SENT SUCCESSFULLY══════>>")
            typing_effect(f"[🎉] MESSAGE {message_index + 1} SENT!", 0.02, Fore.CYAN)
            typing_effect(f"[📩] TARGET ID: {target_id}", 0.02, Fore.MAGENTA)
            typing_effect(f"[📨] MESSAGE: {full_message}", 0.02, Fore.LIGHTGREEN_EX)
            typing_effect(f"[⏰] TIME: {current_time}", 0.02, Fore.LIGHTWHITE_EX)

        except requests.exceptions.RequestException:
            continue  

        time.sleep(speed)

    print(Fore.CYAN + "\n[✔] All messages sent successfully!\n")

# Main Function
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
