import argparse
from cip.collect.downloader import CoronaDownloader
from cip.collect.scraper import WikiGPDScraper, WikiHealthScraper

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Runs the CIP project pipeline")

    parser.add_argument("--complete", help="Runs complete pipeline", action="store_true", dest="complete")

    parser.add_argument("--collect-all", help="Scrapes and downloads all the available data.", action="store_true", dest="collect_all")
    parser.add_argument("--collect-gdp", help="Scrape the GDP data from Wikipedia.", action="store_true", dest="collect_gdp")
    parser.add_argument("--collect-health", help="Scrape the health expenditure data from Wikipedia.", action="store_true", dest="collect_health")
    parser.add_argument("--collect-corona", help="Downloads the Corona data", action="store_true", dest="collect_corona")

    parser.add_argument("--integrate-all", help="Cleans and prepares all the data.", action="store_true", dest="integrate_all")
    parser.add_argument("--integrate-gdp", help="Cleans and prepares the scraped GDP data.", action="store_true", dest="integrate_gdp")
    parser.add_argument("--integrate-health", help="Cleans and prepares the scraped health expenditure data.", action="store_true", dest="integrate_health")
    parser.add_argument("--integrate-corona", help="Cleans and prepares the downloaded corona data.", action="store_true", dest="integrate_corona")

    parser.add_argument("--process-all", help="Processes and stores all the available data.", action="store_true", dest="process_all")
    parser.add_argument("--process-gdp", help="Processes and stores the scraped GDP data.", action="store_true", dest="process_gdp")
    parser.add_argument("--process-health", help="Processes and stores the scraped health expenditure data.", action="store_true", dest="process_health")
    parser.add_argument("--process-corona", help="Processes and stores the downloaded corona data.", action="store_true", dest="process_corona")

    args = parser.parse_args()

    if args.collect_gdp or args.collect_all or args.complete:
        scraper = WikiGPDScraper()
        scraper.scrape()

    if args.collect_health or args.collect_all or args.complete:
        scraper = WikiHealthScraper()
        scraper.scrape()

    if args.collect_corona or args.collect_all or args.complete:
        url_list = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv',
                   'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv',
                   'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv']
        downloader = CoronaDownloader.fromURLList(url_list)
        downloader.download()

    if args.integrate_gdp or args.integrate_all or args.complete:
        print('Integration not yet implemented')
        
    if args.integrate_health or args.integrate_all or args.complete:
        print('Integration not yet implemented')
        
    if args.integrate_corona or args.integrate_all or args.complete:
        print('Integration not yet implemented')
        
    if args.process_gdp or args.process_all or args.complete:
        print('Process not yet implemented')
        
    if args.process_health or args.process_all or args.complete:
        print('Process not yet implemented')
        
    if args.process_corona or args.process_all or args.complete:
        print('Process not yet implemented')

    print('Done')
