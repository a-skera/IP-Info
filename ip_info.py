
import ipaddress
import socket
import argparse


def analyze_ip(ip):
    try:
        address = ipaddress.ip_address(ip)

        print("\n========== IP INFORMATION ==========")
        print(f"IP Address:  {address}")
        print(f"Version:     IPv{address.version}")
        print(f"Private:     {address.is_private}")
        print(f"Public:      {address.is_global}")
        print(f"Loopback:    {address.is_loopback}")
        print(f"Multicast:   {address.is_multicast}")
        print(f"Reserved:    {address.is_reserved}")
        print(f"Unspecified: {address.is_unspecified}")

        print("\n========== DNS INFORMATION ==========")

        try:
            hostname = socket.gethostbyaddr(str(address))[0]
            print(f"Hostname: {hostname}")

        except socket.herror:
            print("Hostname: No reverse DNS record found")

        except OSError as error:
            print(f"DNS Error: {error}")

        print("=====================================")

    except ValueError:
        print("[ERROR] Invalid IP address.")


def main():
    parser = argparse.ArgumentParser(
        description="IP Address Information Tool"
    )

    parser.add_argument(
        "ip",
        help="IP address to analyze"
    )

    args = parser.parse_args()
    analyze_ip(args.ip)


if __name__ == "__main__":
    main()
