from flask import Flask

app = Flask(__name__)

import clr, sys, os
import config

dlllib_path=os.path.join(config.BASE_DIR,"dlllib")
sys.path.insert(0, dlllib_path)

clr.FindAssembly('BSMAnalytics')
clr.AddReference('BSMAnalytics')
from System import Convert
from System import *
from BSMAnalytics import ExcelFuncs

from src import routs
