import pandas as pd
from pathlib import Path
import sys, re

basepath = "C:"
codepath="python"
function = "indias"
N="\\"
namefile = "india"

titlehead = ("{} {}".format('List of States and Union Territories of', namefile.capitalize()))
indiafiletxt = ("{}{}".format(namefile,".txt"))

inputfile = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,"data",N,indiafiletxt))

indiafilepushtxt = ("{}{}".format(namefile,"googlenginefile.txt"))

indiafilegiventxt = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,"data",N,indiafilepushtxt))

def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")

path = Path(inputfile)

if path.is_file():
    pi="\'India file is available \' :"
    p = ("{} {}".format(pi,inputfile))
    prt(p)
    
else:
    pi="\'India file is missing !\' :"
    p = ("{} {}".format(pi,inputfile))
    prt(p)
    
    exit(1)

df = pd.read_csv(inputfile, sep=r'[,|;\n"]+(?=\S)', header=None, 
on_bad_lines='skip', 
engine="python")

indiaslist = ([list(row) for row in df.values])

def removen(string):

    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,' ', clean_string)
        clean_string = [re.sub(r"[^a-zA-Z<>:';2315{}/\-1]+", ' ', k) for k in clean_string.split("\n")]
        
        return clean_string
      

tml = []

def addheadings():

    title = ("{}{}{}".format("<html><head><title>", titlehead, '</title>'))
    clean_string = removen(title)
    a = ''.join(clean_string) 
    tml.append(a)
   
    hh = """
    <style>
    h3 { 
    color: blue; 
    font-family: 'Helvetica Neue', sans-serif; 
    font-size: 15px; font-weight: bold; 
    letter-spacing: -1px; 
    line-height: 2; 
    text-align: left; 
    }

    </style>

    </head>
    <body>
    """
    clean_string = removen(hh)
    b = ''.join(clean_string) 
    tml.append(b)


indias  =  []

ss = '\('
se = '\)'
patten = ("{}{}{}{}{}".format('(',ss, "[^$]*",se,')'))
pats = re.compile("^\s+|\s*,\s*|\s+$")

for i in (indiaslist):
    
    b = re.findall(patten, str(i))
    if (b):

        ic = " ".join(str(elem) for elem in i).strip()
        
        ic = re.sub('\(', ',', str(ic))
        ic = re.sub('\)', '', str(ic))
        icl = [x for x in pats.split(ic) if x]
        indias.append(icl)
    

for i in range(0,len(indias)):
    if(i ==0):
   
       
        th = addheadings()
        bh = ("{}{}{}".format("<h3>",titlehead,"</h3>"))
        tml.append(bh)
        
    else:
        h = ("{}{}{}{}{}".format("<h3>",indias[i][0],",",indias[i][1],"</h3>"))
        tml.append(h)

c = ''.join(tml) 



with open(indiafilegiventxt, 'w') as tfile:
   
    tfile.write(c)

pi="\'The html syntax file is generated  \' :"
p = ("{} {} {}".format(namefile.capitalize(), pi,indiafilegiventxt))
prt(p)

pi="\'Use the html file to create web page  \' :"
p = ("{} {} {}".format(namefile.capitalize(), pi,indiafilegiventxt))
prt(p)
