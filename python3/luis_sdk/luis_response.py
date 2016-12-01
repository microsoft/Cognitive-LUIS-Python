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

import json
from .luis_intent import LUISIntent
from .luis_entity import LUISEntity
from .luis_composite_entity import LUISCompositeEntity
from .luis_dialog import LUISDialog

class LUISResponse:
    '''
    LUIS Response Class.
    Describes the response structure, and is the main point
    to access the response sent by LUIS after prediction.
    '''

    def __init__(self, JSONResponse):
        '''
        A constructor for the LUISResponse class.
        :param JSONResponse: A string containing the incoming JSON.
        '''
        if JSONResponse is None:
            raise TypeError('NULL JSON response')
        if not JSONResponse:
            raise ValueError('Invalid App Id')

        if isinstance(JSONResponse, str):
            try:
                response = json.loads(JSONResponse)
            except Exception:
                raise Exception('Error in parsing json')
        else:
            response = JSONResponse

        if 'statusCode' in response:
            raise Exception(u'Invalid Subscription Key')

        self._query = response['query']

        if 'dialog' in response:
            self._dialog = LUISDialog(response['dialog'])
        else:
            self._dialog = None

        self._intents = []
        self._entities = []
        self._composite_entities = []

        self._top_scoring_intent = LUISIntent(response['topScoringIntent'])
        
        if 'intents' in response:
            for intent in response['intents']:
                self._intents.append(LUISIntent(intent))
        else:
            self._intents.append(self._top_scoring_intent)
        
        for entity in response['entities']:
            self._entities.append(LUISEntity(entity))

        if 'compositeEntities' in response:
            for composite_entity in response['compositeEntities']:
                self._composite_entities.append(LUISCompositeEntity(composite_entity))

    def get_query(self):
        '''
        A getter for the response's query.
        :return: Response's query.
        '''
        return self._query

    def get_top_intent(self):
        '''
        A getter for the response's top scoring intent.
        :return: Response's top scoring intent.
        '''
        return self._top_scoring_intent

    def get_intents(self):
        '''
        A getter for the response's intents.
        :return: A list of intents.
        '''
        return self._intents

    def get_entities(self):
        '''
        A getter for the response's entities.
        :return: A list of entities.
        '''
        return self._entities

    def get_composite_entities(self):
        '''
        A getter for the response's composite entities.
        :return: A list of composite entities.
        '''
        return self._composite_entities

    def get_dialog(self):
        '''
        A getter for the response's dialog.
        :return: Response's dialog.
        '''
        return self._dialog
