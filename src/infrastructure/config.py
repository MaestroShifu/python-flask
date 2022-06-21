import os
from dotenv import load_dotenv

FILE_NAME: str = os.path.abspath('.env')
load_dotenv(FILE_NAME)

class Config(object):
    TEST_URL: str = os.environ.get('TEST_URL')