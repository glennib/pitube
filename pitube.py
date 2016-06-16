#!/usr/bin/env python

import sys
import os
import argparse
from time import time, sleep
from pprint import pprint

if __name__== '__main__':
    scriptdir = os.path.dirname(os.path.realpath(__file__))
    parser = argparse.ArgumentParser(description='Input a YouTube URL and listen to the sound.')
    parser.add_argument('url', action='store', type=str, help='YouTube URL')

    args = parser.parse_args()

    print('Fetching url... Patience...')
    output = os.popen('youtube-dl -g ' + args.url).read()
    output = output.strip('\n')
    output = output.split('\n')
    nlines = len(output)

#    pprint(output)
    pprint(nlines)

    print('Playing with omxplayer. Here are some commands:\n')
    with open(scriptdir + '/omxcommands.txt', 'rb') as file:
        print(file.read())


    os.system('omxplayer "' + output[-1] + '"')
