#!/usr/bin/env python

'''



'''

import argparse, os, sys, glob, json, requests

def caption(url, key):
    '''

    '''
    return "a"

def upload(img):
    '''

    '''

    api_url = "http://uploads.im/api"
    request = requests.post(api_url, files={'img': open(img, 'rb')})
    data = json.loads(request.text)["data"]
    return(data["img_url"])

def rename(path, key):
    '''

    '''

    # check if valid path for a file/dir
    if not os.path.exists(path):
        sys.exit('file or directory not found')

    extensions = (".jpg", ".png")

    # check if file/dir is valid and list all the files to process
    if os.path.isfile(path):
        if path.lower().endswith(extensions):
            tocaption = [path]
        else:
            sys.exit('file is not a valid image')
    else:
        tocaption = []
        for extension in extensions:
            tocaption.extend(glob.glob("*" + extension))

    # for each file upload it to uploads.im and send it to caption
    for img in tocaption:
        # upload the img to uploads.im and get the url
        uploaded_url = upload(img)

        if uploaded_url:
            caption_text = caption(uploaded_url, key)

            # get file extension and rename file with the caption
            file_extension = os.path.splitext(img)[1]
            os.rename(img, caption_text + file_extension)


if __name__ == '__main__':
    '''

    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path of the file or directory to use', action='store')
    parser.add_argument('key', help='Microsoft API\'s key', action='store')
    args = parser.parse_args()
    rename(args.path, args.key)
