import requests
import pyfiglet
from rich import print

title = "HTTP STATUS CHECK"
banner_art1 = pyfiglet.figlet_format(title, font="pagga", width=100)

banner_art2 = """         
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
"""

print (f"[bold rgb(95,135,215)]{banner_art1}[/bold rgb(95,135,215)]")
print (f"[rgb(95,135,215)]{banner_art2}[rgb(95,135,215]")

try:

  url = input("Enter the URL: ").strip()

  r = requests.get(url, timeout=10)

  if r.status_code == 200:
   print(f"[bold green][+] Connection to {url} Successful.[/bold green] HTTP Status Code: {r.status_code}")

  elif r.status_code == 401:
   print(f"[bold yellow][-] Connection to {url} is Unauthorized.[/bold yellow] HTTP Status Code: {r.status_code}")

  elif r.status_code == 403:
   print(f"[bold yellow][-] Connection to {url} is Forbidden, you do not have permission![/bold yellow] HTTP Status Code: {r.status_code}")

  elif r.status_code == 404:
   print(f"[bold red][-] Connection to {url} Cannot be found.[/bold red] HTTP Status Code: {r.status_code}")
   
  elif r.status_code == 500:
   print(f"[bold red][-] Connection to {url}: Internal Server Error![/bold red] HTTP Status Code: {r.status_code}") 

  else:
   print(f"Connection to {url} failed. HTTP Status Code: {r.status_code}")
   
except requests.exceptions.RequestException as e:
   print(f"[bold red][-] Error during the request:[/bold red] {e}")
       
except KeyboardInterrupt:
   print(f"[bold red][-] You have exited the program.[/bold red]")
