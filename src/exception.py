import sys
from src.logger import logging

def error_message_detail(error , error_detail:sys):
    _,_,exc_traceback = error_detail.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name , exc_traceback.tb_lineno , str(error))  
    
    return error_message
    
    
class CustomException(Exception):
    def __init__(self , error_message , error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message , error_detail = error_detail)
    
    def __str__(self):
        return self.error_message    
 
if __name__ == '__main__':
    
    try:
        a = 1/0
    except Exception as e:
        logging.info('Divide by Zero') 
        raise CustomException(e , sys)   


'''
import sys
sys gives access to Python runtime information

    error type

    error traceback

    line number where error occurred

from src.logger import logging 

    This imports your custom logger

    Instead of print(), you use logging.info()

    This writes errors to log files
    
Function: error_message_detail
def error_message_detail(error , error_detail:sys):

    This function formats an error message in a readable way
    
    error → the exception message (ZeroDivisionError)

    error_detail → sys module (used to extract traceback) 
    
    _,_,exc_tb = error_detail.exc_info()
    
    exc_info() returns 3 things:

    exception type

    exception object

    traceback object
    
    _ ignores first two values

    exc_traceback stores traceback
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    This extracts which Python file caused the error
    
    Example : src/components/data_ingestion.py

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name , exc_traceback.tb_lineno , str(error))
    
    This builds a custom error message:

    {0} → file name

    {1} → line number where error occurred

    {2} → actual error message
    
    Example : Error occurred in python script name [data_ingestion.py] 
              line number [23] 
              error message [division by zero]

    return error_message
    
    This returns the error_message


class CustomException(Exception):

We are creating our own error type
Instead of : ZeroDivisionError 
We now raise : CustomException

def __init__(self , error_message , error_detail:sys):

This runs when the exception is raised.

    super().__init__(error_message)
    
    Calls Python’s base Exception class
    
    self.error_message = error_message_detail(error_message , error_detail = error_detail)
    
    Calls your formatting function

    Stores the clean error message
    
    def __str__(self):
    return self.error_message
    
    When Python prints the error , we see : 
    Error occurred in python script name [...] line number [...] error message [...]
    
if __name__ == '__main__':

Run this code only if this file is executed directly

    try:
    a = 1/0 
    
    This intentionally causes an error : 
    ZeroDivisionError 
    
    except Exception as e:
    
    Catches any type of error
    Stores it in variable "e" 
    
    logging.info('Divide by Zero')
    
    Writes to log file:
    
    INFO - Divide by Zero 
    
    raise CustomException(e , sys)
    
    This:
    Wraps original error(e)
    Adds file name + line number
    Throws a clean , readable error    
    
'''     



'''
                         CONTROL FLOW


'''           