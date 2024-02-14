import requests
from bs4 import BeautifulSoup

url = "https://cloud.google.com/asset-inventory/docs/supported-asset-types"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

a_tags = soup.find_all('a')
for a_tag in a_tags:
    code_tags_within_a = a_tag.find_all('code')
    for code_tag in code_tags_within_a:
        print(code_tag.get_text())
