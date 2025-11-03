import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m-%d_%Y_%H-%M-%S')}.log"

# Full path for log file
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Basic logging config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Example usage:
# logging.info("Logging has started")
