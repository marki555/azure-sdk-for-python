# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TermData(Model):
    """Gets all term Id response properties.

    :param language: Language of the terms.
    :type language: str
    :param terms: List of terms.
    :type terms:
     list[~azure.cognitiveservices.vision.contentmoderator.models.TermsInList]
    :param status: Get Term Status.
    :type status:
     ~azure.cognitiveservices.vision.contentmoderator.models.AddGetRefreshStatus
    :param tracking_id: Tracking Id.
    :type tracking_id: str
    """

    _attribute_map = {
        'language': {'key': 'language', 'type': 'str'},
        'terms': {'key': 'terms', 'type': '[TermsInList]'},
        'status': {'key': 'status', 'type': 'AddGetRefreshStatus'},
        'tracking_id': {'key': 'trackingId', 'type': 'str'},
    }

    def __init__(self, language=None, terms=None, status=None, tracking_id=None):
        self.language = language
        self.terms = terms
        self.status = status
        self.tracking_id = tracking_id
