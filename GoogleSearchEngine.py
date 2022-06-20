"""
Purpose : Google Connect is a utility to connect to the Google Search Engine.
Generate the csv data based on the search query given in the argument.
The demonstrated  program generate the datasheet in  a format in CSV.

Design and developed by :
Kyndryl Solutions Private Limited
Project Team : Google Cloud Platform - Guild.
Lab : Nature Labs @ GCP
How to use
------------
python googlegeneratetempledata.py 

Contact 
--------
Kyndryl GCP Guild Moderator : Ramamurthy V 
Email           :  ramamurthy.valavandan@kyndryl.com
GCP Contact     : gcpguild@gmail.com
Date            : June 8 2022.
Contributors    : 42 key members from GCP Guild.
"""
import requests, lxml, json, re, csv, sys,time
from bs4 import BeautifulSoup
from collections import OrderedDict
from pathlib import Path

import pandas as pd

import bs4 as bs
import urllib.request

import numpy as np

import requests
from urllib.error import URLError

mim = "top 25 temples in "

searchengine = 'https://www.google.com/search'

def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")

try:
  response = requests.get(searchengine)
  response.raise_for_status()
except URLError as ue:
  pi="\'The Search Engine is not reachable \' :"
  p = ("{} {}".format(pi,searchengine))
  prt(p)
  
  exit(1)
   
else:
  pi="\'The Search Engine is reachable \' :"
  p = ("{} {}".format(pi,searchengine))
  prt(p)




basepath = "C:"
codepath="python"
function = "indias"
N="\\"
namefile = "india"
max_gs = 10 # maximum number of google search in href or urls
google_json = "google-domains.json"

searchpg = "https://www.googlengine.com/ind"

gourl = re.sub(r'^.+/([^/]+)$', r'\1', searchpg)

indiatempledatadir = ("{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,"data",N))

indiastautfile = ("{}{}_{}".format(indiatempledatadir,gourl.capitalize(),"googlengine_states_ut_master.csv"))

path = Path(indiastautfile)




if path.is_file():
    pi="\'India States and UTs data : \' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    
else:
    pi="\'Data of States and UTs is missing!\' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    pi="\'Execute myindiagenStatesandUTdata.py First !\' :"
    statesutpy = "Get from Git Hub"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Download :' :"
    statesutpy = "https://github.com/NATURE-LABS/India/blob/main/myindiagenStatesandUTdata.py"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Save myindiagenStatesandUTdata.py \' :"
    statesutpy = "in c:\python\indias"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Document :\' :"
    statesutpy = "https://github.com/NATURE-LABS/India/blob/main/Python%20Lab%20India_states_UT.docx"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    exit(1)


titlehead = ("{} {}".format('List of States and Union Territories of', namefile.capitalize()))
indiafiletxt = ("{}{}".format(namefile,".txt"))

inputfile = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,"data",N,indiafiletxt))

inputfile_google_json = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,"data",N,google_json))

def statesutfile(templeget, sut):
    titlehead = ("{} {}".format(templeget, sut.capitalize()))
    patternspace = re.compile(r'\s+')
    sut = re.sub(patternspace, '-', sut)
    indiafilepushtxt = ''
    indiafilepushtxt = ("{}_{}_{}".format(namefile.capitalize(),sut,"googlenginetemple.txt"))
    indiafilegiventxt = ''
    indiafilegiventxt = ("{}{}{}".format(cre_directory,N,indiafilepushtxt))
    return indiafilegiventxt

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}


def bs4_get_text_googlesearch(search):
  #countries = ['in', 'us', 'uk', 'nz', 'vg', 'tg']
  countries = ['in']

  default_language = "en"

  cgl = []

  getmano = ''
  templemano = []

  with open(inputfile_google_json) as jsonFile:
      data = json.load(jsonFile)

      for d in data:
          gcc=(d['country_code'])
          gcn=(d['country_name']) 
          glc=(d['language_code'])
          gd=(d['domain'])
          gts = []
          gts = [gcn,glc,gcc,gd]
    
          if gts not in (cgl):
            cgl.append(gts)    
       
  cgs = sorted(cgl)
  la = []
  for g in (cgs):
    n = g[0]
    l = g[1]
    c = g[2]
    d = g[3]
    if l not in la:

      la.append(l)

    if (c == 'in'):
      language = default_language
    else:
        language = l


    for i in (countries):
    
      if (i == c):
        
          params = {
            'q': search,  # query 
            'gl': c,    # country to search from
            'hl': language,    # language
            "google_domain": d, #Domain
            'safe' : 'active',
            'num' : max_gs
          }
         
          
          try:
            
            response = requests.get(searchengine)
            response.raise_for_status()
            
          except URLError as ue:
            pi="\'The Search Engine is not reachable \' :"
            p = ("{} {}".format(pi,searchengine))
            prt(p)
            
            exit(1)
          else:
            html = requests.get('https://www.google.com/search', headers=headers, params=params).text
            soup = BeautifulSoup(html, 'lxml')
            getmano = (soup.get_text())

          return getmano
          

  lam = sorted(la)

#தமிழ்



#creating directory --- start -- 
datadirgoo = ("{}_{}".format(namefile.capitalize(),"googlengine_temple_States_and_UTs"))

googledatadir = ("{}{}{}".format(indiatempledatadir,N,datadirgoo))


cre_directory = Path(googledatadir)
cre_directory.mkdir(parents=True, exist_ok=True)
#creating directory --- sucessful ----- -- 


df = pd.read_csv(indiastautfile, delimiter=',',
on_bad_lines='skip', 
engine="python"
)


templesget = sorted([list(row) for row in df.values])

sul =  []

for t in templesget:

  #t = [("{}{}{}".format(t[0], " , ", t[1]))]
  
  m = [ x.strip() for x in ''.join(t).strip('[]').split(',') ]
  
  if m not in sul:
      sul.append(m[0])

  else:
        print("Duplicate is removed", t)

#print(sul)

def addinggooglesearchdata():
  getmano = bs4_get_text_googlesearch(search)
  if (getmano):
      #print(getmano)
      
      colheader = [search]
      dfdin = []
          
      dfdin.append(getmano)
      gencsv = pd.DataFrame(dfdin,  columns= colheader )
      gencsv.to_csv(indiafilegiventxt, index=False, na_rep='Unknown')

      
for statename in (sul):

  #statename = "Tamil nadu"
  
  templeget = mim
  search = ("{} {}".format(templeget,statename))

  indiafilegiventxt = statesutfile(templeget, statename)
  
  

  sf = Path(indiafilegiventxt)

  if sf.is_file():
      pi= ("{}{}".format("State or UT name : ", statename))
      p = ("{}".format(pi))
      prt(p)
       
       

      pi="\'Google data of temples in state or UT is already exists for :\' :"
      p = ("{} {}".format(pi,statename))
      prt(p)
      p = ("{}".format(indiafilegiventxt))
      prt(p)
  else:
      pi="\'Google data of temples in state or UT is Googling.. :\' :"
      p = ("{} {}".format(pi,statename))
      prt(p)
      p = ("{}".format(indiafilegiventxt))
      prt(p)
      print("File :",indiafilegiventxt)
      addinggooglesearchdata()  
        
        #getmano = bs4_get_text_googlesearch(search,cose = c,langu = 'en',domn = d,numbe = 10)
       