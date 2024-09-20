import logging
import sys

logger = logging.getLogger('telegram_bot')
logger.setLevel(logging.DEBUG)  # Логируем все, начиная от уровня DEBUG

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler('telegram_bot.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
