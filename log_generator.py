import time
import random
import logging

logging.basicConfig(filename='/var/log/app-error.log', level=logging.INFO, format='%(asctime)s %(message)s')

while True:
    logging.error("Database Connection Failed - Critical Error")
    logging.info("User login successful")
    time.sleep(5)