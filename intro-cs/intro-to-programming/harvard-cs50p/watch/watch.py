import re


def parse(html):
    regex = r"src=\"http[s]?:\/\/(www\.)?youtube\.com\/embed\/(\w+)\""
    matches = re.search(regex, html)

    if not matches: return None

    code = matches.group(2)
    return f"https://youtu.be/{code}"


def main():
    html = input("HTML: ").strip()
    video_url = parse(html)
    print(video_url)


if __name__ == "__main__":
    main()
