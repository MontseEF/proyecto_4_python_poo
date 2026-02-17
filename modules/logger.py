import logging
import os

LOG_PATH = "logs/app.log"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message: str) -> None:
    logging.info(message)

def log_error(message: str) -> None:
    logging.error(message)
