﻿
import sys
import os
import re
import traceback

from severr__client import Logger



def main(argv=None):#Test Main, to be removed
    if argv is None:
        argv = sys.argv

    l = Logger()
    try:
        raise ArithmeticError("An Error Occurred.")
    except:
        l.log("Test bug")


if __name__ == "__main__":
    main()
#    sys.exit(main())