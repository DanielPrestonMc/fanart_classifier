# 'One Piece' Fanart Classification Project
### *by Daniel Preston McBride*
https://www.linkedin.com/in/danielpmcbride/

---

## Contents:

- [Background/Problem Statement](#Background-&-Problem-Statement)
- [The Data](#The-Data)
- [Jupyter Lab Notebook Files](#Jupyter-Lab-Notebook-Files)
- [Python Libraries & Packages](#Python-Libraries-&-Packages)
- [Image Scraping & Transformation](#Image-Scraping-&-Transformation)
- [Modeling](#Modeling)
- [Results](#Results)
- [Application](#Application)
- [Conclusion](#Conclusion)

---

## Background & Problem Statement

Anime fans are some of the most loyal and dedicated fanbase that exists. Many fans take that dedication to new levels, such as creating cosplay, fan fiction, or community meetup groups and unofficial fan accounts and subreddits.  One talented group of fans also use their creativity and skills to express their own unique perspective of their favorite characters through fanart.

What is the measure of good fanart though? How much does it matter that the character in the illustration actually represents the original character? And in this project specifically, how well can image classification utilizing a neural network perform with anime character fanart created in unique and stylish ways but still representing the original character?

The goal of this project is to develop an application that allows 'One Piece' fanart illustrators to submit their creations (the wilder and crazier the better!) and see how accurately the app can classify the artwork by character.

---

## The Data

The training image data was scraped from https://myanimelist.net/.

[Luffy Image Data](data/luffy/) - This folder contains image data for the character 'Luffy'.
<br>
[Zoro Image Data](data/zoro/) - This folder contains image data for the character 'Zoro'.
<br>
[Nami Image Data](data/nami/) - This folder contains image data for the character 'Nami'.
<br>
[Sanji Image Data](data/sanji/) - This folder contains image data for the character 'Sanji'.
<br>
[Chopper Image Data](data/chopper/) - This folder contains image data for the character 'Chopper'.
<br>
[Robin Image Data](data/robin/) - This folder contains image data for the character 'Robin'.
<br>
[Franky Image Data](data/franky/) - This folder contains image data for the character 'Franky'.
<br>
[Brook Image Data](data/brook/) - This folder contains image data for the character 'Brook'.
<br><br>
[Usopp Image Data](data/usopp/) - This folder contains image data for the character 'Usopp'.
<br><br>

---

## Jupyter Lab Notebook Files

[Python File for Scraper Function](code/scraping/scraper.py)
<br>
[Python File for Scraping Character Image Data](code/scraping/01-scraping_characters.py)
<br>
[Python File for CNN Model](code/02-cnn_model.py)
<br>
[Python File for Flask App Deployment](flask_app/cap_app.py)
<br>

---

## Python Libraries & Packages

Numpy, Pandas, Requests, Time, os, bs4(BeautifulSoup), TensorFlow, Sklearn

---

## Image Scraping & Transformation

The training image data was scraped from https://myanimelist.net/ using Beautiful Soup(bs4). A scraper function was constructed that could accept a character's specific html attributes so too much data is not scraped. From there, the images were downloaded locally using the request.get method on the image url. A tensorflow preprocessing method called image_dataset_from_directory converted the local images to tensor array data, which was then converted to numpy array data for use with the neural network model. But before the array data could be used, it was wise to transform the contents of each arrays from values between 0 and 255 to values between 0 and 1. Neural networks usually do a better job working with data in these ranges.

---

## Modeling

The decision was made to utilize a Convolutional Neural Network, which is usually best for image data.  First, Conv2D layers with MaxPooling2D layers were built out to add a variety of filters to each piece of image data that the model can train on.  This allows for better adaptation to more obscure pieces of test image data.  After adding a Flatten layer to make the data accessible for input into the dense neural network, dense layers and dropout layers were added to train the model.

---

## Results

The model was measured on the accuracy of predicting the correct category(or character) for each piece of image data.  The model had a best performance score of 66% on the testing data.

---

## Application

The web application was deployed using Flask and loaded in our trained model to accept new image data to predict on via a file input html button.  After a new file was submitted, it was ran through the model using the model.predict method.  The next screen of the web app will print out the character name prediction in text as well as posting the user submitted image side by side with an actual character image used to originally train the model.

---

## Conclusion

This experiment can be limited by local or cloud storage capacity for image data as well as CPU processing power for deeper neural network computations on larger amounts of data.

Risks for the experiment can include potential copyright infringement issues with character owners, depending on the intended deployment of the application.  Also, using user-created fanart without proper authorization could lead to potential roadblocks in testing, as well as locally saving user submitted images without properly communicating with users.  Another potential larger risk with using a model like this is training on image data of real people and using this application to potential track and spy on the whereabouts of actual, private citizens.

We can assume that the model will never perform with 100% accuracy because the user submitted images may have varying degrees of character recognition based on the artistic abilities of the user or purposefully obscuring a character illustration through creative expression.  With more image data being trained on by the model, particularly the more obscure characterization images, then better the model may be at prediction more unique illustrations.
