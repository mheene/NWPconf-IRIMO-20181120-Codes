# NWPconf-IRIMO-20181120-Codes

This repository contains the presentation slides with all excercises and tools for my prestation at the ["First International Conference on Numerical Weather and Climate Prediction"](http://nwpconf.irimo.ir/) in Tehran.

# Slides
The presentation contains two parts. Part one is about "Data retrieval for data assimilation" while part two is an introdution in BUFR. In addition the presentation provides an overview in BUFR processing in particular with ecCodes.

# Examples
- [Example 00](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/ex00-bufr_dump) - bufr_dump (inspect a BUFR)
- [Example 01](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/ex01-masterTableVersion) - bufr_ls (read masterTablesVersionNumber)
- [Example 02](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/ex02-updateSequenceNumber) - bufr_ls (read updateSequenceNumber)
- [Example 03](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/ex03-bufr_compare) - bufr_compare (compare 2 BUFR)
- [Example 04](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/ex04-bufr_filter) - bufr_filter (extract a subset)
- [Example 05](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/ex05-bufr_filter) - bufr_filter (manipulate a BUFR)
- [Example 06](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/ex06-bufr_set) - bufr_set (remove optional section 2)
- [Example 07](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/ex07-bufr_copy) - bufr_count and bufr_copy
- [Example 08](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/ex08_nationalChars) - bufr_filter (national chars)
- [Example 09](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/ex09_sanityChecks) - bufr_filter (parse your input data)
- [Example 10](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/ex10_api) - python api - parse a SYNOP message with multiple subsets

# Tools
- [fetchOpendata.sh](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/blob/master/tools/fetchOpenData.sh) - efficient way to fetch data from https://opendata.dwd.de
- [bitReader.py](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/blob/master/tools/bitReader.py) - print a BUFR in binary representation of 0 and 1

# data
- [corruptBUFR.bin](https://github.com/mheene/NWPconf-IRIMO-20181120-Codes/tree/master/examples/data) - a corrupt BUFR file

# Docker image with 3 decoders and the BUFR validation dashboard
The Docker image with 3 decoders (Geo::BUFR, libECBUFR and BUFRDC) and the BUFR validation dashboard can be found [here](https://github.com/mheene/allInOne)

[![Try in PWD](https://raw.githubusercontent.com/play-with-docker/stacks/master/assets/images/button.png)](https://labs.play-with-docker.com/?stack=https://raw.githubusercontent.com/mheene/allInOne/master/stack.yml)


