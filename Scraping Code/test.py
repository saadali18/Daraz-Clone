from sys import implementation
from bs4 import BeautifulSoup
import csv
import json
from pathlib import Path
import cv2 
import urllib.request
import numpy as np

def ScrapBrands(script):
    csvfile=open('Brands.csv','a', newline='')
    obj=csv.writer(csvfile)
    header = ("Brand_ID","Brand_Name")
    #obj.writerow(header) 
    data=script
    data=data[16:]
    res = json.loads(data)
    no_of_products=len(res["mods"]["listItems"])
    for i in range(no_of_products):
            try:
                
                Brand_Id=res["mods"]["listItems"][i]["brandId"]
                Brand_Name=res["mods"]["listItems"][i]["brandName"]
                row_csv = [Brand_Id,Brand_Name]
                obj.writerow(row_csv)
            except:
            
                continue
    csvfile.close()

def ScrapSellers(script):
    csvfile=open('Sellers.csv','a', newline='')
    obj=csv.writer(csvfile)
    header = ("Seller_ID","Seller_Name")
    #obj.writerow(header) 
    data=script
    data=data[16:]
    res = json.loads(data)
    no_of_products=len(res["mods"]["listItems"])
    for i in range(no_of_products):
            try:
                Seller_Id=res["mods"]["listItems"][i]["sellerId"]
                Seller_Name=res["mods"]["listItems"][i]["sellerName"]
                row_csv = [Seller_Id,Seller_Name]
                obj.writerow(row_csv)
            except:
            
                continue
    csvfile.close()
# get all tenders by looping their page no
def ScrapProducts(script):
    csvfile=open('Products.csv','a', newline='')
    obj=csv.writer(csvfile)
    header = ("Category","Sub_Category_1","Sub_Category_2", "Product_Name","Product_ID", "Brand_ID", "Seller_ID", "Prize", "Rating_Score", "Review", "Installment", "Description", "In_Stock","Top_Reviewed","Special_Offer_Detail","Special_Offer_Prize","Special_Offer_Till", "Country","Product_URL","Image_Url")
    #obj.writerow(header) 
    data=script
    data=data[16:]
    res = json.loads(data)
    no_of_products=len(res["mods"]["listItems"])
    print(res["mods"]["listItems"])
    for i in range(no_of_products):
            try:
                Id=res["mods"]["listItems"][i]["itemId"]
                Name=res["mods"]["listItems"][i]["name"]
                inStock=res["mods"]["listItems"][i]["inStock"]
                Category="Home and Lifestyle"
                Sub_Category_1="Kitchen and Dining"
                Sub_Category_2="kAD"
                Brand_Id=res["mods"]["listItems"][i]["brandId"]
                Prize=res["mods"]["listItems"][i]["priceShow"]
                ratingScore=res["mods"]["listItems"][i]["ratingScore"]
                Seller_Id=res["mods"]["listItems"][i]["sellerId"]
                Installment=res["mods"]["listItems"][i]["installment"]
                description=res["mods"]["listItems"][i]["description"]
                country=res["mods"]["listItems"][i]["location"]
                review=res["mods"]["listItems"][i]["review"]
                Product_Url=res["mods"]["listItems"][i]["productUrl"]
                Top_Reviewed="1"
                Special_Offer_Detail="Special_Offer_Detail"
                Special_Offer_Prize="Special_Offer_Prize"
                Special_Offer_Till="24=jun-21"
                ImageUrl=res["mods"]["listItems"][i]["image"]
                row_csv = [Category,Sub_Category_1,Sub_Category_2,Id,Name,Brand_Id,Seller_Id,Prize,ratingScore,review,Installment,description,inStock,Top_Reviewed,Special_Offer_Detail,Special_Offer_Prize,Special_Offer_Till,country,Product_Url,ImageUrl]
                obj.writerow(row_csv)
            except:
                continue
    csvfile.close()
if __name__=='__main__':
    txt = open('data.txt', 'r').read()
    
    ScrapProducts(txt)
    ScrapBrands(txt)
    ScrapSellers(txt)
    # req = urllib.request.urlopen('https://static-01.daraz.pk/p/5c87dc64b84702c5ced40bbac2adbb16.jpg')
    # arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    # img1 = cv2.imdecode(arr, -1) # 'Load it as it is'
    
    # print(img1)
    # img = cv2.imread("C:\\Users\\Lenovo\\Desktop\\Scraping\\Testing\\1.jpg")
    # print(img)

   
        
        

  
