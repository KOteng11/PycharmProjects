import re


url = input("URL: ").strip()

if username := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, flags=re.IGNORECASE):
    print(f"Username: {username.group(1)}")
