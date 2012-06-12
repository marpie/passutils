#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" remove_count

    remove_count takes a input-file and removes the password
    count at the beginning of the line.

    Author: marpie (marpie+passutils@a12d404.net)

    Last Update:  20120612
    Created:      20120612

"""
# Imports

# Version Information
__version__ = "0.0.1"
__program__ = "remove_count v" + __version__
__author__ = "marpie"
__email__ = "marpie+passutils_remove_count@a12d404.net"
__license__ = "BSD License"
__copyright__ = "Copyright 2012, a12d404.net"
__status__ = "Prototype"  # ("Prototype", "Development", "Testing", "Production")

#SCRIPT_PATH = os.path.dirname( os.path.realpath( __file__ ) )


# Main
def main(argv):
    count_size = 8
    with open(argv[1], 'w') as out_file:
        with open(argv[2], 'r') as in_file:
            for line in in_file:
                password = line[count_size:].strip()
                out_file.write(password + chr(0x0A))
    
    return True


if __name__ == "__main__":
    import sys
    print( __doc__ )
    sys.exit( not main( sys.argv ) )
