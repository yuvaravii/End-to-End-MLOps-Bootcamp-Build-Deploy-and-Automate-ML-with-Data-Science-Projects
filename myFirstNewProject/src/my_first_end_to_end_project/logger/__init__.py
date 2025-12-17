import os 
import sys
import logging

logging_str = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"

log_dir = "my_execution_logs"
log_file = os.path.join(log_dir, "logged_summary.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)  # shows logging in console/terminal
    ]
)

logger = logging.getLogger("myProjectLogger")
