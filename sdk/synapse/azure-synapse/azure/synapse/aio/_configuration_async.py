# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from .._version import VERSION


class SynapseClientConfiguration(Configuration):
    """Configuration for SynapseClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

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
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")
        if synapse_dns_suffix is None:
            raise ValueError("Parameter 'synapse_dns_suffix' must not be None.")
        if livy_api_version is None:
            raise ValueError("Parameter 'livy_api_version' must not be None.")
        super(SynapseClientConfiguration, self).__init__(**kwargs)

        self.credential = credential
        self.synapse_dns_suffix = synapse_dns_suffix
        self.livy_api_version = livy_api_version
        self.api_version = "2019-11-01-preview"
        self.credential_scopes = ['https://dev.azuresynapse.net/.default']
        kwargs.setdefault('sdk_moniker', 'azure-synapse/{}'.format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self,
        **kwargs: Any
    ) -> None:
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.AsyncBearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs)
