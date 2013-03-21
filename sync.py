import authentication
from os import listdir
from time import sleep
import config

FIVE_MINUTES = 60 * 5

img_dir = config.get_img_dir()
client = authentication.get_client()

def upload(image):
    f = open(img_dir + image)
    client.put_file(image, f)

    print 'Uploaded file: ' + image

def get_new_images():
    remote_file_names = map(lambda file: file['path'][1:], client.metadata('/')['contents'])
    local_file_names = listdir(img_dir)

    return filter(lambda f: f not in remote_file_names, local_file_names)

def check_files():
    new_images = get_new_images()

    if len(new_images) > 0:
        print 'Found ' + str(len(new_images)) + ' new images.'

    for image in new_images: upload(image)

while True:
    check_files();
    sleep(FIVE_MINUTES)