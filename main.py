#import urllib
import requests
from bs4 import BeautifulSoup
#import urllib.request, urllib.parse, urllib.error
from csv import writer
#import datetime
#import os
#from os.path import isfile, join
import csv
#import shutil
#import sqlite3

vasel_range_one = (10)
vasel_range_two = (1)
vasel_top_index = ('{}-{}'.format(vasel_range_one, vasel_range_two))

vasel_url = ('https://www.dicetower.com/game-video/tom-vasels-top-100-games-all-time-2021-{}'.format(vasel_top_index))
quinn_url = ('https://www.shutupandsitdown.com/videos/quinns-walks-you-through-his-game-collection/')

response1 = requests.get(vasel_url)
#html1 = response1.read()
soup1 = BeautifulSoup(response1.text, "html.parser")

titles = soup1.find_all(class_='gt_title')

for div in titles:
    game = soup1.find('a').get_text().replace('\n', '')
print(game)


    
       



    

 