import argparse
from cip.scraper import WikiGPDScraper

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Runs the CIP project pipeline")

    parser.add_argument("--no-scraping", help="Skips the scrapping part.",
                        action="store_true", dest="not_scraping")

    args = parser.parse_args()
    if not args.not_scraping:
        scraper = WikiGPDScraper()
        scraper.scrape()
        print('Done scraping!')
    else:
        print('Done!')
