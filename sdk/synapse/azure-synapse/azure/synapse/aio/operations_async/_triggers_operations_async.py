# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod, async_poller

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class TriggersOperations:
    """TriggersOperations async operations.

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
    ) -> "models.TriggerListResponse":
        """Lists triggers.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TriggerListResponse or the result of cls(response)
        :rtype: ~azure.synapse.models.TriggerListResponse
        :raises: ~azure.synapse.models.CloudErrorException:
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TriggerListResponse"]
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
            deserialized = self._deserialize('TriggerListResponse', pipeline_response)
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
    list_by_workspace.metadata = {'url': '/triggers'}

    async def create_or_update(
        self,
        workspace_name: str,
        trigger_name: str,
        properties: "models.Trigger",
        if_match: Optional[str] = None,
        **kwargs
    ) -> "models.TriggerResource":
        """Creates or updates a trigger.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param trigger_name: The trigger name.
        :type trigger_name: str
        :param properties: Properties of the trigger.
        :type properties: ~azure.synapse.models.Trigger
        :param if_match: ETag of the trigger entity.  Should only be specified for update, for which it
         should match existing entity or can be * for unconditional update.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TriggerResource or the result of cls(response)
        :rtype: ~azure.synapse.models.TriggerResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TriggerResource"]
        error_map = kwargs.pop('error_map', {})

        _trigger = models.TriggerResource(properties=properties)
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'triggerName': self._serialize.url("trigger_name", trigger_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
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
        body_content = self._serialize.body(_trigger, 'TriggerResource')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('TriggerResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/triggers/{triggerName}'}

    async def get(
        self,
        workspace_name: str,
        trigger_name: str,
        if_none_match: Optional[str] = None,
        **kwargs
    ) -> "models.TriggerResource":
        """Gets a trigger.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param trigger_name: The trigger name.
        :type trigger_name: str
        :param if_none_match: ETag of the trigger entity. Should only be specified for get. If the ETag
         matches the existing entity tag, or if * was provided, then no content will be returned.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TriggerResource or the result of cls(response)
        :rtype: ~azure.synapse.models.TriggerResource or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TriggerResource"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'triggerName': self._serialize.url("trigger_name", trigger_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
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
            deserialized = self._deserialize('TriggerResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/triggers/{triggerName}'}

    async def delete(
        self,
        workspace_name: str,
        trigger_name: str,
        **kwargs
    ) -> None:
        """Deletes a trigger.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param trigger_name: The trigger name.
        :type trigger_name: str
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
            'triggerName': self._serialize.url("trigger_name", trigger_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
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

    delete.metadata = {'url': '/triggers/{triggerName}'}

    async def _subscribe_to_events_initial(
        self,
        workspace_name: str,
        trigger_name: str,
        **kwargs
    ) -> "models.TriggerSubscriptionOperationStatus":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TriggerSubscriptionOperationStatus"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self._subscribe_to_events_initial.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'triggerName': self._serialize.url("trigger_name", trigger_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('TriggerSubscriptionOperationStatus', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _subscribe_to_events_initial.metadata = {'url': '/triggers/{triggerName}/subscribeToEvents'}

    async def subscribe_to_events(
        self,
        workspace_name: str,
        trigger_name: str,
        **kwargs
    ) -> "models.TriggerSubscriptionOperationStatus":
        """Subscribe event trigger to events.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param trigger_name: The trigger name.
        :type trigger_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns TriggerSubscriptionOperationStatus
        :rtype: ~azure.core.polling.LROPoller[~azure.synapse.models.TriggerSubscriptionOperationStatus]

        :raises ~azure.synapse.models.CloudErrorException:
        """
        polling = kwargs.pop('polling', False)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TriggerSubscriptionOperationStatus"]
        raw_result = await self._subscribe_to_events_initial(
            workspace_name=workspace_name,
            trigger_name=trigger_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('TriggerSubscriptionOperationStatus', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: raise ValueError("polling being True is not valid because no default polling implemetation has been defined.")
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    subscribe_to_events.metadata = {'url': '/triggers/{triggerName}/subscribeToEvents'}

    async def get_event_subscription_status(
        self,
        workspace_name: str,
        trigger_name: str,
        **kwargs
    ) -> "models.TriggerSubscriptionOperationStatus":
        """Get a trigger's event subscription status.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param trigger_name: The trigger name.
        :type trigger_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TriggerSubscriptionOperationStatus or the result of cls(response)
        :rtype: ~azure.synapse.models.TriggerSubscriptionOperationStatus
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TriggerSubscriptionOperationStatus"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.get_event_subscription_status.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'triggerName': self._serialize.url("trigger_name", trigger_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('TriggerSubscriptionOperationStatus', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_event_subscription_status.metadata = {'url': '/triggers/{triggerName}/getEventSubscriptionStatus'}

    async def _unsubscribe_from_events_initial(
        self,
        workspace_name: str,
        trigger_name: str,
        **kwargs
    ) -> "models.TriggerSubscriptionOperationStatus":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TriggerSubscriptionOperationStatus"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self._unsubscribe_from_events_initial.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'triggerName': self._serialize.url("trigger_name", trigger_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('TriggerSubscriptionOperationStatus', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _unsubscribe_from_events_initial.metadata = {'url': '/triggers/{triggerName}/unsubscribeFromEvents'}

    async def unsubscribe_from_events(
        self,
        workspace_name: str,
        trigger_name: str,
        **kwargs
    ) -> "models.TriggerSubscriptionOperationStatus":
        """Unsubscribe event trigger from events.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param trigger_name: The trigger name.
        :type trigger_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns TriggerSubscriptionOperationStatus
        :rtype: ~azure.core.polling.LROPoller[~azure.synapse.models.TriggerSubscriptionOperationStatus]

        :raises ~azure.synapse.models.CloudErrorException:
        """
        polling = kwargs.pop('polling', False)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TriggerSubscriptionOperationStatus"]
        raw_result = await self._unsubscribe_from_events_initial(
            workspace_name=workspace_name,
            trigger_name=trigger_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('TriggerSubscriptionOperationStatus', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: raise ValueError("polling being True is not valid because no default polling implemetation has been defined.")
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    unsubscribe_from_events.metadata = {'url': '/triggers/{triggerName}/unsubscribeFromEvents'}

    async def _start_initial(
        self,
        workspace_name: str,
        trigger_name: str,
        **kwargs
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self._start_initial.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'triggerName': self._serialize.url("trigger_name", trigger_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    _start_initial.metadata = {'url': '/triggers/{triggerName}/start'}

    async def start(
        self,
        workspace_name: str,
        trigger_name: str,
        **kwargs
    ) -> None:
        """Starts a trigger.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param trigger_name: The trigger name.
        :type trigger_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]

        :raises ~azure.synapse.models.CloudErrorException:
        """
        polling = kwargs.pop('polling', False)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        raw_result = await self._start_initial(
            workspace_name=workspace_name,
            trigger_name=trigger_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: raise ValueError("polling being True is not valid because no default polling implemetation has been defined.")
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    start.metadata = {'url': '/triggers/{triggerName}/start'}

    async def _stop_initial(
        self,
        workspace_name: str,
        trigger_name: str,
        **kwargs
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self._stop_initial.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'triggerName': self._serialize.url("trigger_name", trigger_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    _stop_initial.metadata = {'url': '/triggers/{triggerName}/stop'}

    async def stop(
        self,
        workspace_name: str,
        trigger_name: str,
        **kwargs
    ) -> None:
        """Stops a trigger.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param trigger_name: The trigger name.
        :type trigger_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]

        :raises ~azure.synapse.models.CloudErrorException:
        """
        polling = kwargs.pop('polling', False)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        raw_result = await self._stop_initial(
            workspace_name=workspace_name,
            trigger_name=trigger_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: raise ValueError("polling being True is not valid because no default polling implemetation has been defined.")
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    stop.metadata = {'url': '/triggers/{triggerName}/stop'}
