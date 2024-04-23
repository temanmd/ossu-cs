import sys
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

number = sys.argv[1]

try:
    count = float(number)
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(url)
except requests.RequestException:
    sys.exit("Request error")

data = response.json()
price = data["bpi"]["USD"]["rate_float"]
amount = count * price

print(f"${amount:,.4f}")
