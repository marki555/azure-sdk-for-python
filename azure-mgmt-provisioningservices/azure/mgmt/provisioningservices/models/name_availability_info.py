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


class NameAvailabilityInfo(Model):
    """Description of name availability.

    :param name_available: specifies if a name is available or not
    :type name_available: bool
    :param reason: specifies the reason a name is unavailable. Possible values
     include: 'Invalid', 'AlreadyExists'
    :type reason: str or
     ~azure.mgmt.provisioningservices.models.NameUnavailabilityReason
    :param message: message containing a etailed reason name is unavailable
    :type message: str
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, name_available=None, reason=None, message=None):
        self.name_available = name_available
        self.reason = reason
        self.message = message