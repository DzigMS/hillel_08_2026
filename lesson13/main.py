import logging
import time
from logging import Formatter
from logging import config

from lesson12.model import Triangle

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.StreamHandler(),
#         logging.FileHandler('custom.log', mode='w'),
#     ]
# )
config.fileConfig('log_config.ini')
logging._levelToName.setdefault(25, "Own Level")

log = logging.getLogger(__name__)

while True:
    log.error('Start program')
    answer = input('Do you want to continue? (y/n)\n')
    if answer == 'n':
        break
    try:
        # t2 = Triangle(1, 2, 3)
        # t = Triangle(1, 2, 5)
        values = input("Give me triangle sides by comma separated\n")
        sides = [int(v.rstrip()) for v in values.split(',')]
        triangle = Triangle(*sides)
    except Exception as e:
        print('Exception captured')
    log.error('Go to next cycle')
