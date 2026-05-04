import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"

# ✅ create folder only
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# ✅ then create file path
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
if __name__ == "__main__":
    logging.info("Logging has started.")