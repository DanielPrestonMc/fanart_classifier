# Scraping each specific character's images to be used in model

import numpy as np
import pandas as pd
import requests
import time

# importing anime scraper function creating in scraper.py file
from scraper import anime_scraper_2
from bs4 import BeautifulSoup

# create list of tuples containing page to be scraped and name of character for corresponding page
url_folder = [
    ('https://www.animecharactersdatabase.com/photo.php?cid=20337', 'brook'),
    ('https://www.animecharactersdatabase.com/photo.php?cid=28642', 'chopper'),
    ('https://www.animecharactersdatabase.com/photo.php?cid=12437', 'franky'),
    ('https://www.animecharactersdatabase.com/photo.php?cid=10607', 'luffy'),
    ('https://www.animecharactersdatabase.com/photo.php?cid=12439', 'nami'),
    ('https://www.animecharactersdatabase.com/photo.php?cid=12441', 'robin'),
    ('https://www.animecharactersdatabase.com/photo.php?cid=12443', 'sanji'),
    ('https://www.animecharactersdatabase.com/photo.php?cid=12445', 'usopp'),
    ('https://www.animecharactersdatabase.com/photo.php?cid=12442', 'zoro')
]


# using anime scraper function creating in scraper.py file to download image data for each individual character in list.
anime_scraper_2(url_folder, 'Image of')
