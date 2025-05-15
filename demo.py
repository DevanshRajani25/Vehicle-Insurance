# This both execution will give logs in log folder

## For checking Logging file
# from src.logger import logging

# logging.debug("This is a debug message!")
# logging.info("This is a info message!")
# logging.warning("This is a warning message!")
# logging.error("This is a error message!")
# logging.critical("This is a critical message!")


## For checking exception file
from src.logger import logging
from src.exception import MyException
import sys 

try:
    a = 1+'z'
except Exception as e:
    logging.info(e)
    raise MyException(e,sys) from e 