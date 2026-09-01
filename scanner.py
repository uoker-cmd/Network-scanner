import socket
import argparse
from datetime import datetime


def scan_port(target, port, timeout=0.5):
    """
    Check whether a TCP port is open.
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((target, port))

        if result == 0:
            return True

    except socket.error:
        return False

    finally:
        sock.close()

    return False


def main():
    parser = argparse.ArgumentParser(
        description="TCP Network Scanner"
    )

    parser.add_argument(
        "target",
        help="Target IP address or hostname"
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-1024",
        help="Port range, example: 1-1000"
    )

    args = parser.parse_args()

    target = args.target

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[!] Could not resolve target.")
        return

    try:
        start_port, end_port = map(
            int,
            args.ports.split("-")
        )
    except ValueError:
        print("[!] Invalid port range.")
        print("[*] Example: -p 1-1000")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("[!] Invalid port range.")
        return

    print("=" * 55)
    print("        PYTHON NETWORK SCANNER")
    print("=" * 55)

    print(f"Target   : {target}")
    print(f"IP       : {target_ip}")
    print(f"Ports    : {start_port}-{end_port}")
    print(f"Started  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 55)

    open_ports = []

    for port in range(start_port, end_port + 1):

        if scan_port(target_ip, port):
            print(f"[+] Port {port:<5} OPEN")
            open_ports.append(port)

    print("-" * 55)

    if open_ports:
        print(f"[+] Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("[-] No open ports found.")

    print("=" * 55)


if __name__ == "__main__":
    main()
