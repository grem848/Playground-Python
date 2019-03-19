# Exercise 2 - 20-CLI arguments and a better webget module
# Implement the whole program, using https://hackernews.com as a test URL:

# 1. Implement the download part
#       * If no destination file was specified, save the file in default_file.dat
# 2. Improve the code: if no destination file was specified, use the last subset of the URL as the name for the file
# 3. Improve the code: if no destination file was specified, use the MIME-type of the HTTP header to guess the file extension


# bash commands: 
# python 20-cli-exercise2.py -h
# python 20-cli-exercise2.py https://dr.dk
# python 20-cli-exercise2.py https://dr.dk -d dr.html

import os
import requests
import argparse

def download(url, des="default_file.exe"):
    r = requests.get(url, allow_redirects=True)
    open(des, 'wb').write(r.content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('URL', help='an integer for the accumulator')
    parser.add_argument('-d', '--destination', default='default_file.dat', help='The name of the file to store the url in')
    args = parser.parse_args()
    download(args.URL, args.destination)
    print("URL: " + args.URL)
    print("Destination: " + args.destination)
    if args.destination == 'default_file.dat':
        print("Saved to default file!")

