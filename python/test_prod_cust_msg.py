import random
import logging
import threading
import concurrent.futures
import queue
import time

def producer(pipeline, event):
    while not event.is_set():
        msg = random.randint(1, 101)
        logging.info(f"producer got {msg}")
        pipeline.put(msg)
    logging.info(f"producer received Event set")

def consumer(pipeline, event):
    while not event.is_set() or not pipeline.empty():
        msg = pipeline.get()
        logging.info(f"consumer got {msg}, queue size {pipeline.qsize()}")
    logging.info("Consumer received Event set or pipeline empty")


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = queue.Queue()
    event = threading.Event()
    #with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #    executor.submit(producer, pipeline)
    #    executor.submit(consumer, pipeline)

    prd = threading.Thread(target=producer, args=(pipeline, event))
    cns = threading.Thread(target=consumer, args=(pipeline, event))

    prd.start()
    cns.start()

    time.sleep(0.002)
    logging.info('about to set Event')
    event.set()


    prd.join()
    cns.join()
