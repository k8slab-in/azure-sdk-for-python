# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SparkBatchOperations(object):
    """SparkBatchOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        workspace_name,  # type: str
        spark_pool_name,  # type: str
        from_parameter=None,  # type: Optional[int]
        size=None,  # type: Optional[int]
        detailed=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ExtendedLivyListBatchResponse"
        """List all spark batch jobs which are running under a particular spark pool.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand" targets the ondemand pool.
        :type spark_pool_name: str
        :param from_parameter: Optional param specifying which index the list should begin from.
        :type from_parameter: int
        :param size: Optional param specifying the size of the returned list.
                     By default it is 20 and that is the maximum.
        :type size: int
        :param detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :type detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExtendedLivyListBatchResponse or the result of cls(response)
        :rtype: ~azure.synapse.models.ExtendedLivyListBatchResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ExtendedLivyListBatchResponse"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if from_parameter is not None:
            query_parameters['from'] = self._serialize.query("from_parameter", from_parameter, 'int')
        if size is not None:
            query_parameters['size'] = self._serialize.query("size", size, 'int')
        if detailed is not None:
            query_parameters['detailed'] = self._serialize.query("detailed", detailed, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('ExtendedLivyListBatchResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/batches'}

    def create(
        self,
        workspace_name,  # type: str
        spark_pool_name,  # type: str
        livy_request,  # type: "models.ExtendedLivyBatchRequest"
        detailed=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ExtendedLivyBatchResponse"
        """Create new spark batch job.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand" targets the ondemand pool.
        :type spark_pool_name: str
        :param livy_request: Livy compatible batch job request payload.
        :type livy_request: ~azure.synapse.models.ExtendedLivyBatchRequest
        :param detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :type detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExtendedLivyBatchResponse or the result of cls(response)
        :rtype: ~azure.synapse.models.ExtendedLivyBatchResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ExtendedLivyBatchResponse"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if detailed is not None:
            query_parameters['detailed'] = self._serialize.query("detailed", detailed, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(livy_request, 'ExtendedLivyBatchRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('ExtendedLivyBatchResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/batches'}

    def get(
        self,
        workspace_name,  # type: str
        spark_pool_name,  # type: str
        batch_id,  # type: int
        detailed=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ExtendedLivyBatchResponse"
        """Gets a single spark batch job.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand" targets the ondemand pool.
        :type spark_pool_name: str
        :param batch_id: Identifier for the batch job.
        :type batch_id: int
        :param detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :type detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExtendedLivyBatchResponse or the result of cls(response)
        :rtype: ~azure.synapse.models.ExtendedLivyBatchResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ExtendedLivyBatchResponse"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str'),
            'batchId': self._serialize.url("batch_id", batch_id, 'int'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if detailed is not None:
            query_parameters['detailed'] = self._serialize.query("detailed", detailed, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('ExtendedLivyBatchResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/batches/{batchId}'}

    def delete(
        self,
        workspace_name,  # type: str
        spark_pool_name,  # type: str
        batch_id,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Cancels a running spark batch job.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand" targets the ondemand pool.
        :type spark_pool_name: str
        :param batch_id: Identifier for the batch job.
        :type batch_id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str'),
            'batchId': self._serialize.url("batch_id", batch_id, 'int'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/batches/{batchId}'}
