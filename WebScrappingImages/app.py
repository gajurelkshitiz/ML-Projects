from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import os
from ScrapperImage.ScrapperImage import ScrapperImage
from businesslayer.BusinessLayerUtil import BusinessLayer

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/showimages')
@cross_origin()
def displayimages():
    list_images = os.listdir('static')
    print(list_images)

    try:
        if(len(list_images) > 0):
            return render_template('showimages.html', user_images = list_images)
        else:
            return "Images doesn't exists."
    
    except Exception as e:
        print("No images found. ", e)
        return "Please try with different keyword."



@app.route('/searchimages',methods=['GET','POST'])
def searchimages():
    if request.method=='POST':
        search_term = request.form['keyword']
    else:
        print("Please enter something")
    
    imagescrapperutil=BusinessLayer ## Instantiate a object for ScrapperImage Class
    imagescrapper=ScrapperImage()
    list_images=os.listdir('static')
    imagescrapper.delete_downloaded_images(list_images)## Delete the old images before search
    
    # Processing the search term:
    image_name=search_term.split()
    image_name="+".join(image_name)
    
    ## We need to add the header metadata
    
    header={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
            
            }
    lst_images=imagescrapperutil.downloadImages(image_name,header)
    
    return displayimages() # redirect the control to the show images method
    


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)

