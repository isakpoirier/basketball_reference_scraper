import basketball_scrape as scraper
from basketball_scrape import DataScraper

def start():
    daily_scrape = scraper.DataScraper()
    daily_scrape.run_scrape()


if __name__ == "__main__":
    start() 