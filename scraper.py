import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def main():

    url = "https://www.plymouth.ac.uk/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except RequestException as e:
        print(f"Request error: {e}")
        return
    
    response  = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    page_title = soup.title.string

    print(f"Page Title: {page_title}")

    headings = soup.find_all('h1')
    for h1 in headings:
        print(h1.get_text(strip=True))


if __name__ == "__main__":
    main()
