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

import sys
import os
import re
import time

# python 2 and python 3 compatibility library
from six import iteritems

from severr_client import api_client
from severr_client.apis import EventsApi

class SeverrClient(object):
    """
    Description of class
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def createAppEvent(self, classification, eventType, eventMessage): #Default None the arguments if they're not required?

        if classification is None: classification = "Error";
        if eventType  is None: eventType = 'unknown';
        if eventMessage is None: eventMessage = 'unknown';

        return AppEvent(self.apiKey, classification, eventType, eventMessage);



    def fillDefaults(self, appEvent):
        if appEvent.apiKey is None: appEvent.apiKey = self.api_key

        if appEvent.contextAppVersion  is None: appEvent.contextAppVersion = self.context_app_version
        if appEvent.contextEnvName is None: appEvent.contextEnvName = self.context_env_name
        if appEvent.contextEnvVersion  is None: appEvent.contextEnvVersion = self.context_env_version
        if appEvent.contextEnvHostname is None: appEvent.contextEnvHostname = self.context_env_hostname

        if appEvent.contextAppOS is None:
            appEvent.contextAppOS = self.context_app_os
            appEvent.contextAppOSVersion = self.context_app_os_version

        if appEvent.contextDataCenter is None: appEvent.contextDataCenter = self.contextDataCenter;
        if appEvent.contextDataCenterRegion  is None: appEvent.contextDataCenterRegion = _this.contextDataCenterRegion;

        if appEvent.eventTime is None: appEvent.eventTime = time.gmtime() * 1000; #Confirm if this is correct form of output
        return appEvent