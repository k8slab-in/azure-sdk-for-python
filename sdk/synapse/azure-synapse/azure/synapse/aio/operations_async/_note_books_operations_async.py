# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class NoteBooksOperations:
    """NoteBooksOperations async operations.

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

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_workspace(
        self,
        workspace_name: str,
        **kwargs
    ) -> "models.NoteBookListResponse":
        """Lists notebooks.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NoteBookListResponse or the result of cls(response)
        :rtype: ~azure.synapse.models.NoteBookListResponse
        :raises: ~azure.synapse.models.CloudErrorException:
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.NoteBookListResponse"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_workspace.metadata['url']
                path_format_arguments = {
                    'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
                    'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link
                path_format_arguments = {
                    'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
                    'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('NoteBookListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException.from_response(response, self._deserialize)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_workspace.metadata = {'url': '/notebooks'}

    def list_summary_by_work_space(
        self,
        workspace_name: str,
        **kwargs
    ) -> "models.NoteBookListResponse":
        """Lists a summary of notebooks.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NoteBookListResponse or the result of cls(response)
        :rtype: ~azure.synapse.models.NoteBookListResponse
        :raises: ~azure.synapse.models.CloudErrorException:
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.NoteBookListResponse"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_summary_by_work_space.metadata['url']
                path_format_arguments = {
                    'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
                    'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link
                path_format_arguments = {
                    'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
                    'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('NoteBookListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException.from_response(response, self._deserialize)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_summary_by_work_space.metadata = {'url': '/notebooks/summary'}

    async def create_or_update(
        self,
        workspace_name: str,
        note_book_name: str,
        properties: "models.NoteBook",
        if_match: Optional[str] = None,
        **kwargs
    ) -> "models.NoteBookResource":
        """Creates or updates a Note Book.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param note_book_name: The note book name.
        :type note_book_name: str
        :param properties: Properties of NoteBook.
        :type properties: ~azure.synapse.models.NoteBook
        :param if_match: ETag of the Note book entity.  Should only be specified for update, for which
         it should match existing entity or can be * for unconditional update.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NoteBookResource or the result of cls(response)
        :rtype: ~azure.synapse.models.NoteBookResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.NoteBookResource"]
        error_map = kwargs.pop('error_map', {})

        _note_book = models.NoteBookResource(properties=properties)
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'noteBookName': self._serialize.url("note_book_name", note_book_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_note_book, 'NoteBookResource')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('NoteBookResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/notebooks/{noteBookName}'}

    async def get(
        self,
        workspace_name: str,
        note_book_name: str,
        if_none_match: Optional[str] = None,
        **kwargs
    ) -> "models.NoteBookResource":
        """Gets a Note Book.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param note_book_name: The note book name.
        :type note_book_name: str
        :param if_none_match: ETag of the notebook entity. Should only be specified for get. If the
         ETag matches the existing entity tag, or if * was provided, then no content will be returned.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NoteBookResource or the result of cls(response)
        :rtype: ~azure.synapse.models.NoteBookResource or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.NoteBookResource"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'noteBookName': self._serialize.url("note_book_name", note_book_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('NoteBookResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/notebooks/{noteBookName}'}

    async def delete(
        self,
        workspace_name: str,
        note_book_name: str,
        **kwargs
    ) -> None:
        """Deletes a Note book.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param note_book_name: The note book name.
        :type note_book_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'noteBookName': self._serialize.url("note_book_name", note_book_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/notebooks/{noteBookName}'}
