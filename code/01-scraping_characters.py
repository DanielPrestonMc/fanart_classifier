# Scraping each specific character's images to be used in model

import numpy as np
import pandas as pd
import requests
import time

# importing anime scraper function creating in scraper.py file
from scraper import anime_scraper
from bs4 import BeautifulSoup

# using anime scraper function creating in scraper.py file to download image data for each specific individual character.

# # Monkey D. Luffy
anime_scraper('https://myanimelist.net/character/40/Luffy_Monkey_D/pictures',
            'Luffy "Mugiwara, Straw Hat, Lucy" Monkey D. picture',
            'luffy')

# Roronoa Zora
anime_scraper('https://myanimelist.net/character/62/Zoro_Roronoa/pictures',
            'Zoro "Pirate Hunter, Marimo" Roronoa picture',
            'zoro')

# Nami
anime_scraper('https://myanimelist.net/character/723/Nami/pictures',
            'Nami "Cat Burglar, Namizo"  picture',
            'nami')

# Sanji
anime_scraper('https://myanimelist.net/character/305/Sanji/pictures',
            'Sanji "Black Leg, Mr. Prince"  picture',
            'sanji')

# Nico Robin
anime_scraper('https://myanimelist.net/character/61/Robin_Nico/pictures',
            'Robin "Devil Child, Miss All Sunday" Nico picture',
            'robin')

# Franky
anime_scraper('https://myanimelist.net/character/64/Franky/pictures',
            'Franky "Cyborg, Cutty Flam, Bakanky"  picture',
            'franky')

# Tony Tony Chopper
anime_scraper('https://myanimelist.net/character/309/Chopper_Tony_Tony/pictures',
            'Chopper Tony Tony picture',
            'chopper')

# Brook
anime_scraper('https://myanimelist.net/character/5627/Brook/pictures',
            'Brook "Dead Bones, Soul King"  picture',
            'brook')

# Usopp
anime_scraper('https://myanimelist.net/character/724/Usopp/pictures',
            'Usopp "Sogeking, Sniper King, Usoland, God"  picture',
            'usopp')
