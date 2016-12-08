# coding: utf-8

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

from __future__ import absolute_import
from __builtin__ import *  # My interpreter was shirking adding this automatically on the non-generated files. Most shouldn't need this, figure out why on a second pass

import sys
import os
import re
import time

# python 2 and python 3 compatibility library
from six import iteritems

from severr_client import ApiClient
from severr_client import EventsApi
from severr_client.apis import events_api
from severr_client.models import *
from event_trace_builder import EventTraceBuilder


# http://stackoverflow.com/questions/9252543/importerror-cannot-import-name-x Reformat like the last answer?


class Logger(object):
    """
    The public facing class that will log errors.

    A use case would be like:
    import severr_client

    ...

    l = Logger()

    ...

    try:
        ...
    except:
        l.log("Optional Error String")
    """

    def log(self, message=None, classification="Error"):
        """
        
        """
        client = SeverrClient("ca6b942a89e04069ec96fa2b3438efb310995233724595",
                              "http://ec2-52-91-176-104.compute-1.amazonaws.com/api/v1", "1.0", "development",
                              "RMachine", "Win10", "10.10", "datacenter", "Datacenter region")


        exc_info = sys.exc_info()
        try:
            # Below taken from: https://docs.python.org/2/library/sys.html
            # "" Since most functions don’t need access to the
            # traceback, the best solution is to use something like exctype, value = sys.exc_info()[:2] to extract only
            # the exception type and value. If you do need the traceback, make sure to delete it after use (best done
            # with a try ... finally statement) or to call exc_info() in a function that does not itself handle an
            # exception. ""
            type, value = exc_info[:2]
            excevent = client.create_new_app_event(classification, str(type), str(value))

            excevent.event_stacktrace = EventTraceBuilder.get_event_traces(exc_info)
            client.send_event(excevent)  # use async method when implemented
        finally:
            del exc_info


class SeverrClient(object):
    """
    Description of class
    """

    # Implied class variable
    # event_Api

    # api_Key
    # context_App_Version
    # context_Env_Name
    # context_Env_Version
    # context_Env_Hostname
    # context_AppOS
    # context_AppOS_Version
    # context_DataCenter
    # context_DataCenter_Region

    def __init__(self, api_key=None, base_path=None, context_app_version=None, context_env_name="development", context_env_version=None,
                 context_env_hostname=None,
                 context_appos=None, context_appos_version=None, context_datacenter=None,
                 context_datacenter_region=None):

        # Populate default appmanager values. The C# code uses ConfigurationManager to parse and format the global App.config file.Haven't found anywhere in Python like that yet
        # Configuration.py? But that's an instanced class. Does it get the details from wherever they are stored for me? I need to put my API key somewhere.
        # ANSWER: Don't worry about the configuration manager. That's a C# only thing. Let's just go with the constructor like it is here.

        self.api_Key = api_key

        self.context_App_Version = context_app_version
        self.context_Env_Name = context_env_name
        self.context_Env_Version = context_env_version
        self.context_Env_Hostname = context_env_hostname
        self.context_AppOS = context_appos
        self.context_AppOS_Version = context_appos_version
        self.context_DataCenter = context_datacenter
        self.context_DataCenter_Region = context_datacenter_region
        if base_path is None:
            client = ApiClient()
        else:
            client = ApiClient(base_path)
        self.events_api = EventsApi(client)

    def create_new_app_event(self, classification="Error", eventType="unknown",
                             eventMessage="unknown"):  # Default None the arguments if they're not required?
        """
        """

        return AppEvent(self.api_Key, classification, eventType, eventMessage)

    def send_event(self, app_event):
        """
        """

        self.fill_defaults(app_event)
        self.events_api.events_post(app_event)

    def send_event_async(self, app_event):
        """
        """

        raise NotImplementedError("Method not implemented currently.")

    def fill_defaults(self, app_event):
        if app_event.api_key is None: app_event.apiKey = self.api_Key

        if app_event.context_app_version is None: app_event.context_app_version = self.context_App_Version
        if app_event.context_env_name is None: app_event.context_env_name = self.context_Env_Name
        if app_event.context_env_version is None: app_event.context_env_version = self.context_Env_Version
        if app_event.context_env_hostname is None: app_event.context_env_hostname = self.context_Env_Hostname

        if app_event.context_app_os is None:
            app_event.context_app_os = self.context_AppOS
            app_event.context_app_os_version = self.context_AppOS_Version

        if app_event.context_data_center is None: app_event.context_data_center = self.context_DataCenter
        if app_event.context_data_center_region is None: app_event.context_data_center_region = self.context_DataCenter_Region

        if app_event.event_time is None: app_event.event_time = time.gmtime() * 1000  # Confirm if this is correct form of output
        # ANSWER: This is not correct as it doesn't offer millisecond granulatity
        return app_event
