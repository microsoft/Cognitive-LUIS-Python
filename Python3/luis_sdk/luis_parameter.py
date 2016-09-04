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

from .luis_parametervalue import LUISParameterValue

class LUISParameter:
    '''
    LUIS Parameter Class.
    Describes the LUIS Parameter structure.
    '''

    def __init__(self, parameter):
        '''
        A constructor for the LUISParameter class.
        :param parameter: A dictionary containing the parameter data.
        '''
        self._name = parameter['name']
        self._required = parameter['required']
        self._parameter_values = []
        if parameter['value']:
            for parameter_value in parameter['value']:
                self._parameter_values.append(LUISParameterValue(parameter_value))

    def get_name(self):
        '''
        A getter for the parameter's name.
        :return: Parameter's name.
        '''
        return self._name

    def get_required(self):
        '''
        A getter for the parameter's required flag.
        :return: A boolean that expresses whether the parameter is required or not.
        '''
        return self._required

    def get_parameter_values(self):
        '''
        A getter for the parameters's values.
        :return: A list of parameter values.
        '''
        return self._parameter_values
