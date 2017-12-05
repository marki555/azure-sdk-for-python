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


class CertificateResponse(Model):
    """The X509 Certificate.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param properties: properties of a certificate
    :type properties:
     ~azure.mgmt.provisioningservices.models.CertificateProperties
    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The name of the certificate.
    :vartype name: str
    :ivar etag: The entity tag.
    :vartype etag: str
    :ivar type: The resource type.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'etag': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'CertificateProperties'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, properties=None):
        self.properties = properties
        self.id = None
        self.name = None
        self.etag = None
        self.type = None