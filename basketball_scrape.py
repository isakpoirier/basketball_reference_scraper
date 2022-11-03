import subprocess
from dotenv import load_dotenv
from libs.scraper_utils import run_scrape

OUTPUT_LOCATIONS = [
    os.getenv("GAME_LOGS"), 
    os.getenv("ROSTERS"),
    os.getenv("TEAM_STATS"),
    os.getenv("OPP_STATS")

]

class DataScraper:
    def __init__(self):
        self.years = [2019, 2020, 2021, 2022, 2023]

    def run_scrape():
        scrape_data(output_loc = OUTPUT_LOCATIONS,
            years = self.years)