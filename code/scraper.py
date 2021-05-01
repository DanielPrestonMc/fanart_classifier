# Creating scraper function to be used in separate file to scrape specific character images.

import numpy as np
import pandas as pd
import requests
import time
import os

from bs4 import BeautifulSoup


# function that takes the website url to be scraped, specify the attribute for corresponding image(img) data to be scraped, & name of folder to save image files to locally.
def anime_scraper(url, alt_attr, folder):

    time.sleep(5)

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
