from loguru import logger
import os
import sys

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger.remove()

logger.add(
    f"{log_dir}/pipeline.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG"
)

logger.add(
    sys.stdout,
    format="{time:HH:mm:ss} | {level: <8} | {message}",
    level="INFO"
)

app_logger = logger
