import requests
from bs4 import BeautifulSoup as bs
from io import BytesIO
from PIL import Image
from multiprocessing.dummy import Pool

def googleSearch(args):
    [keyword, startFrom, verbose] = args

    if verbose:
        print "Crawling Google"

    image_urls = []

    google_search = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=0ahUKEwilqcTb4Y7cAhUPHzQIHSTiCc8Q_AUICigB&biw=1440&bih=742&start={}".format(keyword, startFrom)
    response = requests.get(google_search, timeout=2)
    soup = bs(response.content, "html.parser")
    images = soup.find_all('img')
    image_urls += images

    return image_urls


def crawlImages(keyword, verbose=False):
    images = []
    if (verbose):
        processed = 1

    pool = Pool(3)
    imagesFetched = pool.map(googleSearch, [[keyword, x*20, verbose] for x in range(3)]) # this will search 3 google pages
    pool.close()
    pool.join()

    normalizedImagesFetched = []
    for i in imagesFetched:
        normalizedImagesFetched += i

    for image in normalizedImagesFetched:
        resp = requests.get(image.get('src'))

        images.append(BytesIO(resp.content))

        if (verbose):
            processed += 1
            if (processed % 5 == 0):
                print "Downloading images"

    return images

# for testing purposes
# im = crawlImages("waterloo university")
# Image.open(im[0]).show()
