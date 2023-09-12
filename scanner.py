import socket
import optparse
import signal
import sys
from colorama import Fore, Style

def def_handler(sig, frame):
    print(Fore.RED + "\n\n[!] Exiting...\n" + Style.RESET_ALL)
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="Enter the IP of the target")

    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error(Fore.RED + "[!] Enter a valid IP, use --help for more information" + Style.RESET_ALL)
    return options

def make_scan(ip):
    print(Fore.CYAN + "\n\n[+] Scanning ports on %s...\n" % (ip) + Style.RESET_ALL)
    for port in range(1, 65535):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1000)
            s.connect((ip, port))
            print(Fore.YELLOW + "[+] PORT %d: " % (port) + Fore.GREEN + "OPEN\n" + Style.RESET_ALL)
        except:
            continue

if __name__ == '__main__':
    options = get_arguments()   
    make_scan(options.ip)
