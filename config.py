from ConfigParser import SafeConfigParser, NoOptionError
import os

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG = THIS_DIR + '/config.ini'

parser = SafeConfigParser()
parser.read(CONFIG)

APP_KEY = parser.get('oauth', 'client.key')
APP_SECRET = parser.get('oauth', 'client.secret')
LOCAL_IMG_DIR = parser.get('images', 'location')

def get_key():
    return APP_KEY

def get_secret():
    return APP_SECRET

def get_img_dir():
    return LOCAL_IMG_DIR

def save_access_token(token_key, token_secret):
    parser.set('oauth', 'access.key', token_key)
    parser.set('oauth', 'access.secret', token_secret)
    parser.write(open(CONFIG, 'w'))

def get_access_token():
    try:
        return parser.get('oauth', 'access.key'), parser.get('oauth', 'access.secret')
    except NoOptionError:
        return None, None
