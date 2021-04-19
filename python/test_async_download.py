import sys
import requests
import time
import threading
import concurrent.futures
import multiprocessing
import random
import asyncio
import aiohttp


def get_sites(n):
    return [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice"
    ] * n


class Timer:
    def __init__(self, nr_urls, func_name):
        self.nr_urls = nr_urls
        self.func_name = func_name
        self.start = 0
        self.end = 0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = time.time()
        self.duration = self.end - self.start
        print(f"{self.func_name}: Downloaded {self.nr_urls} in {self.duration} seconds")
        return False

############################################################
# no multi task
def request_site(url, session):
    with session.get(url) as response:
        #print(f"Read {len(response.content)} from {url}")
        pass


def request_download(sites):
    with Timer(len(sites), 'request'):
        with requests.Session() as session:
            for url in sites:
                request_site(url, session)


############################################################
# multi threading

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def threading_download_site(url):
    session = get_session()
    with session.get(url) as response:
        #print(f"Read {len(response.content)} from {url}")
        pass


def threading_download_all_sites(sites):
    with Timer(len(sites), 'threading'):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(threading_download_site, sites)


############################################################
# multi processing

mp_session = None

def set_global_session():
    global mp_session
    if not mp_session:
        mp_session = requests.Session()


def mp_download_site(url):
    with mp_session.get(url) as response:
        #name = multiprocessing.current_process().name
        #print(f"{name}:Read {len(response.content)} from {url}")
        pass


def mp_download(sites):
    with Timer(len(sites), 'multi-pro'):
        with multiprocessing.Pool(initializer=set_global_session) as pool:
            pool.map(mp_download_site, sites)


############################################################
# asyncio
async def async_download_url(session, url):
    async with session.get(url) as response:
        text = await response.text()
        #print("Read {0} from {1}".format(len(text), url))


async def async_download_urls(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(async_download_url(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


def async_download(sites):
    with Timer(len(sites), 'async'):
        asyncio.get_event_loop().run_until_complete(async_download_urls(sites))


if __name__ == '__main__':
    n = sys.argv[1]

    sites = get_sites(int(n))
    request_download(sites)
    threading_download_all_sites(sites)
    async_download(sites)
    mp_download(sites)
