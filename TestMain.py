
import sys
import os
import re

from severr__client import Logger



def main(argv=None):#Test Main, to be removed
    if argv is None:
        argv = sys.argv

    l = Logger()
    try:
        x = 2/0
    except:
        l.log("Test bug")
        
            


if __name__ == "__main__":
    main()
#    sys.exit(main())