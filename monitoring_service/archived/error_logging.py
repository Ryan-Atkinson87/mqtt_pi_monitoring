"""
error_logging.py
"""
import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_dir="log", log_file_name="thingsboard_service.log"):
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, log_file_name)

    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)

    return logger