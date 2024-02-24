import logging
import os

from from_root import from_root
from datetime import datetime

Log_file = f"{datetime.now().strftime('%m_%d%_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, Log_file)

os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(filename=logs_path, level=logging.DEBUG, format=" [ %(asctime)s ] %(levelname)s - %(message)s"