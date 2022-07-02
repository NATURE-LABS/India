"""
Purpose : Google Connect temples data to the Google Search Engine.
States and Union Territories : Collecting the temple locations.
Temples data is needed for the googlengine.com collect the Temple Name. Temple Location,
Co-ordinates, Distance from major cities to the temple location.

Design and developed by :
Kyndryl Solutions Private Limited
Project Team : Google Cloud Platform - Guild.
Lab : Nature Labs @ GCP
How to use
------------
python googlengine.py https://www.googlengine.com/ind

Contact 
--------
Kyndryl GCP Guild Moderator : Ramamurthy V 
Email           : ramamurthy.valavandan@kyndryl.com
GCP Contact     : gcpguild@gmail.com
Date            : June 8 2022.
Contributors    : 42 key members from GCP Guild.
Revised         : Google Cloud Projects, Hyper Scaler, Kyndryl
Date            : July 02 2022.

"""
from pathlib import Path

import requests, re, csv, sys

import pandas as pd
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import numpy as np
from bs4 import BeautifulSoup
import requests, json, lxml
from pathlib import Path


basepath = "C:"
codepath="google"
function = "serpapi"
N="\\"
namefile = "indias"
max_gs = 10 # maximum number of google search in href or urls
#-----------------------------------------------------
indiatempledatadir = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,namefile,N,"data"))

datadirgoo = ("{}{}{}".format(namefile.capitalize(),"_","googlengine_temple_States_and_UTs"))

googledataindiastutdir = ("{}{}{}".format(indiatempledatadir,N,datadirgoo))

cre_directory = Path(googledataindiastutdir)
cre_directory.mkdir(parents=True, exist_ok=True)

indiastautfile = ("{}{}{}".format(googledataindiastutdir,N,"Ind_googlengine_states_ut_master.csv"))
#-----------------------------------------------------

searchpg = "https://www.googlengine.com/ind"

gourl = re.sub(r'^.+/([^/]+)$', r'\1', searchpg)


def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")

def googlenginein(sek):
    if (sek == 'go'):
        website = requests.get(searchpg)
        soup = BeautifulSoup(website.content, 'html.parser')

        bese= soup.prettify()

        #print(bese)
        lt = "&lt;"
        gt = "&gt;"

        bese = re.sub(lt, '<', bese)
        bese = re.sub(gt, '>', bese)

        mano = []

        patten = ("{}{}{}".format('<h3>', "([^$]*)", '</h3>'))

        bese = re.findall(patten, str(bese))

        bese = re.sub('<h3>', '', str(bese))

        bese = re.sub('</h3>', '|', str(bese))
        bese = re.sub('&amp;', 'and', str(bese))

        bese = re.sub('[^A-Za-z|,]+', ' ' , str(bese))


        mano = [ x.strip() for x in bese.strip('[]').split('|') ]

        templeslist =  []

        n = 0
        for t in (mano):
            
            if (n != 0):
            
                if (t not in templeslist):
                    templeslist.append(t)

                else:
                    print("Duplicate is removed", t)
            n =+ 1

        #print(templeslist)
        colheader = ['States and Union Territories in India']
        gencsv = pd.DataFrame(templeslist,  columns= colheader )
        gencsv.to_csv(indiastautfile, index=False, na_rep='Unknown')

path = Path(indiastautfile)

if path.is_file():
    pi="\'India States and UTs data : \' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    
else:
    pi="\'Creating data of States and UTs !\' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    googlenginein(sek='go')
