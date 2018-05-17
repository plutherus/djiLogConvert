__author__ = 'pluther'

import srtConvert
import argparse
import logging
import os


parser = argparse.ArgumentParser(description='Converts a .SRT file from a DJI drone to csv format')
parser.add_argument('--debug', '-d', help='Runs script in debug mode', action='store_true', default=False)
parser.add_argument('--inputFile', '--input', '-f', '-i', help='Location of original .SRT file', required=True)
parser.add_argument('--outputFile', '--output', '-o', help='File to store the csv in')
args = parser.parse_args()

#Set logging level:
if args.debug:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    debug = True
else:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    debug = False

inFile = args.inputFile

if (args.outputFile):
    logging.debug('Output file is given as ' + args.outputFile)
    outFile = args.outputFile
else:
    outFile = os.path.splitext(inFile)[0] + '.csv'

logging.info('Reading DJI Subtitles from ' + inFile)

srtConvert.convertSRT(inFile,outFile, debug)

logging.info('Output was written to ' + outFile)
