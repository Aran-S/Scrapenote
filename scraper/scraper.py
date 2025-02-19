class WebScraper:
    def __init__(self):
        pass

    def fetch_data(self, url):
        import requests
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch data from {url}")

    def parse_data(self, raw_data):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(raw_data, 'html.parser')
        return soup.get_text()