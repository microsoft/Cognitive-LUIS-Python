'''
Copyright (c) Microsoft. All rights reserved.
Licensed under the MIT license.

Microsoft Cognitive Services (formerly Project Oxford): https://www.microsoft.com/cognitive-services

Microsoft Cognitive Services (formerly Project Oxford) GitHub:
https://github.com/Microsoft/ProjectOxford-ClientSDK

Copyright (c) Microsoft Corporation
All rights reserved.

MIT License:
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ""AS IS"", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from luis_sdk import LUISClient

def on_success(res):
    '''
    A callback function that processes the luis_response object
    if the prediction succeeds.
    :param res: a luis_response object containing the response data.
    :return: None
    '''
    print('---------------------------------------------')
    print('LUIS Response: ')
    print('Query: ' + res.get_query())
    print('Top Scoring Intent: ' + res.get_top_intent().get_name())
    if res.get_dialog() is not None:
        if res.get_dialog().get_prompt() is None:
            print('Dialog Prompt: None')
        else:
            print('Dialog Prompt: ' + res.get_dialog().get_prompt())
        if res.get_dialog().get_parameter_name() is None:
            print('Dialog Parameter: None')
        else:
            print('Dialog Parameter Name: ' + res.get_dialog().get_parameter_name())
        print('Dialog Status: ' + res.get_dialog().get_status())
    print('Entities:')
    for entity in res.get_entities():
        print('"%s":' % entity.get_name())
        print('Type: %s, Score: %s' % (entity.get_type(), entity.get_score()))

def on_failure(err):
    '''
    A callback function that processes the error object
    if the prediction fails.
    :param err: An Exception object.
    :return: None
    '''
    print(err)

try:
    APPID = input('Please enter your app Id:\n')
    APPKEY = input('Please input your subscription key:\n')
    TEXT = input('Please input the text to predict:\n')
    CLIENT = LUISClient(APPID, APPKEY, True)
    CLIENT.predict(TEXT, {'on_success': on_success, 'on_failure': on_failure})
    print('-------\nMain thread finishing!!\n-------')
except Exception as exc:
    print(exc)
