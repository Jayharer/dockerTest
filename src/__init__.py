from flask import Flask
import clr, sys, os
import config


sys.path.insert(0, config.DLL_PATH)

clr.FindAssembly('BSMAnalytics')
clr.AddReference('BSMAnalytics')
from System import Convert
from System import *
from BSMAnalytics import ExcelFuncs

app = Flask(__name__)

from src import routs
