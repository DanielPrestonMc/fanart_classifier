# Creating scraper function to be used in separate file to scrape specific character images.

import numpy as np
import pandas as pd
import requests
import time
import os

from bs4 import BeautifulSoup


# function that takes the website url to be scraped, specify the attribute for corresponding image(img) data to be scraped, & name of folder to save image files to locally.
def anime_scraper(url, alt_attr, folder):

    time.sleep(3)

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    # sorting through scraped page content for specific image data with `alt_attrs` attributes.
    images = soup.find_all('img', attrs={
    'alt':alt_attr
    })

    # appending each image url to a list to be used for downloading into specific folder
    image_urls = []

    for img in images:
        image_urls.append(img.attrs['data-src'])

    # Referenced from: https://www.thepythoncode.com/article/download-web-page-images-python
    # Referenced from: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests

    # creates new folder to download images to if folder does not already exist.
    if not os.path.isdir(f'../assets/{folder}'):
        os.makedirs(f'../assets/{folder}')

    # loop through list of image urls
    for url in image_urls:

        # specify the folder and file name(the same file name at the very end of the url) to download images to
        filename = os.path.join(f'../assets/{folder}', url.split('/')[-1])

        time.sleep(2)

        # new get request for each image
        res = requests.get(url, stream=True)

        # saving image data to specified file and folder with appropriate permissions.
        with open(filename, 'wb+') as f:
            for chunk in res.iter_content(1024):
                f.write(chunk)




def anime_scraper_2(url_folder, alt):

    for i in url_folder:
        time.sleep(3)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
            }

        soup = BeautifulSoup(requests.get(i[0], headers=headers).content,
                            'html.parser')

        images = soup.find_all('img', attrs={
        'alt': alt
        })

        image_urls = [img.attrs['src'] for img in images]

        if not os.path.isdir(f'../assets/{i[1]}'):
            os.makedirs(f'../assets/{i[1]}')

        for url in image_urls:
            new_path = 'https://ami.animecharactersdatabase.com/uploads/chars/'
            img_name = url.split('/')[-1]

            filename = os.path.join(f'../assets/{i[1]}', img_name)

            time.sleep(2)

            res = requests.get(new_path + img_name,
                                stream=True,
                                headers=headers)

            with open(filename, 'wb+') as f:
                for chunk in res.iter_content(1024):
                    f.write(chunk)
