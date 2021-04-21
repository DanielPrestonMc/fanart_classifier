import numpy as np
import pandas as pd
import requests

from bs4 import BeautifulSoup

name = 'Zoro'
url = 'https://myanimelist.net/character/62/Zoro_Roronoa/pictures'
alt_attr = 'Zoro "Pirate Hunter, Marimo" Roronoa picture'

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
