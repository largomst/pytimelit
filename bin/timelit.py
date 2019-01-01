# bin/python
# encoding: utf-8

import os
import time
import glob
import random
import datetime
import platform

DEBUG = platform.platform().find('Windows') >= 0

if DEBUG:
    image_path_prefix = '/mnt/base-us/extensions/pytimelit/bin/images/metadata/'

    def show(image):
        print("清空")
        print("显示{}".format(image))

else:
    image_path_prefix = '/mnt/base-us/extensions/pytimelit/bin/images/metadata/'

    def show(image):
        # clear screen
        os.system('eips -c')
        # show new image
        os.system('eips -g {}'.format(image))


def main():
    show(image_path_prefix + 'quote_Leg_0_credits.png')

    while True:
        now = datetime.datetime.now()
        now_time = now.strftime('%H%M')
        image_name = "quote_{}_*_credits.png"
        images = glob.glob(image_path_prefix + image_name.format(now_time))

        FAST_MODE = 120 if 500 < int(now_time) < 2300 else 900

        if len(images) > 0:
            show(random.choice(images))
            time.sleep(FAST_MODE)
        else:
            time.sleep(60)


if __name__ == "__main__":
    main()
