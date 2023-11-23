import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        embedded_url = re.search(r'^<iframe src="(https?://(?:www\.)?youtube\.com/)(?:embed/)(\w+)"></iframe>$', s)
        url = re.sub(r"https?://(www\.)?youtube\.com/", "https://youtu.be/", embedded_url.group(1))

        return url + embedded_url.group(2)
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
