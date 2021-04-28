import numpy as np
import pandas as pd
import requests
import time
import os

from bs4 import BeautifulSoup



def anime_scraper(url, alt_attr, char_name, folder):

    time.sleep(5)

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    images = soup.find_all('img', attrs={
    'alt':alt_attr
    })

    image_urls = []

    for img in images:
        image_urls.append(img.attrs['data-src'])

    # Referenced from: https://www.thepythoncode.com/article/download-web-page-images-python
    # Referenced from: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests

    if not os.path.isdir(f'../../assets/{folder}'):
        os.makedirs(f'../../assets/{folder}')

    for url in image_urls:

        filename = os.path.join(f'../../assets/{folder}', url.split('/')[-1])

        time.sleep(5)

        res = requests.get(url, stream=True)

        with open(filename, 'wb+') as f:
            for chunk in res.iter_content(1024):
                f.write(chunk)
