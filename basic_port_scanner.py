import socket
import sys
from datetime import datetime
from colorama import Fore, init 

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


target_ip = input("Enter the target IP address: ").strip()

scan_start = datetime.now()

def port_scan(target_ip):
   
    try:
        ip = socket.gethostbyname(target_ip)
        
        print(Fore.MAGENTA + f"Port scan started at: {scan_start}")
        
        print(Fore.YELLOW + f"Scanning {ip}")
        
        for port in range(20,90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
               print(Fore.GREEN + "Port {}: Open".format(port))
               
            sock.close()
                
    except KeyboardInterrupt:
      print(Fore.RED + f"You have exited the port scanner")
      sys.exit()          
            
    except socket.gaierror:
      print(Fore.RED + f"The hostname could not be found, exiting the port scanner")
      sys.exit()
         
    except socket.error:
      print(Fore.RED + f"Could not connect to the server")
      sys.exit()

                  
port_scan(target_ip)        

scan_end = datetime.now()

print(Fore.MAGENTA + f"Port scan ended at: {scan_end}")
