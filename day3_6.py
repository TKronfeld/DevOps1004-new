import requests
try:
    requests.get("JJJHJ; jkjkjkj")
except requests.exceptions.MissingSchema:
    print("missing scheme in URL")