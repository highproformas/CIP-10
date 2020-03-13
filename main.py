import argparse
from cip.scraper import WikiGPDScraper, WikiHealthScraper

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Runs the CIP project pipeline")

    parser.add_argument("--scrape-all", help="Scrape all the available data.", action="store_true", dest="scrape_all")
    parser.add_argument("--scrape-gdp", help="Scrape the GDP data from Wikipedia.", action="store_true", dest="scrape_gdp")
    parser.add_argument("--scrape-health", help="Scrape the health expenditure data from Wikipedia.", action="store_true", dest="scrape_health")

    args = parser.parse_args()
    if args.scrape_gdp or args.scrape_all:
        scraper = WikiGPDScraper()
        scraper.scrape()

    if args.scrape_gdp or args.scrape_all:
        scraper = WikiHealthScraper()
        scraper.scrape()

    print('I am done here!')
