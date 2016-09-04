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

from .luis_composite_entity_child import LUISCompositeEntityChild

class LUISCompositeEntity:
    '''
    LUIS Composite Entity Class.
    Describes the LUIS Composite Entity structure.
    '''

    def __init__(self, composite_entity):
        '''
        A constructor for the LUISCompositeEntity class.
        :param composite_entity: A dictionary containing the composite entity data.
        '''
        self._parent_type = composite_entity['parentType']
        self._value = composite_entity['value']
        self._composite_entity_children = []
        for composite_entity_child in composite_entity['children']:
            self._composite_entity_children.append(LUISCompositeEntityChild(composite_entity_child))

    def get_parent_type(self):
        '''
        A getter for the composite entity's parent type.
        :return: Composite Entity's parent type.
        '''
        return self._parent_type

    def get_value(self):
        '''
        A getter for the composite entity's value.
        :return: Composite Entity's value.
        '''
        return self._value

    def get_children(self):
        '''
        A getter for the composite entity's children.
        :return: Composite_Entity's children.
        '''
        return self._composite_entity_children
