from exception import CustomException
from logger import logging
import os,sys
a = 10
b = 0
def divide(a, b):
    try:
        result = a / b
        logging.info("in app file")
        return result
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    except Exception as e:
        logging.info("in app file")
        raise CustomException(e,sys)
    
