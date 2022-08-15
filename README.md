# Daraz-Clone
_DARAZ clone is an online web application for new sellers at DARAZ. Where they can reach to any specific product according to its brand, seller or category etc. 
It provides extra feature as well where sellers can get prediction-based result weather their product can be in a Top Reviewed products or not_

## Optical Character Recognition
OCR is implemented in this project, in order to read text from product images. Text can be important announcements or offers 
 ### How to run OCR

1) To run Python file in a OCR folder, firstly you have to download tesseract file (tesseract.exe) from https://tesseract-ocr.github.io/tessdoc/Downloads.html
2) Add the file path where you download it
3) Now you are up to run OCR to detect/read text from images 

## YOLO Object Detection Model
Few images have "TOP Reviewed" tag that is blur enough to give below average performance of OCR. So to tackle this problem, we are using YOLO to detect tag at a fixed. This model returns two states either True (Top reviewed tag exist) or False

### How to run YOLO
In a yolo_custom_detection.txt file you will find a link of drive, from where you can download a model that is already trained to detect TOP REVIEWED on images 
You just need to pass URLS of images in a array to model in a yolo_custom_detection.py. It will return you Array of 1 and 0s. 1 means found 0 means Not found



## Scraping 
In a scraping folder you will find a python file (test.py) along with the data.txt file. Data.txt file contains <script> tags of window.pageview. Pass script tags of products (you  want to scrap) in data.txt. Then execute a python file. Products, Brands and Sellers will be scraped in csv files of Dataset folder. In case of error or no products added in file, do check your path in python file 
  
 
  
## Web App
I have shared the published folder of my web app, to run it you can deploy it to any server using filezilla. For code base, you can check Models folder in App folder App>>Model

