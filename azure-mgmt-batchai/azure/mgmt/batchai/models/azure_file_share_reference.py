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


class AzureFileShareReference(Model):
    """Details of the Azure File Share to mount on the cluster.

    :param account_name: Name of the storage account.
    :type account_name: str
    :param azure_file_url: URL to access the Azure File.
    :type azure_file_url: str
    :param credentials: Information of the Azure File credentials.
    :type credentials: :class:`AzureStorageCredentialsInfo
     <azure.mgmt.batchai.models.AzureStorageCredentialsInfo>`
    :param relative_mount_path: Specifies the relative path on the compute
     node where the Azure file share will be mounted. Note that all file shares
     will be mounted under $AZ_BATCHAI_MOUNT_ROOT location.
    :type relative_mount_path: str
    :param file_mode: Specifies the file mode. Default value is 0777. Valid
     only if OS is linux. Default value: "0777" .
    :type file_mode: str
    :param directory_mode: Specifies the directory Mode. Default value is
     0777. Valid only if OS is linux. Default value: "0777" .
    :type directory_mode: str
    """

    _validation = {
        'account_name': {'required': True},
        'azure_file_url': {'required': True},
        'credentials': {'required': True},
        'relative_mount_path': {'required': True},
    }

    _attribute_map = {
        'account_name': {'key': 'accountName', 'type': 'str'},
        'azure_file_url': {'key': 'azureFileUrl', 'type': 'str'},
        'credentials': {'key': 'credentials', 'type': 'AzureStorageCredentialsInfo'},
        'relative_mount_path': {'key': 'relativeMountPath', 'type': 'str'},
        'file_mode': {'key': 'fileMode', 'type': 'str'},
        'directory_mode': {'key': 'directoryMode', 'type': 'str'},
    }

    def __init__(self, account_name, azure_file_url, credentials, relative_mount_path, file_mode="0777", directory_mode="0777"):
        self.account_name = account_name
        self.azure_file_url = azure_file_url
        self.credentials = credentials
        self.relative_mount_path = relative_mount_path
        self.file_mode = file_mode
        self.directory_mode = directory_mode
