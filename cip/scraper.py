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
        df.to_csv('./data/gdp_raw.csv', sep='|', header=True, index=False)
        print('GDP Scrape done!')

class WikiHealthScraper(Scraper):
    def __init__(self, url='https://en.wikipedia.org/wiki/List_of_countries_by_total_health_expenditure_per_capita'):
        super().__init__(url)
        print('Setup Wiki Health Expenditure Scraper')

    def scrape(self):
        soup = super().scrape()
        data = []
        table = soup.find(id='WHO2')

        for row in table.select(selector='tr'):
            cells = row.select(selector='td')

            if len(cells) >= 4:
                name = ((cells[0]).select(selector='a')[0]).text.strip()
                value_2k = (cells[1]).text.strip()
                value_2k5 = (cells[2]).text.strip()
                value_2k10 = (cells[3]).text.strip()
                value_2k15 = (cells[4]).text.strip()
                data.append({'name': name, '2000': value_2k, '2005': value_2k5, '2010': value_2k10, '2015': value_2k15})
        df = pd.DataFrame(data, columns=['name', '2000', '2005', '2010', '2015'])
        df.head()
        df.to_csv('./data/health_raw.csv', sep='|', header=True, index=False)
        print('Health Expenditure Scrape done!')
