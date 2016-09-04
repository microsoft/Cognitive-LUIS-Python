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

class LUISEntity:
    '''
    LUIS Entity Class.
    Describes the LUIS Entity structure.
    '''

    def __init__(self, entity):
        '''
        A constructor for the LUISEntity class.
        :param entity: A dictionary containing the entity data.
        '''
        self._name = entity['entity']
        self._type = entity['type']
        if 'startIndex' in entity:
            self._start_idx = entity['startIndex']
        else:
            self._start_idx = None
        if 'endIndex' in entity:
            self._end_idx = entity['endIndex']
        else:
            self._end_idx = None
        if 'score' in entity:
            self._score = entity['score']
        else:
            self._score = None
        if 'resolution' in entity:
            self._resolution = entity['resolution']
        else:
            self._resolution = None

    def get_name(self):
        '''
        A getter for the entity's name.
        :return: Entity's name.
        '''
        return self._name

    def get_type(self):
        '''
        A getter for the entity's type.
        :return: Entity's type.
        '''
        return self._type

    def get_start_idx(self):
        '''
        A getter for the entity's start index.
        :return: Entity's start index.
        '''
        return self._start_idx

    def get_end_idx(self):
        '''
        A getter for the entity's end index.
        :return: Entity's end index.
        '''
        return self._end_idx

    def get_score(self):
        '''
        A getter for the entity's score.
        :return: Entity's score.
        '''
        return self._score

    def get_resolution(self):
        '''
        A getter for the entity's resolution.
        :return: Entity's resolution.
        '''
        return self._resolution
