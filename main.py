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



quinn_url = ('https://www.shutupandsitdown.com/videos/quinns-walks-you-through-his-game-collection/')





def get_vasel_top_list():
    i = 0
   
    for i in range (91):
        vasel_range_one = (i+10)
        vasel_range_two = (i+1)
        vasel_top_index = ('{}-{}'.format(vasel_range_one, vasel_range_two))
        vasel_url = ('https://www.dicetower.com/game-video/tom-vasels-top-100-games-all-time-2021-{}'.format(vasel_top_index))
        response1 = requests.get(vasel_url)
        src1 = response1.content
        soup1 = BeautifulSoup(src1, 'html.parser')
        links = soup1.find_all(class_='gt_title')
        for link in links:
            if "" in link.text:
                print(link.text)
                i += 10
                get_vasel_top_list

get_vasel_top_list()

 