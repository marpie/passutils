#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" flatten_wordlist

    flatten_wordlist takes a input-file and removes all occurences of ...
        - word
        - Word
        - WORD
    ... and just returns "word".

    Author: marpie (marpie+passutils@a12d404.net)

    Last Update:  20120612
    Created:      20120612

"""
import sys

# Version Information
__version__ = "0.0.1"
__program__ = "flatten_wordlist v" + __version__
__author__ = "marpie"
__email__ = "marpie+passutils_flatten_wordlist@a12d404.net"
__license__ = "BSD License"
__copyright__ = "Copyright 2012, a12d404.net"
__status__ = "Prototype"  # ("Prototype", "Development", "Testing", "Production")

#SCRIPT_PATH = os.path.dirname( os.path.realpath( __file__ ) )


# Main
def main(argv):
    print("[*] Preparing input file...")
    i = 0
    special = {}
    normal = {}
    with open(argv[2], 'r') as f:
        for line in f:
            if i > 15000:
                sys.stdout.write(".")
                sys.stdout.flush()
                i = 0
            i += 1
            
            password = line.strip()
            lower_case = password.lower()
            if lower_case == password:
                normal[password] = 1
                continue
            
            upper_case = password.upper()
            if upper_case == password:
                normal[lower_case] = 1
                continue
            
            capital_case = password.capitalize()
            if capital_case == password:
                normal[lower_case] = 1
                continue
            
            special[password] = 1
    
    print("\n\n[*] Writing output file...")
    i = 0
    with open(argv[1], 'w') as f:
        for password in normal.iterkeys():
            if i > 15000:
                sys.stdout.write(".")
                sys.stdout.flush()
                i = 0
            i += 1
            f.write(password + chr(0x0A))
        
        for password in special.iterkeys():
            if i > 15000:
                sys.stdout.write(".")
                sys.stdout.flush()
                i = 0
            i += 1
            f.write(password + chr(0x0A))
    
    print("\n\n[X] Done.")
    
    return True


if __name__ == "__main__":
    import sys
    print( __doc__ )
    sys.exit( not main( sys.argv ) )
