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
from __builtin__ import * #My interpreter was shirking adding this automatically on the non-generated files. Most shouldn't need this, figure out why on a second pass

import sys
import os
import re
import time
import event_trace_builder

# python 2 and python 3 compatibility library
from six import iteritems

from severr_client import api_client #import isn't catching? Check this import
from severr_client.apis import events_api
from severr_client.models import *


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

    def log(self, message = None):
        """
        
        """
        client = SeverrClient()
        excinfo = sys.exc_info()
        excevent = None #Very C type declaration, might not need it if python doesn't consider the for scoped; I can't remember

        for type, value, _ in excinfo:
            excevent = client.create_new_app_event(message, str(type), str(value))
        
        excevent.event_stacktrace = EventTraceBuilder.get_event_traces(exc_info)
        client.send_event(excevent) #use async method when implemented
        



class SeverrClient(object):
    """
    Description of class
    """
    
    #Implied class variable 
    #event_Api
    
    #api_Key
    #context_App_Version
    #context_Env_Name
    #context_Env_Version
    #context_Env_Hostname
    #context_AppOS
    #context_AppOS_Version
    #context_DataCenter
    #context_DataCenter_Region

    def __init__(self, api_key = None, context_app_version = None, context_env_name = "development", context_env_version = None, context_env_hostname = None,
                 context_appos = None, context_appos_version = None, context_datacenter = None, context_datacenter_region = None):

        #Populate default appmanager values. The C# code uses ConfigurationManager to parse and format the global App.config file.Haven't found anywhere in Python like that yet
        #Configuration.py? But that's an instanced class. Does it get the details from wherever they are stored for me? I need to put my API key somewhere.


        self.api_Key = api_key

        self.context_App_Version = context_app_version
        self.context_Env_Name = context_env_name
        self.context_Env_Version = context_env_version
        self.context_Env_Hostname = context_env_hostname
        self.context_AppOS = context_appos
        self.context_AppOS_Version = context_appos_version
        self.context_DataCenter = context_datacenter
        self.context_DataCenter_Region = context_datacenter_region

    def create_new_app_event(self, classification = "Error", eventType = "unknown", eventMessage = "unknown"): #Default None the arguments if they're not required?
        """
        """

        return AppEvent(self.apiKey, classification, eventType, eventMessage)

    def send_event(self, app_event):
        """
        """

        fill_defaults(app_event)
        event_API.events_post(app_event)

    def send_event_async(self, app_event):
        """
        """

        raise NotImplementedError("Method not implemented currently.")

    def fill_defaults(self, app_event):
        if app_event.apiKey is None: app_event.apiKey = self.api_Key

        if app_event.contextAppVersion  is None: app_event.contextAppVersion = self.context_App_Version
        if app_event.contextEnvName is None: app_event.contextEnvName = self.context_Env_Name
        if app_event.contextEnvVersion  is None: app_event.contextEnvVersion = self.context_Env_Version
        if app_event.contextEnvHostname is None: app_event.contextEnvHostname = self.context_Env_Hostname

        if app_event.contextAppOS is None:
            app_event.contextAppOS = self.context_AppOS
            app_event.contextAppOSVersion = self.context_AppOS_Version

        if app_event.contextDataCenter is None: app_event.contextDataCenter = self.context_DataCenter
        if app_event.contextDataCenterRegion  is None: app_event.contextDataCenterRegion = self.context_DataCenter_Region

        if app_event.eventTime is None: app_event.eventTime = time.gmtime() * 1000 #Confirm if this is correct form of output
        return app_event