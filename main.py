# discord.gg/ruinus

import os
import json
import requests
from colorama import Fore, Style
import time
import fade

snusbase_auth = '' # Enter your api key.
snusbase_api = 'https://api-experimental.snusbase.com/'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

os.system('A$GARD - Made by gig')

def snus_email():
    clear()
    fade_ascii_alone = fade.purplepink(ascii_alone)
    print(fade_ascii_alone)

    def send_request(url, body=None):
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()
    
    termss = input(Style.RESET_ALL + "["+Fore.MAGENTA+"+"+Style.RESET_ALL+"] " + "Enter A Password-$ ")

    if termss == "exit":
        exit()
    elif termss == "menu":
        menu()
    else:
        search_response = send_request('data/search', {
            'terms': [termss],
            'types': ["email"],
            'wildcard': False,
        })
        formatted_response = json.dumps(search_response, indent=2)
        print(formatted_response)

        input("\nPress Enter to continue...")
        menu()

def snus_password():
    clear()
    fade_ascii_alone = fade.purplepink(ascii_alone)
    print(fade_ascii_alone)

    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termss = input(Style.RESET_ALL + "["+Fore.MAGENTA+"+"+Style.RESET_ALL+"] " + "Enter A Password-$ ")

        if termss == "exit":
            exit()
        elif termss == "menu":
            menu()
        else:
            search_response = send_request('data/search', {
                'terms': [termss],
                'types': ["password"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nPress Enter to continue...")
            menu()


def snus_Ip():
    clear()
    fade_ascii_alone = fade.purplepink(ascii_alone)
    print(fade_ascii_alone)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termss = input(Style.RESET_ALL + "["+Fore.MAGENTA+"+"+Style.RESET_ALL+"] " + "Enter a IP Address-$ ")

        if termss == "exit":
            exit()
        elif termss == "menu":
            menu()
        else:
            search_response = send_request('data/search', {
                'terms': [termss],
                'types': ["lastip"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\Press Enter to continue...")
            menu()

def snus_name():
    clear()
    fade_ascii_alone = fade.purplepink(ascii_alone)
    print(fade_ascii_alone)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.MAGENTA+"+"+Style.RESET_ALL+"] " + "Enter a First and Last Name with a space-$ ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            menu()
        else:
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["name"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nPress Enter to continue...")
            menu()

def snus_hash():
    clear()
    text_default_fade = fade.purplepink(ascii_alone)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termss = input(Style.RESET_ALL + "["+Fore.MAGENTA+"+"+Style.RESET_ALL+"] " + "Enter a Hash password-$ ")

        if termss == "exit":
            exit()
        elif termss == "menu":
            menu()
        else:
            search_response = send_request('data/search', {
                'terms': [termss],
                'types': ["hash"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nPress enter to continue...")
            menu()

def snus_username():
    clear()
    fade_ascii_alone = fade.purplepink(ascii_alone)
    print(fade_ascii_alone)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termss = input(Style.RESET_ALL + "["+Fore.MAGENTA+"+"+Style.RESET_ALL+"] " + "Enter a Username-$ ")

        if termss == "exit":
            exit()
        elif termss == "menu":
            menu()
        else:
            search_response = send_request('data/search', {
                'terms': [termss],
                'types': ["username"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)

            input("\nPress Enter to continue...")
            menu()

def menu():
    clear()
    print(ascii_text)
    choice = input("A$GARD-$ ")

    if choice == "1":
        snus_email()
    elif choice == "2":
        snus_password()
    elif choice == "3":
        snus_Ip()
    elif choice == "4":
        snus_name()
    elif choice == "5":
        snus_hash()
    elif choice == "6":
        snus_username()
    elif choice == "0":
        print("Closing in 3 seconds...")
        time.sleep(3)
        os._exit(0)
    else:
        print("Error, Please enter a valid option...")
        time.sleep(1)
        menu()

ascii_alone = """

 █████  ███████  ██████   █████  ██████  ██████  
██   ██ ██      ██       ██   ██ ██   ██ ██   ██ 
███████ ███████ ██   ███ ███████ ██████  ██   ██ 
██   ██      ██ ██    ██ ██   ██ ██   ██ ██   ██ 
██   ██ ███████  ██████  ██   ██ ██   ██ ██████  

"""


ascii_text = """

 █████  ███████  ██████   █████  ██████  ██████  
██   ██ ██      ██       ██   ██ ██   ██ ██   ██ 
███████ ███████ ██   ███ ███████ ██████  ██   ██ 
██   ██      ██ ██    ██ ██   ██ ██   ██ ██   ██ 
██   ██ ███████  ██████  ██   ██ ██   ██ ██████  

(1) $ Lookup Email.
(2) $ Lookup Password.
(3) $ Lookup IP.
(4) $ Lookup Name.
(5) $ Lookup Hash.
(6) $ Lookup Username.
(0) $ Exit The Program.

"""

if __name__ == "__main__":
    menu()
