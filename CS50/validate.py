import re

email = input("Enter Email: ").strip().lower()

if re.search(r"^\w+@(?:\w+\.)?\w+\.(?:edu|com|gov|net|org)$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
