from bs4 import BeautifulSoup as bs
import os
import json
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve


class ScrapperImage:

    # Create Image Url
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



    def downloadImagesFromURL(imageUrlList,image_name, header):
        masterListOfImages = []
        count=0
        ### print images
        imageFiles = []
        # imageTypes = []
        image_counter=0
        for img in imageUrlList:
            try:
                if (count > 5):
                    break
                else:
                    count = count + 1
                req = urllib.request.Request(img, headers=header)

                try:
                    urllib.request.urlretrieve(img,"./static/"+image_name+str(image_counter)+".jpg")
                    image_counter=image_counter+1
                except Exception as e:
                    print("Image write failed:  ",e)
                    image_counter = image_counter + 1
                respData = urllib.request.urlopen(req)
                raw_img = respData.read()
                # soup = bs(respData, 'html.parser')

                imageFiles.append(raw_img)
                # imageTypes.append(Type)

            except Exception as e:
                print("could not load : " + img)
                print(e)
                count = count + 1
        masterListOfImages.append(imageFiles)
        # masterListOfImages.append(imageTypes)

        return masterListOfImages


    def delete_downloaded_images(self,list_of_images):
        for self.image in list_of_images:
            try:
                os.remove("./static/"+self.image)
            except Exception as e:
                print('error in deleting:  ',e)
        return 0