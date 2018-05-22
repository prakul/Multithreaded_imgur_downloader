from time import time
from secrets import CLIENT_ID
from utils import setup_download_dir, get_links, download_link
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    ts = time()
    client_id = CLIENT_ID
    download_directory = setup_download_dir()
    links = get_links(client_id)
    for link in links:
        download_link(download_directory, link)
    logging.info('Time Taken %s', time()-ts)


if __name__ == '__main__':
    main()