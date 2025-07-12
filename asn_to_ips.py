import requests
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.CYAN}
   ___   ____  _   _   _____ ____   ___  ____  
  / _ \\ |  _ \\| \\ | | | ____|  _ \\ / _ \\|  _ \\ 
 | | | || |_) |  \\| | |  _| | | | | | | | |_) |
 | |_| ||  _ <| |\\  | | |___| |_| | |_| |  _ < 
  \\___(_)_| \\_\\_| \\_| |_____|____/ \\___/|_| \\_\\
             ASN to IP Range Fetcher
    {Style.RESET_ALL}Author: Ghost  |  Tool: ASN IP Range Scraper
    """
    print(banner)

def get_ip_ranges(asn_number):
    url = f"https://api.bgpview.io/asn/{asn_number}/prefixes"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"{Fore.RED}[!] Failed to fetch data for ASN {asn_number}")
        return []

    data = response.json()
    ipv4 = [item["prefix"] for item in data["data"]["ipv4_prefixes"]]
    ipv6 = [item["prefix"] for item in data["data"]["ipv6_prefixes"]]
    return ipv4 + ipv6

def save_to_file(filename, ip_list):
    with open(filename, "w") as f:
        for ip in ip_list:
            f.write(f"{ip}\n")
    print(f"{Fore.GREEN}[+] Saved {len(ip_list)} IP ranges to {filename}")

def print_colorful_ips(ip_list):
    for ip in ip_list:
        if ":" in ip:
            print(f"{Fore.MAGENTA}{ip}")
        else:
            print(f"{Fore.CYAN}{ip}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get IP ranges for a given ASN")
    parser.add_argument("asn", help="Autonomous System Number (e.g., AS15169 or 15169)")
    parser.add_argument("-o", "--output", help="Output file name")

    args = parser.parse_args()
    asn_number = args.asn.upper().replace("AS", "")
    output_file = args.output or f"AS{asn_number}_ranges.txt"

    print_banner()
    ip_ranges = get_ip_ranges(asn_number)

    print(f"{Fore.YELLOW}[~] IP ranges for AS{asn_number}:\n")
    print_colorful_ips(ip_ranges)

    save_to_file(output_file, ip_ranges)
