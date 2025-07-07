import logging

# Configure the logger
logger = logging.getLogger("sremate")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler("sremate.log")
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(file_handler)