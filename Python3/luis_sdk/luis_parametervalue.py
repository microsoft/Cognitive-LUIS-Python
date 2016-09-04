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

class LUISParameterValue:
    '''
    LUIS Paramater Value Class.
    Describes the LUIS Paramter Value structure.
    '''

    def __init__(self, parameter_value):
        '''
        A constructor for the LUISAction class.
        :param parameter_value: A dictionary containing the parameter value data.
        '''
        self._name = parameter_value['entity']
        self._type = parameter_value['type']
        if 'score' in parameter_value:
            self._score = parameter_value['score']
        else:
            self._score = None
        if 'resolution' in parameter_value:
            self._resolution = parameter_value['resolution']
        else:
            self._resolution = None


    def get_name(self):
        '''
        A getter for the parameter value's name.
        :return: Parameter value's name.
        '''
        return self._name

    def get_type(self):
        '''
        A getter for the parameter value's type.
        :return: Parameter value's type.
        '''
        return self._type

    def get_score(self):
        '''
        A getter for the parameter value's score.
        :return: Parameter value's score.
        '''
        return self._score

    def get_resolution(self):
        '''
        A getter for the parameter value's resolution.
        :return: Parameter value's resolution.
        '''
        return self._resolution
