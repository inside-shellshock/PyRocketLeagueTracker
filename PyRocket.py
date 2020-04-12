import colorama
import os
import pyfiglet
from pyfiglet import figlet_format
import threading
from time import sleep
from requests import get
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Back, Style
init(convert=None)

valoriText = ["Tracker Score", "Gol/Tiri %", "Vittorie", "Gol", "Parate", "Tiri", "MVP", "Assist", "MVP/Vittore %", "Livello ricompensa"]
valori = []
valori2 = []


def Target_primario(url):
    global d
    sleep(0.5)
    response = get(url)
    html_soup = BeautifulSoup(response.text, "html.parser")
    for each_div in html_soup.find_all('div', {'class':'value'}):
        x = each_div.text
        valori.append(x.replace("\n", "").replace(" ", ""))

    d = dict(zip(valoriText, valori))
    print(f"\t\tStatistiche per: {Fore.MAGENTA}{target_nick}{Fore.WHITE}")
    for valore, chiave in d.items():
        print(f"{valore} : {Fore.MAGENTA}{chiave}{Fore.WHITE}")
    print()

def Target_secondario(url2):
    global d
    sleep(1)
    response = get(url2)
    html_soup = BeautifulSoup(response.text, "html.parser")
    for each_div in html_soup.find_all('div', {'class':'value'}):
        x = each_div.text
        valori2.append(x.replace("\n", "").replace(" ", ""))
    d2 = dict(zip(valoriText, valori2))
    print(f"\t\tStatistiche per: {Fore.CYAN}{target_nick2}{Fore.WHITE}")
    #print(Fore.RED, d2, Fore.WHITE)
    for valore, chiave in d2.items():
        print(f"{valore} : {Fore.CYAN}{chiave}{Fore.WHITE}")

if __name__ == "__main__":
    os.system("cls")
    print(figlet_format("Rocket League Tracker", font="small"), end="")
    global target_nick
    global target_nick2
    target_nick = ""
    target_nick2 = ""
    print()
    url = "https://rocketleague.tracker.network/profile/ps/" + target_nick
    url2 = "https://rocketleague.tracker.network/profile/ps/" + target_nick2
    try:
        thread1 = threading.Thread(target=Target_primario, args=(url,))
        thread2 = threading.Thread(target=Target_secondario, args=(url2,))

        thread1.start()
        thread2.start()
    except Exception as msg:
        print(msg)
