import numpy as np
import pandas as pd
import requests

from bs4 import BeautifulSoup

name = 'Luffy'
url = 'https://myanimelist.net/character/40/Luffy_Monkey_D/pictures'
alt_attr = 'Luffy "Mugiwara, Straw Hat, Lucy" Monkey D. picture'

def scraper(url=url, alt_attr=alt_attr, name=name):
    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')

    images = soup.find_all('img', attrs={
    'alt':alt_attr
    })

    image_list = {
        'name':name,
        'url': []
        }

    for i in images:
        image_list['url'].append(i.attrs['data-src'])

    image_df = pd.DataFrame(image_list)

    image_df.to_csv(f'../../data/{name}_data.csv', index=False)



scraper()
