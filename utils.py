import logging
import json
import os
from pathlib import Path
from config import DOWNLOAD_URL, IMG_TYPES
from time import time
try:
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import Request, urlopen

logger = logging.getLogger(__name__)


def get_links(client_id):
    req = Request(DOWNLOAD_URL)
    req.add_header("Authorization", "Client-ID {}".format(client_id))
    data = urlopen(req).read()
    data = json.loads(data.decode('utf-8'))
    return map(lambda item: item['link'],
               filter(lambda item: 'type' in item and item['type'] in IMG_TYPES, data['data']))


def download_link(directory, link):
    download_path = directory / os.path.basename(link)
    img = urlopen(link)
    file = download_path.open('wb')
    file.write(img.read())
    logger.info('Downloaded %s', link)


def setup_download_dir():
    download_dir = Path('images_{0}'.format(str(time())))
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir

