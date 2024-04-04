import requests
import random
from datetime import datetime
from colorama import Fore
import json

GREEN = Fore.GREEN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Fore.RESET
MAGENTA = Fore.MAGENTA

with open('info.json', 'r') as file:
    data = json.load(file)

server_id = data['server_vote_link']
d_id = data['d_id']

def main():
    date_and_time = datetime.now()
    time = date_and_time.strftime('%H:%M:%S')
    proxies_file = open('proxies.txt', 'r')
    proxies_list = [line.strip() for line in proxies_file.readlines()]
    random.shuffle(proxies_list)
    for proxy in proxies_list:
        ip, port = proxy.split(":")
        proxy = f"http://{ip}:{port}"
        proxies = {
            "http": proxy,
            "https": proxy,
        }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Origin': 'https://discordbee.com',
        'Referer': f'https://discordbee.com/servers?server={server_id}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_8_9; en-US) AppleWebKit/536.39 (KHTML, like Gecko) Chrome/52.0.1972.231 Safari/535'
    }
    while True:
        try:
            form_url = f"https://discordbee.com/voting?server={server_id}&vote=1&d={d_id}"

            form_payload = {
                "server": server_id,
                "vote": "1",
                "d": d_id
            }

            response = requests.get(form_url, data=form_payload, proxies=proxies, headers=headers)
            if response.status_code == 200 or 302:
                print(f"[{BLUE}{time}{RESET}] [{GREEN}SUCCESS{RESET}] [{YELLOW}Added vote!{RESET}]")
            else:
                print(f"[{BLUE}{time}{RESET}] [{RED}ERROR{RESET}] [{YELLOW}Vote could not be added{RESET}]")
        except Exception as e:
            print(f"[{BLUE}{time}{RESET}] [{RED}ERROR{RESET}] [{YELLOW}{e}{RESET}]")
            continue


if __name__ == "__main__":
    main()
