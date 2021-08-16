import os
import logging

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig(filename='api.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')