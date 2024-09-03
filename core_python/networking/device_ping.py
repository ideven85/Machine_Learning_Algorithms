import os
from logging import Logger


#fixme
#Error sh command not found
def ping_device(ip_address):
    log = Logger("general")
    response = os.system("Pinging 1" + ip_address)
    if response==0:
        log.info(f"Device {ip_address} is reachable")
    else:
        log.warning(f"Device {ip_address} out of reach")


def main():
    ping_device("localhost")

if __name__ == '__main__':
    main()
