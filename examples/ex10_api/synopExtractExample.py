import traceback
import sys

from eccodes import *

VERBOSE = 1  # verbose error reporting
# open bufr file
f = open(sys.argv[1], "rb")

# loop for the messages in the file
while 1:
    # get handle for message
    bufr = codes_bufr_new_from_file(f)
    if bufr is None:
        break

    codes_set(bufr, 'unpack', 1)

    try: 
    
        compressed = codes_get(bufr,'compressedData')
        numberOfSubsets = codes_get(bufr,'numberOfSubsets')
        print "Number of Subsets %d"  % (numberOfSubsets)
        
        if compressed:
            print "not implemented"
        else:

            for i in range(numberOfSubsets):
                blockNo = codes_get(bufr,'/subsetNumber=' + str(i+1) + '/blockNumber')
                stationNo = codes_get(bufr,'/subsetNumber=' + str(i+1) + '/stationNumber')

                t2m = codes_get(bufr,'/subsetNumber=' + str(i+1) + '/airTemperature')
                rh = codes_get(bufr,'/subsetNumber=' + str(i+1) + '/relativeHumidity')
                print "Subset: %d Station %.2d%.3d T2m %f RH %f " % (i+1, blockNo, stationNo, t2m, rh)

    except CodesInternalError as err:
        print 'Loop: Error with key="%s" : %s' % (key, err.msg)

    # delete handle
    codes_release(bufr)

# close the file
f.close()
