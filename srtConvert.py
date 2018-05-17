__author__ = 'pluther'

import logging

def setLoggingLevel(debug):
    if debug:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

def convertSRT(inFile,outFile,debug):
    setLoggingLevel(debug)
    logging.debug('Debug logging is on.')
    csvFile = open(outFile,'w')

    # First line of the csv file is the keys. Write then once before doing anything else
    csvFile.write('Date,Time,Latitude,Longitude,Height\n')
    with open(inFile) as f:
        lines = f.read().splitlines()
    for i in range(len(lines)):
        if lines[i].startswith('HOME'):
            lineparts = lines[i].split(' ')
            date = lineparts[1]
            time = lineparts[2]
            logging.debug('Date: ' + str(date))
            logging.debug('Time: ' + str(time))
            if not (lines[i+1].startswith('GPS')):
                logging.error('Line following HOME should be GPS. Instead, it is' )
                logging.error(lines[i+1])
                sys.exit(1)
            else:
                lineparts = lines[i+1].split(' ')

                longlat = lineparts[0][4:-4]
                ll = longlat.split(',')
                longitude = ll[0]
                latitude = ll[1]
                logging.debug('Latitude: ' + str(latitude))
                logging.debug('Longitude: ' + str(longitude))

                height=lineparts[1][10:]
                logging.debug('Height: ' + str(height))

            # Now that we have all the information, write it to the file:
            separator = ','
            outputLine = separator.join([date,time,latitude,longitude,height])
            csvFile.write(outputLine + '\n')





