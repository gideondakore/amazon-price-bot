import requests
from bs4 import BeautifulSoup

class DataManager:
    def __init__(self):
        self.amazon_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
        self.title = ""
        self.total_amount = None
        self.scrape()


    def scrape(self):
        """ You can get these headers from this site: https://httpbin.org/headers"""
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Priority": "u=0, i",
            "Sec-Ch-Ua": "\"Not?A_Brand\";v=\"99\", \"Chromium\";v=\"130\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Linux\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        }

        # Make a request to Amazon
        response = requests.get(url=self.amazon_url, headers=headers)

        response.raise_for_status()
        data = response.text

        soup = BeautifulSoup(data, "html.parser")

        practice_whole_price = soup.find(name="span", class_="a-price-whole").get_text()
        practice_fraction_price = soup.find(name="span", class_="a-price-fraction").get_text()

        item_price = float(practice_whole_price + practice_fraction_price)
        self.title = soup.title.text
        self.total_amount = item_price






