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
from __builtin__ import * #My interpreter was shirking adding this automatically on the non-generated files. Most shouldn't need this, figure out why on a second pass

import sys
import os
import re
import traceback

from severr_client.models import *
from six import iteritems


class EventTraceBuilder(object):
    """
    description of class

    All members are classmethods since we instance the stacktrace and we want to keep multiple stack traces seperate.
    """

    @classmethod
    def get_event_traces(self, exc_info = None):
        """
        """

        trace = Stacktrace()
        if exc_info is None: exc_info = sys.exc_info()

        self.add_stack_trace(trace, exc_info)
        return trace

    @classmethod
    def add_stack_trace(self, trace_list, exc_info=None):
        """
        """

        if exc_info is None: exc_info = sys.exc_info
        newTrace = InnerStackTrace()

        for type, value, tb in exc_info:
            newTrace.trace_lines = self.get_event_tracelines(tb)
            newTrace.type = str(type)
            newTrace.message = str(value)
        trace_list.append(newTrace)

    @classmethod
    def get_event_tracelines(self, tb):
        """
        """

        stacklines = StackTraceLines()
        line = StackTraceLine()

        for filename, line, func, text in traceback.extract_tb(trace):
            line.file = str(filename)
            line.line = line
            line.function = str(func)

        stacklines.append(line)
        return stacklines

    @classmethod
    def format_name(self, name):
        """
        """

        raise NotImplementedError("Method not implemented currently.")

    @classmethod
    def is_exc_info_tuple(self, exc_info):
        """
        """

        raise NotImpementedError("Method not implemented currently.")
     


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