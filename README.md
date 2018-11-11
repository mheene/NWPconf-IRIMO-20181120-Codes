# NWPconf-IRIMO-20181120-Codes

This repository contains the presentation slides with all excercises and tools for my prestation at the ["First International Conference on Numerical Weather and Climate Prediction"](http://nwpconf.irimo.ir/) in Tehran.

# Slides
The presentation contains two parts. Part one is about "Data retrieval for data assimilation" while part two is an introdution in BUFR. In addition the presentation provides an overview in BUFR processing in particular with ecCodes.

# Examples
- Example 00 - bufr_dump (inspect a BUFR)
- Example 01 - bufr_ls (read masterTablesVersionNumber)
- Example 02 - bufr_ls (read updateSequenceNumber)
- Example 03 - bufr_compare (compare 2 BUFR)
- Example 04 - bufr_filter (extract a subset)
- Example 05 - bufr_filter (manipulate a BUFR)
- Example 06 - bufr_set (remove optional section 2)
- Example 07 - bufr_count and bufr_copy
- Example 08 - bufr_filter (national chars)
- Example 09 - bufr_filter (parse your input data)
- Example 10 - python api - parse a SYNOP message with multiple subsets

# Tools
- fetchOpendata.sh - efficient way to fetch data from https://opendata.dwd.de
- bitReader.py - print a BUFR in binary representation of 0 and 1

# data
- corruptBUFR.bin - a corrupt BUFR file

# Docker image with 3 decoders and the BUFR validation dashboard
The Docker image with 3 decoders (Geo::BUFR, libECBUFR and BUFRDC) and the BUFR validation dashboard can be found [here](https://github.com/mheene/allInOne)

[![Try in PWD](https://raw.githubusercontent.com/play-with-docker/stacks/master/assets/images/button.png)](https://labs.play-with-docker.com/?stack=https://raw.githubusercontent.com/mheene/allInOne/master/stack.yml)


