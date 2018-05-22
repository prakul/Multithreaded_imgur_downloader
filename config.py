import random

IMG_TYPES = {'image/jpeg', 'image/png', 'image/gif'}
GALLERY_TERMS = ['cats', 'dogs', 'humor', 'flowers']
DOWNLOAD_URL_1 = 'https://api.imgur.com/3/gallery/search/{0}?q={1}'.format(random.randint(1,10), random.choice(GALLERY_TERMS))
DOWNLOAD_URL = 'https://api.imgur.com/3/gallery/random/random/'
