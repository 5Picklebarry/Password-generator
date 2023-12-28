import random
import string
import ctypes
import os
from colorama import Fore, Style, init

init()

MIN_LENGTH = 5
MAX_LENGTH = 50

def set_cmd_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def print_header():
    header = f"""{Fore.RED}
    (  ____ \(  ____ )\__   __/(  ____ \| \    /\( \      (  ____ \( ___ \ ( ___  )( ____ )( ____ )|\     /|
    | (    \/| (    )|   ) (   | (    \/|  \  / /| (      | (    \/| (   ) )| (   ) || (    )|| (    )|( \   / )
    | (____  | (____)|   | |   | |      |  (_/ / | |      | (__    | (__/ / | (___) || (____)|| (_____) \ (_) / 
    (_____ \ |  ____)|   | |   | |      |   _ (  | |      |  __)   |  __ (  |  ___  ||     __)|     __)  \   /  
    ) )| (          | |   | |      |  ( \ \ | |      | (      | ( \ \ | (   ) || (\ (   | (\ (      ) (   
    /\____) )| )     ___) (___| (____/\|  /  \ \| (____/\| (____/\| )___) )| )   ( || ) \ \__| ) \ \__ | |   
    \______/ |/       \_______/(_______/|_/    \/(\_______/(_______/|/ \___/ |/     \||/   \__/|/   \__/ \_/   
    {Style.RESET_ALL}
    """
    print(header)

    text = f"{Fore.RED}Made by 5picklebarry{Style.RESET_ALL}"
    length = 120
    character = ' '

    centered_text = text.center(length, character)
    print(centered_text)

print_header()

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    set_cmd_title("5picklebarrys password gen")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print_header()

        while True:
            try:
                desired_length = int(input(f"{Fore.BLUE}\nEnter the desired password length (between 5 and 50): {Style.RESET_ALL}"))
                if 5 <= desired_length <= 50:
                    break
                else:
                    print(f"{Fore.MAGENTA}(=){Style.RESET_ALL} {Fore.RED}Please enter a valid length between 5 and 50.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.MAGENTA}(=){Style.RESET_ALL} {Fore.RED}Please enter a valid number.{Style.RESET_ALL}")

        password = generate_password(desired_length)
        print(
            f"{Fore.MAGENTA}(=){Style.RESET_ALL} {Fore.CYAN}Generated Password ({desired_length} characters):{Style.RESET_ALL}"
            f"{Fore.YELLOW}{password}{Style.RESET_ALL}"
        )

        input(f"{Fore.GREEN}\nPress Enter to generate another password...{Style.RESET_ALL}")