from time import time
from secrets import CLIENT_ID
from utils import setup_download_dir, get_links, download_link
import logging
import Queue
import threading
from functools import partial
from multiprocessing.pool import Pool

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

'''
Benchmarking Single threaded vs Multithreaded vs Multiprocess download of images
Since this is a network IO heavy task with CPU usage to a minimum, good gains are observed in 
using multithreading.
'''


def single_threaded_execution():
    start_ts = time()
    download_directory = setup_download_dir()
    links = get_links(CLIENT_ID)
    count = len(links)
    for link in links:
        download_link(download_directory, link)
    logging.info('Time Taken to Sequentially download %s images took %s Seconds', count, time() - start_ts)


def multi_threaded_execution(num_of_threads=8):

    class WorkerThread(threading.Thread):
        def run(self):
            while True:
                dir, link = queue.get()
                download_link(dir, link)
                queue.task_done()

    start_ts = time()
    download_dir = setup_download_dir()
    links = get_links(CLIENT_ID)
    count = len(links)
    queue = Queue.Queue()

    for i in range(num_of_threads):
        t = WorkerThread()
        t.daemon = True
        t.start()

    for link in links:
        queue.put((download_dir, link))

    queue.join()
    logging.info('Time Taken to Parallely download %s images took %s Seconds', count, time() - start_ts)


def multi_process_execution(pool_size=8):
    start_time = time()
    download_dir = setup_download_dir()
    links = get_links(CLIENT_ID)
    count = len(links)
    download = partial(download_link, download_dir)
    p = Pool(pool_size)
    p.map(download, links)
    logging.info('Time Taken to Multiprocess download %s images took %s Seconds', count, time() - start_time)


if __name__ == '__main__':
    single_threaded_execution()
    multi_threaded_execution()
    multi_process_execution()

