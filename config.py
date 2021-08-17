import os, sys
import logging

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig(filename='api.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

if sys.platform == 'win32':
    DLL_PATH = BASE_DIR + '\dllLib\win32'
else:
    DLL_PATH = BASE_DIR + '/dllLib/linux'
