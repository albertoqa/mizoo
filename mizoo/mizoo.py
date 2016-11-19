#!/usr/bin/env python

'''
Mizoo rename all your photos with a description of what is in them.
It uses Microsoft Computer Vision API's to describe what it sees on
the image and rename the file to that description.

By naming your photos with a description of the content you will
never have to dig up an old photo from your library ever again, just
search for the content!

Warning: Machines are not very good at captioning yet so don't trust
this to much...

Usage: > mizoo directory key
'''

import argparse, os, sys, glob, json, requests, http, urllib

uploads_api = "http://uploads.im/api"
caption_api = "https://api.projectoxford.ai/vision/v1.0/describe?"

def caption(url, key):
    '''
    Return the caption for the imagen on the given url. A valid Microsoft API's
    key must be given.
    -----------------------------------------
    url: the url of the image to analyze
    key: a valid Microsoft API's key

    return: caption for the image
    '''

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Content-Type': 'application/json',
    }

    data = json.dumps({"Url": url}, separators=(',',':'))

    # make request to the api and process the response
    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/vision/v1.0/describe?", data, headers)
        response = conn.getresponse()
        data = json.loads(response.read().decode())
        return(data['description']['captions'][0]["text"])
        conn.close()
    except Exception as e:
        print(e)

def upload(img):
    '''
    Stream the given image to uploads.im api.
    -----------------------------------------
    img: path of the image

    returns: the url of the uploaded image
    '''

    # post the img to uploads.im
    request = requests.post(uploads_api, files={'img': open(img, 'rb')})
    data = json.loads(request.text)["data"]

    # return the url of the uploaded image
    return(data["img_url"])

def rename(path, key):
    '''
    Rename the photo-s in the given path using the Microsoft Computer Vision
    API's to describe them.
    -----------------------------------------

    path: file/dir of the images to rename
    key:  Microsoft's API key
    '''

    # check if valid path for a file/dir
    if not os.path.exists(path):
        sys.exit('file or directory not found')

    extensions = (".jpg", ".png", ".gif", ".bpm")

    # check if file/dir is valid and list all the files to process
    if os.path.isfile(path):
        if path.lower().endswith(extensions):
            tocaption = [path]
        else:
            sys.exit('file is not a valid image')
    else:
        tocaption = []
        for extension in extensions:
            tocaption.extend(glob.glob(path + "*" + extension))

    print('Processing...')
    # print(tocaption)
    # for each file upload it to uploads.im and send it to caption
    for img in tocaption:
        # upload the img to uploads.im and get the url
        uploaded_url = upload(img)

        if uploaded_url:
            caption_text = caption(uploaded_url, key)

            # get file extension and rename file with the caption
            file_extension = os.path.splitext(img)[1]
            prev_path = os.path.dirname(img)
            os.rename(img, prev_path + "/" + caption_text + file_extension)

    print('Success')

def main():
    '''
    Parse arguments and start the renaming.
    -----------------------------------------

    path: path of the file or directory to rename
    key: Microsoft API's key
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path of the file or directory to use', action='store')
    parser.add_argument('key', help='Microsoft API\'s key', action='store')
    args = parser.parse_args()
    rename(args.path, args.key)

if __name__ == '__main__':
    main()
