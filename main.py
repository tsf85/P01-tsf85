#import urllib
import pathlib
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





def clear_vasel_list():
    file = open("Vasel_list.txt", "w")
    file.close()

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
                file = open("Vasel_list.txt", "a") 
                file.write(str(link.text))
                file.write('\n')
                file.close()
                #print(link.text)
                i += 10
                get_vasel_top_list


get_vasel_top_list()
#clear_vasel_list()

def clear_quinn_list():
    file = open("Quinn_list.txt", "w")
    file.close()

def get_quinn_top_list():
    quinn_url = ('https://www.shutupandsitdown.com/videos/quinns-walks-you-through-his-game-collection/')
    response2 = requests.get(quinn_url)
    src2 = response2.content
    soup2 = BeautifulSoup(src2, 'html.parser')
    links = soup2.find_all('strong')
    for link in links:
        if "" in link.text:
            file = open("Quinn_list.txt", "a") 
            file.write(str(link.text))
            file.write('\n')
            file.close()
            #print(link.text)

#get_quinn_top_list()
#clear_quinn_list()
 