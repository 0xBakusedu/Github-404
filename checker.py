import requests
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def check_404_github(domain):
    url = f"https://{domain}/"
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        server = response.headers.get('Server', '')
        if response.status_code == 404 and "GitHub.com" in server:
            return True
    except requests.RequestException:
        pass
    return False

def banner():
    print(Fore.CYAN + Style.BRIGHT + "="*50)
    print(Fore.GREEN + Style.BRIGHT + "       GitHub 404 Checker".center(50))
    print(Fore.YELLOW + Style.BRIGHT + "       Coded by 0xBakusedu x WL".center(50))
    print(Fore.CYAN + Style.BRIGHT + "="*50 + "\n")

def main():
    banner()
    try:
        with open("list.txt", "r") as file:
            domains = [line.strip() for line in file if line.strip()]

        with open("404.txt", "w") as out:
            for domain in domains:
                if check_404_github(domain):
                    full_url = f"https://{domain}/"
                    print(Fore.RED + f"[404] {full_url}")
                    out.write(full_url + "\n")
                else:
                    print(Fore.GREEN + f"[OK ] https://{domain}/")
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Dihentikan oleh pengguna.")
        sys.exit(0)
    except FileNotFoundError:
        print(Fore.RED + "[!] File list.txt tidak ditemukan!")
        sys.exit(1)

if __name__ == "__main__":
    main()
