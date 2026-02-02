import logging 
import os 
from datetime import datetime 

#Absolute path of this file (logger.py)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ↑ goes from src/logger.py → src/ → project root

#Log file name 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#Logs directory (always at project root)
LOGS_DIR = os.path.join(BASE_DIR , "logs") 
os.makedirs(LOGS_DIR , exist_ok=True) 

#Full log file path 
LOG_FILE_PATH = os.path.join(LOGS_DIR , LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH , 
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s" , 
    level = logging.INFO
) 





'''
import logging
import os
from datetime import datetime

logging → Python’s built-in logging system

os → file & directory handling

datetime → timestamps for log file names

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    __file__

    ➡️ Path of the current file (logger.py)
    
    Example : C:\CODE\40-MLProject\src\logger.py

    os.path.abspath(__file__)

    ➡️ Converts it into a full absolute path
    
    Example : C:\CODE\40-MLProject\src\logger.py
    
    First os.path.dirname(...)

    ➡️ Moves one level up

    C:\CODE\40-MLProject\src
    
    Second os.path.dirname(...)

    ➡️ Moves one more level up

    C:\CODE\40-MLProject  #This is the project root

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

datetime.now()

→ gets current date & time

.strftime('%m_%d_%Y_%H_%M_%S' formats time as : 

09_25_2024_14_37_10

LOGS_DIR = os.path.join(BASE_DIR , "logs") 

    This builds : C:\CODE\40-MLProject\logs
    
    os.makedirs(LOGS_DIR , exist_ok=True) #Create the logs/ folder 


LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE) which results in : 

C:\CODE\40-MLProject\logs\01_30_2026_13_42_10.log

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

This line configures Python’s global logging engine.
 
    filename=LOG_FILE_PATH
    “Send ALL logs to this file”
    
     format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s" 
     Defines how each log line looks 
     
     Example : 
     [2024-09-25 14:37:10] 42 data_ingestion - INFO - Data ingestion started
     
     level=logging.INFO
     INFO and above are recorded

     DEBUG is ignored

     ERROR, WARNING, CRITICAL are included
    
'''
