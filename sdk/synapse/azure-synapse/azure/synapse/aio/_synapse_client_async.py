# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import SynapseClientConfiguration
from .operations_async import MonitoringOperations
from .operations_async import SparkBatchOperations
from .operations_async import SparkSessionOperations
from .operations_async import WorkspaceAclOperations
from .operations_async import LinkedServicesOperations
from .operations_async import DatasetsOperations
from .operations_async import PipelinesOperations
from .operations_async import PipelineRunsOperations
from .operations_async import ActivityRunsOperations
from .operations_async import TriggersOperations
from .operations_async import TriggerRunsOperations
from .operations_async import DataFlowsOperations
from .operations_async import DataFlowDebugSessionOperations
from .operations_async import SqlScriptsOperations
from .operations_async import SparkJobDefinitionsOperations
from .operations_async import NoteBooksOperations
from .. import models


class SynapseClient(object):
    """SynapseClient.

    :ivar monitoring: MonitoringOperations operations
    :vartype monitoring: azure.synapse.aio.operations_async.MonitoringOperations
    :ivar spark_batch: SparkBatchOperations operations
    :vartype spark_batch: azure.synapse.aio.operations_async.SparkBatchOperations
    :ivar spark_session: SparkSessionOperations operations
    :vartype spark_session: azure.synapse.aio.operations_async.SparkSessionOperations
    :ivar workspace_acl: WorkspaceAclOperations operations
    :vartype workspace_acl: azure.synapse.aio.operations_async.WorkspaceAclOperations
    :ivar linked_services: LinkedServicesOperations operations
    :vartype linked_services: azure.synapse.aio.operations_async.LinkedServicesOperations
    :ivar datasets: DatasetsOperations operations
    :vartype datasets: azure.synapse.aio.operations_async.DatasetsOperations
    :ivar pipelines: PipelinesOperations operations
    :vartype pipelines: azure.synapse.aio.operations_async.PipelinesOperations
    :ivar pipeline_runs: PipelineRunsOperations operations
    :vartype pipeline_runs: azure.synapse.aio.operations_async.PipelineRunsOperations
    :ivar activity_runs: ActivityRunsOperations operations
    :vartype activity_runs: azure.synapse.aio.operations_async.ActivityRunsOperations
    :ivar triggers: TriggersOperations operations
    :vartype triggers: azure.synapse.aio.operations_async.TriggersOperations
    :ivar trigger_runs: TriggerRunsOperations operations
    :vartype trigger_runs: azure.synapse.aio.operations_async.TriggerRunsOperations
    :ivar data_flows: DataFlowsOperations operations
    :vartype data_flows: azure.synapse.aio.operations_async.DataFlowsOperations
    :ivar data_flow_debug_session: DataFlowDebugSessionOperations operations
    :vartype data_flow_debug_session: azure.synapse.aio.operations_async.DataFlowDebugSessionOperations
    :ivar sql_scripts: SqlScriptsOperations operations
    :vartype sql_scripts: azure.synapse.aio.operations_async.SqlScriptsOperations
    :ivar spark_job_definitions: SparkJobDefinitionsOperations operations
    :vartype spark_job_definitions: azure.synapse.aio.operations_async.SparkJobDefinitionsOperations
    :ivar note_books: NoteBooksOperations operations
    :vartype note_books: azure.synapse.aio.operations_async.NoteBooksOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param synapse_dns_suffix: Gets the DNS suffix used as the base for all Synapse service requests.
    :type synapse_dns_suffix: str
    :param livy_api_version: Valid api-version for the request.
    :type livy_api_version: str
    """

    def __init__(
        self,
        credential: "TokenCredential",
        synapse_dns_suffix: str = "dev.azuresynapse.net",
        livy_api_version: str = "2019-11-01-preview",
        **kwargs: Any
    ) -> None:
        base_url = 'https://{workspaceName}.{SynapseDnsSuffix}'
        self._config = SynapseClientConfiguration(credential, synapse_dns_suffix, livy_api_version, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.monitoring = MonitoringOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.spark_batch = SparkBatchOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.spark_session = SparkSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_acl = WorkspaceAclOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.linked_services = LinkedServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.datasets = DatasetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipelines = PipelinesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipeline_runs = PipelineRunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.activity_runs = ActivityRunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.triggers = TriggersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger_runs = TriggerRunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flows = DataFlowsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flow_debug_session = DataFlowDebugSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_scripts = SqlScriptsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.spark_job_definitions = SparkJobDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.note_books = NoteBooksOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SynapseClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
