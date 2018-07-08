import requests
from bs4 import BeautifulSoup as bs
from io import BytesIO
from PIL import Image

def crawlImages(keyword, verbose=False):
    google_search = "https://www.google.com/search?q=" + keyword + "&source=lnms&tbm=isch&sa=X&ved=0ahUKEwilqcTb4Y7cAhUPHzQIHSTiCc8Q_AUICigB&biw=1440&bih=742"
    bing_search = "https://www4.bing.com/images/search?q=" + keyword + "&FORM=HDRSC2"
    images = []

    if (verbose):
        print "Crawling Google"
    response = requests.get(google_search, timeout=2)
    soup = bs(response.content, "html.parser")
    soup = soup.find("table", attrs={"class":"images_table"})

    processed = 1

    # google search
    for row in soup.findAll("tr"):
        for item in row.findAll("td"):
            resp = requests.get(item.img.get("src"))
            images.append(BytesIO(resp.content))

            if (verbose):
                processed += 1
                if (processed % 5 == 0):
                    print "Downloading images"


    if (verbose):
        print "Crawling Bing"
    response = requests.get(bing_search, timeout=2)
    soup = bs(response.content, "html.parser")

    # bing search
    for image in soup.findAll("div", attrs={"class":"cico"}):
        resp = requests.get(image.img.get("src"))
        images.append(BytesIO(resp.content))

        if (verbose):
            processed += 1
            if (processed % 5 == 0):
                print "Downloading images"

    return images

# for testing purposes
# im = crawlImages("waterloo university")
# Image.open(im[0]).show()
