# CIP Project Team 10
## About
This repository contains the source code for the CIP project for team 10.

## Setup
To get started, install the required packages first using:

```
python setup.py install
```

## Usage
The pipeline runs using flags, which allows for detailed control.
See help `--help` or `-h` for more details.

```
usage: main.py [-h] [--complete] [--collect-all] [--collect-gdp]
               [--collect-health] [--collect-corona] [--integrate-all]
               [--integrate-gdp] [--integrate-health] [--integrate-corona]
               [--process-all] [--process-gdp] [--process-health]
               [--process-corona]

Runs the CIP project pipeline

optional arguments:
  -h, --help          show this help message and exit
  --complete          Runs complete pipeline
  --collect-all       Scrapes and downloads all the available data.
  --collect-gdp       Scrape the GDP data from Wikipedia.
  --collect-health    Scrape the health expenditure data from Wikipedia.
  --collect-corona    Downloads the Corona data
  --integrate-all     Cleans and prepares all the data.
  --integrate-gdp     Cleans and prepares the scraped GDP data.
  --integrate-health  Cleans and prepares the scraped health expenditure data.
  --integrate-corona  Cleans and prepares the downloaded corona data.
  --process-all       Processes and stores all the available data.
  --process-gdp       Processes and stores the scraped GDP data.
  --process-health    Processes and stores the scraped health expenditure
                      data.
  --process-corona    Processes and stores the downloaded corona data.

```

## Credits
The data herein presented has been obtained from various sources.

* Corona data: [https://github.com/CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)
* GDP data: [https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita)
* Health expenditure data: [https://en.wikipedia.org/wiki/List_of_countries_by_total_health_expenditure_per_capita](https://en.wikipedia.org/wiki/List_of_countries_by_total_health_expenditure_per_capita)