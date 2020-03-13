import os
import pandas as pd
from abc import ABC
from urllib.parse import urlparse

class Downloader(ABC):
    def __init__(self, data):
        self.data = data

    @classmethod
    def fromURLList(cls, urls):
        return cls(urls)

    @classmethod
    def fromURLString(cls, url):
        return cls([url])

    def download(self):
        pass

class CoronaDownloader(Downloader):
    def __init__(self, data):
        super().__init__(data)
        print('Setup Corona Downloader')

    def download(self):
        for url in self.data:
            _url = urlparse(url)
            filename = os.path.basename(_url.path)
            df = pd.read_csv(url, sep=',')
            df.to_csv(os.path.join('./data/',filename))
        print('Corona Download done!')