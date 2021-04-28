import numpy as np
import pandas as pd
import requests
import time

from scraper import anime_scraper
from bs4 import BeautifulSoup


anime_scraper('https://myanimelist.net/character/40/Luffy_Monkey_D/pictures',
            'Luffy "Mugiwara, Straw Hat, Lucy" Monkey D. picture',
            'Luffy',
            'luffy')

anime_scraper('https://myanimelist.net/character/62/Zoro_Roronoa/pictures',
            'Zoro "Pirate Hunter, Marimo" Roronoa picture',
            'Zoro',
            'zoro')
