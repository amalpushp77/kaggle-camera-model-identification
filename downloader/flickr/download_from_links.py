import numpy as np
import pandas as pd
import httplib2
from bs4 import BeautifulSoup
import urllib.request
from tqdm import tqdm
import os


folders = os.listdir('links/')
for i in folders:
    cnt = 0
    df = pd.read_csv('links/'+i)
    
    i = i.replace('.csv','')
    for index, row in df.iterrows():
        
        try:
            img = urllib.request.urlopen(row['link']).read()
        except urllib.error.HTTPError as e:
            if e.getcode() == 404:
                continue
        except ConnectionResetError:
            continue
            
    out = open("files/{0}/{1}.jpg".format(i,cnt), "wb")
    out.write(img)
    out.close
    cnt += 1
