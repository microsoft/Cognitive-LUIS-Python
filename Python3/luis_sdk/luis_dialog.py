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

class LUISDialog:
    '''
    LUIS Dialog Class.
    Describes the LUIS Action structure.
    '''

    def __init__(self, dialog):
        '''
        A constructor for the LUISDialog class.
        :param action: A dictionary containing the dialog data.
        '''
        if 'prompt' in dialog:
            self._prompt = dialog['prompt']
        else:
            self._prompt = None

        if 'parameterName' in dialog:
            self._parameter_name = dialog['parameterName']
        else:
            self._parameter_name = None

        self._context_id = dialog['contextId']
        self._status = dialog['status']
        self._finished = self._status == 'Finished'

    def get_prompt(self):
        '''
        A getter for the dialog's prompt.
        :return: Dialog's prompt.
        '''
        return self._prompt

    def get_parameter_name(self):
        '''
        A getter for the dialog's parameter name.
        :return: Dialog's parameter name.
        '''
        return self._parameter_name

    def get_context_id(self):
        '''
        A getter for the dialog's context Id.
        :return: Dialog's prompt.
        '''
        return self._context_id

    def get_status(self):
        '''
        A getter for the dialog's status.
        :return: Dialog's status.
        '''
        return self._status

    def is_finished(self):
        '''
        Checks whether the dialog has finished or not.
        :return: A boolean that expresses whether the dialog has finished or not.
        '''
        return self._finished
