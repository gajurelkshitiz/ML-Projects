from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import os
import time
from urllib.parse import urlparse, parse_qs

def get_image_urls(search_query, num_images=10):
    # Set up the Selenium driver
    driver = webdriver.Chrome()  # Use the path to your chromedriver executable
    driver.get("https://www.google.com/imghp")

    # Find the search box element and input the search query
    search_box = driver.find_element("name", "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Scroll down to load more images
    for _ in range(3):  # Adjust the number of scrolls as needed
        driver.find_element_by_tag_name("body").send_keys(Keys.END)
        time.sleep(2)  # Allow time for images to load

    # Get the page source and parse it with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    # Find image URLs in the parsed HTML
    img_urls = []
    for img_tag in soup.find_all("img"):
        img_url = img_tag.get("src")
        if img_url:
            img_urls.append(img_url)

    # Close the browser
    driver.quit()

    return img_urls[:num_images]

def download_images(img_urls, save_folder="cat_images"):
    # Create a folder to save the images
    os.makedirs(save_folder, exist_ok=True)

    # Download and save each image
    for i, img_url in enumerate(img_urls):
        response = requests.get(img_url)
        if response.status_code == 200:
            # Extract the image file name from the URL
            img_name = f"cat_image_{i+1}.jpg"
            img_path = os.path.join(save_folder, img_name)

            # Save the image
            with open(img_path, "wb") as img_file:
                img_file.write(response.content)

            print(f"Image {i+1} saved: {img_path}")

def main():
    search_query = "cat"
    num_images = 10
    img_urls = get_image_urls(search_query, num_images)
    download_images(img_urls)

if __name__ == "__main__":
    main()
