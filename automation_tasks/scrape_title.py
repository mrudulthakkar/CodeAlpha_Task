import re
import requests

url = "https://www.google.com"
response = requests.get(url)

html = response.text  

# Regex pattern for title
pattern = r"<title>(.*)</title>"

match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)

if match:
    print("group(0):", match.group(0))   # whole match (<title>...</title>)
    print("group(1):", match.group(1))   # only the text inside
else:
    print("No title found")
