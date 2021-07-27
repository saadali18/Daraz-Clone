import json
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\\Users\\Lenovo\\Desktop\\Tesseract\\tesseract.exe'
import cv2
import requests
from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO
from urllib.request import urlopen
import numpy as np
import urllib.request 
import json
import pandas
def get_ProductsURL(page_url):
    Urls=[]
    #https://www.daraz.pk/smart-watches/?spm=a2a0e.searchlistcategory.cate_1.7.384438ddHqiCy5
    #page_url = "https://www.daraz.pk/smartphones/apple/?page="+str(i)+"&spm=a2a0e.home.cate_1_1.2.57e17d68JzDrDi" # url of table pages
    response = requests.get(page_url)    # get HTML
    if response.status_code == 200: # check the request is successfully get response with content
        soup = BeautifulSoup(response.text, 'html.parser')   # get all tags of html as objects
        all_scripts = soup.find_all('script')
        my_script=all_scripts[3]
        data=my_script.string
        data=data[16:]
        res = json.loads(data)
        no_of_products=len(res["mods"]["listItems"])
        print(no_of_products)
        for i in range(no_of_products):
            try:       
                Product_Url=res["mods"]["listItems"][i]["image"]
                Urls.append(Product_Url)
            except:
                print(i)
                continue
        return Urls

def Special_Offer_dec(url):
    url_response = urllib.request.urlopen(url)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)
    text=pytesseract.image_to_string(img)
    if "Mega Deals" in text:
        
        return True
    else:
    
        return False
