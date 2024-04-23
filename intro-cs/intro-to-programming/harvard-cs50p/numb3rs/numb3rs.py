import re


def validate(ip):
    part = r"(\d{,2}|[0-1]\d{2}|2[0-4]\d|25[0-5])"
    is_valid = re.search(rf"^{part}\.{part}\.{part}\.{part}$", ip)
    return True if is_valid else False


def main():
    ip = input("IPv4 Address: ").strip()
    is_valid = validate(ip)
    print(is_valid)


if __name__ == "__main__":
    main()
