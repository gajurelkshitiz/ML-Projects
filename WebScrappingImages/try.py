from bs4 import BeautifulSoup as bs
import os
import json
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# url = "https://www.google.com/search?q=dogs&sca_esv=588712944&tbm=isch&sxsrf=AM9HkKntTjFxEtYsIYk4ryq8vMfecLRosA:1701948636287&source=lnms&sa=X&ved=2ahUKEwjX4JDfnP2CAxUjTGwGHeFxB5UQ_AUoAXoECAIQAw&biw=638&bih=549&dpr=1.5"


def createImageUrl(searchterm):
        searchterm=searchterm.split()
        searchterm="+".join(searchterm)
        web_url = "https://www.google.com/search?q="+ searchterm +"&sca_esv=588269219&tbm=isch&sxsrf=AM9HkKlCm6JsRjli4a-D38o92tXLhm1wiw:1701839515263&source=lnms&sa=X&ved=2ahUKEwiQkJaehvqCAxXpT2wGHY__CJIQ_AUoAXoECAEQAw&biw=1280&bih=551&dpr=1.5"
        return web_url
    
# get raw HTML
def scrap_html_data(url, header):
    request = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    html = bs(response_data, 'html.parser')
    return html

# Contains the link of original images, and image type
def getimageUrlList(rawHtml):
    imageUrlList = []
    
    for div in rawHtml.find_all("div", {"class": "fR600b islir"}):
        # Find the img tag within the div
        img_tag = div.find('img')

        if img_tag:
            image_url = img_tag.get('src') or img_tag.get('data-src')
            imageUrlList.append(image_url)
        
    print("there are total", len(imageUrlList), "images")
    return imageUrlList



get_url = createImageUrl("cat")
raw_html = scrap_html_data(get_url, header)
print(raw_html)
# myurllist = getimageUrlList(raw_html)
# print(myurllist)