#!/usr/bin/env python

'''



'''

import argparse, os, sys, glob

def rename(path, key):
    '''

    '''



    # file or dir?
    # recursive dir search?
    # detect images -> only png and jpg now
    # once I have the list of images....
    # for each one upload it to uploads.im

    # check if valid path for a file/dir
    if not os.path.exists(path):
        sys.exit('file or directory not found')

    extensions = (".jpg", ".png")

    if os.path.isfile(path):
        if path.lower().endswith(extensions):
            r = [path]
        else:
            sys.exit('file is not a valid image')
    else:
        r = []
        for extension in extensions:
            r.extend(glob.glob("*" + extension))

    print(r)


if __name__ == '__main__':
    '''

    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path of the file or directory to use', action='store')
    parser.add_argument('key', help='Microsoft API\'s key', action='store')
    args = parser.parse_args()
    rename(args.path, args.key)
