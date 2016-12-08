"""
    Severr Client API

    Get your application events and errors to Severr via the *Severr API*.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from __future__ import absolute_import #Only seems to matter in py 2.5? http://stackoverflow.com/questions/33743880/what-does-from-future-import-absolute-import-actually-do

import sys
import os
import re
import traceback

from severr_client.models import *
from six import iteritems

class event_trace_builder(object):
    """
    description of class
    """

    def get_event_traces(self):
        """
        """

        trace = stacktrace()#I don't see it inheriting from any list in the swagger code. Confirm?
        einfo = sys.exc_info()
        add_stack_trace(self, trace, einfo)
        return trace

    def add_stack_trace(self, trace_list, exc_info=None):
        """
        """

        if exc_info is None: exc_info = sys.exc_info
        newTrace = inner_stack_trace()

        newTrace.trace_lines = get_event_tracelines(self, exc_info[2])
        newTrace.type = str(exc_info[0])
        newTrace.message = str(exc_info[1])
        trace_list.append(newTrace)

    def get_event_tracelines(self, tb):
        """
        """

        stacklines = stack_trace_lines()#I don't see it inheriting from any list in the swagger code. Confirm?
        line = stack_trace_line()

        for filename, line, func, text in traceback.extract_tb(trace):
            line.file = str(filename)
            line.line = line
            line.fuction = str(func)

        stacklines.append(line)
        return stacklines

    def format_name(self, name):
        """
        """

        raise NotImplementedError("Fuction not Implemented currently")

    def is_exc_info_tuple(self, exc_info):
        """
        """

        raise NotImpementedError("Fuction not Implemented currently")
     


def main(argv=None):#Test Main, to be removed
    if argv is None:
        argv = sys.argv
    
    try:
        x = 2/0
    except:
        trace = sys.exc_info()[2]
        for filename, line, func, text in traceback.extract_tb(trace):
            print str(text)
            


if __name__ == "__main__":
    main()
#    sys.exit(main())