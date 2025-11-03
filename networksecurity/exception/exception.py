import sys
from networksecurity.logging.logger import logging

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = str(error_message)
        
        # Extracting traceback details
        _, _, exc_tb = error_detail.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script [{self.file_name}] at line number [{self.lineno}]: {self.error_message}"

if __name__ == "__main__":
    try:
        logging.info("Starting the application")
        a = 1 / 0
        print("This will not be printed")
    except Exception as e:
        raise NetworkSecurityException(e, sys)
