# IO.Severr.EventsApi

All URIs are relative to *https://www.severr.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_post**](EventsApi.md#events_post) | **POST** /events | Submit an application event or error to Severr


# **events_post**
> events_post(data)

Submit an application event or error to Severr

 The events endpoint submits an application event or an application error / exception with an optional stacktrace field to Severr.  ##### Sample POST request body: ``` {  \"apiKey\": \"a9a2807a2e8fd4602adae9e8f819790a267213234083\",  \"classification\": \"Error\",  \"eventType\": \"System.Exception\",  \"eventMessage\": \"This is a test exception.\",  \"eventTime\": 1479477482291,  \"eventStacktrace\": [    {      \"type\": \"System.Exception\",      \"message\": \"This is a test exception.\",      \"traceLines\": [        {          \"function\": \"Main\",          \"line\": 19,          \"file\": \"SeverrSampleApp\\\\Program.cs\"        }      ]    }  ],  \"contextAppVersion\": \"1.0\",  \"contextEnvName\": \"development\",  \"contextEnvHostname\": \"severr.io\",  \"contextAppOS\": \"Win32NT Service Pack 1\",  \"contextAppOSVersion\": \"6.1.7601.65536\" } ``` ##### Sample POST response body (200 OK): ``` { } ``` 

### Example 
```python
import time
import IO.Severr
from IO.Severr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = IO.Severr.EventsApi()
data = IO.Severr.AppEvent() # AppEvent | Event to submit

try: 
    # Submit an application event or error to Severr
    api_instance.events_post(data)
except ApiException as e:
    print "Exception when calling EventsApi->events_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AppEvent**](AppEvent.md)| Event to submit | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

