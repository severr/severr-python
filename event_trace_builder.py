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



def main(argv=None):#Test Main
    if argv is None:
        argv = sys.argv




if __name__ == "__main__":
    sys.exit(main())


class event_trace_builder(object):
    """
    description of class
    """
    
    def __init__(self):#Might not need init
        return NotImplemented

    def getEventTraces(self, exception):
        if exception is None: return None
        trace = stacktrace()
        addStackTrace(self, trace, exception)
        return trace

    def addStackTrace(self, traceList, exception):
        newTrace = inner_stack_trace()
        catchingmethod #Reflection for calling method

        newTrace.trace_lines = getEventTraceLines(self, exception, catchingmethod) #Continue on, need reflection and to get the error name
        #Discusss arbreak lines 133-176 to put in exception error stack

        return NotImplemented

    def getEventTraceLines(self, exception, catchingMethod):
        return NotImplemented