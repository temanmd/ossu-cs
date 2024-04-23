import re


def count(string):
    regex = r"\b(um)\b"
    matches = re.findall(regex, string, flags=re.I)
    if not matches:
        return 0
    return len(matches)


def main():
    string = input("Input: ").strip()
    print(count(string))


if __name__ == "__main__":
    main()
