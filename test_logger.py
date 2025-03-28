from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger = get_logger(__name__)  # Only one logger instance

def divide_num(a, b):
    try:
        result = a / b 
        logger.info("Dividing two numbers")
        return result
    except Exception as E:
        logger.error(f"Error occurred: {str(E)}")  # Log the actual error message
        raise CustomException(str(E), sys)  # Pass the required arguments

if __name__ == "__main__":
    try:
        logger.info("Starting main program")
        divide_num(10, 10)# This will raise an error
    except CustomException as ce:
        logger.error(str(ce))  # Logs the detailed custom exception
