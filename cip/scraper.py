import requests
from abc import ABC
import pandas as pd
from bs4 import BeautifulSoup


class Scraper(ABC):
    def __init__(self, url):
        self.url = url

    def scrape(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

class WikiGPDScraper(Scraper):
    def __init__(self, url='https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita'):
        super().__init__(url)
        print('Setup Wiki GDP Scraper')

    def scrape(self):
        soup = super().scrape()
        data = []
        for idx, table in enumerate(soup.findAll(name='table', attrs={'class': 'wikitable sortable'})):
            relevant = False
            # There are multiple tables, not all of which are relevant
            for headers in table.findAll(name='th'):
                # The relevant tables contain a column 'Int$'
                if headers.text.strip() == 'Int$':
                    relevant = True
            if relevant:
                # get the data (skipping the first td as it is not relevant)
                rows = []
                for row in table.select(selector='tr'):
                    cells = row.select(selector='td')[1:]
                    if len(cells) >= 2:
                        name = ((cells[0]).select(selector='a')[0]).text.strip()
                        amount = (cells[1]).text.strip()
                        rows.append({'table': idx, 'name': name, 'amount': amount})
                if len(rows) > 0:
                    data.extend(rows)
        df = pd.DataFrame(data, columns=['table', 'name', 'amount'])
        df.to_csv('./data/gdp.csv', sep='|', header=True, index=False)
