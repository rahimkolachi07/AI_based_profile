import requests
from bs4 import BeautifulSoup
import re

def extract_emails(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        unique_emails = list(set(emails))
        return unique_emails, text
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")
        return [], ""

