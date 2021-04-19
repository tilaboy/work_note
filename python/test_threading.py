import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    thread_name = threading.get_ident()
    logging.info(f"{thread_name} felt into sleep")
    time.sleep(4)
    logging.info("Thread %s: finishing", name)


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before running thread")
    threads = list()
    for i in range(3):
        x = threading.Thread(target=thread_function, args=(i,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        logging.info(f"Main    : before join {index} thread")
        thread.join()
        logging.info(f"Main    : thread {index} done")
