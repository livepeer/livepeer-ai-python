# Livepeer AI Python Library

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=livepeer-ai&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

Welcome to the [Livepeer AI](https://livepeer.ai/) Python! This library offers a seamless integration with the [Livepeer AI API](https://docs.livepeer.org/ai/api-reference/text-to-image), enabling you to easily incorporate powerful AI capabilities into your Python applications, whether they run in the browser or on the server side.

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install livepeer-ai
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add livepeer-ai
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from livepeer-ai python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "livepeer-ai",
# ]
# ///

from livepeer_ai import Livepeer

sdk = Livepeer(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.text_to_image(request={
        "prompt": "<value>",
    })

    assert res.image_response is not None

    # Handle response
    print(res.image_response)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from livepeer_ai import Livepeer

async def main():
    async with Livepeer(
        http_bearer="<YOUR_BEARER_TOKEN_HERE>",
    ) as livepeer:

        res = await livepeer.generate.text_to_image_async(request={
            "prompt": "<value>",
        })

        assert res.image_response is not None

        # Handle response
        print(res.image_response)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [generate](docs/sdks/generate/README.md)

* [text_to_image](docs/sdks/generate/README.md#text_to_image) - Text To Image
* [image_to_image](docs/sdks/generate/README.md#image_to_image) - Image To Image
* [image_to_video](docs/sdks/generate/README.md#image_to_video) - Image To Video
* [upscale](docs/sdks/generate/README.md#upscale) - Upscale
* [audio_to_text](docs/sdks/generate/README.md#audio_to_text) - Audio To Text
* [segment_anything2](docs/sdks/generate/README.md#segment_anything2) - Segment Anything 2
* [llm](docs/sdks/generate/README.md#llm) - LLM
* [image_to_text](docs/sdks/generate/README.md#image_to_text) - Image To Text
* [live_video_to_video](docs/sdks/generate/README.md#live_video_to_video) - Live Video To Video
* [text_to_speech](docs/sdks/generate/README.md#text_to_speech) - Text To Speech


</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.image_to_image(request={
        "prompt": "<value>",
        "image": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    assert res.image_response is not None

    # Handle response
    print(res.image_response)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from livepeer_ai import Livepeer
from livepeer_ai.utils import BackoffStrategy, RetryConfig

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.text_to_image(request={
        "prompt": "<value>",
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.image_response is not None

    # Handle response
    print(res.image_response)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from livepeer_ai import Livepeer
from livepeer_ai.utils import BackoffStrategy, RetryConfig

with Livepeer(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.text_to_image(request={
        "prompt": "<value>",
    })

    assert res.image_response is not None

    # Handle response
    print(res.image_response)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `text_to_image_async` method may raise the following exceptions:

| Error Type                 | Status Code | Content Type     |
| -------------------------- | ----------- | ---------------- |
| errors.HTTPError           | 400, 401    | application/json |
| errors.HTTPValidationError | 422         | application/json |
| errors.HTTPError           | 500         | application/json |
| errors.SDKError            | 4XX, 5XX    | \*/\*            |

### Example

```python
from livepeer_ai import Livepeer
from livepeer_ai.models import errors

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:
    res = None
    try:

        res = livepeer.generate.text_to_image(request={
            "prompt": "<value>",
        })

        assert res.image_response is not None

        # Handle response
        print(res.image_response)

    except errors.HTTPError as e:
        # handle e.data: errors.HTTPErrorData
        raise(e)
    except errors.HTTPValidationError as e:
        # handle e.data: errors.HTTPValidationErrorData
        raise(e)
    except errors.HTTPError as e:
        # handle e.data: errors.HTTPErrorData
        raise(e)
    except errors.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                                      |
| --- | ------------------------------------------- |
| 0   | `https://dream-gateway.livepeer.cloud`      |
| 1   | `https://livepeer.studio/api/beta/generate` |

#### Example

```python
from livepeer_ai import Livepeer

with Livepeer(
    server_idx=1,
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.text_to_image(request={
        "prompt": "<value>",
    })

    assert res.image_response is not None

    # Handle response
    print(res.image_response)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from livepeer_ai import Livepeer

with Livepeer(
    server_url="https://dream-gateway.livepeer.cloud",
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.text_to_image(request={
        "prompt": "<value>",
    })

    assert res.image_response is not None

    # Handle response
    print(res.image_response)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from livepeer_ai import Livepeer
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Livepeer(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from livepeer_ai import Livepeer
from livepeer_ai.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Livepeer(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      |
| ------------- | ---- | ----------- |
| `http_bearer` | http | HTTP Bearer |

To authenticate with the API the `http_bearer` parameter must be set when initializing the SDK client instance. For example:
```python
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.text_to_image(request={
        "prompt": "<value>",
    })

    assert res.image_response is not None

    # Handle response
    print(res.image_response)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Livepeer` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from livepeer_ai import Livepeer
def main():
    with Livepeer(
        http_bearer="<YOUR_BEARER_TOKEN_HERE>",
    ) as livepeer:
        # Rest of application here...


# Or when using async:
async def amain():
    async with Livepeer(
        http_bearer="<YOUR_BEARER_TOKEN_HERE>",
    ) as livepeer:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from livepeer_ai import Livepeer
import logging

logging.basicConfig(level=logging.DEBUG)
s = Livepeer(debug_logger=logging.getLogger("livepeer_ai"))
```
<!-- End Debugging [debug] -->

<!-- Start Summary [summary] -->
## Summary

Livepeer AI Runner: An application to run AI pipelines
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Livepeer AI Python Library](#livepeer-ai-python-library)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in **alpha**, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. We look forward to hearing your feedback. Feel free to open a [PR](https://github.com/livepeer/livepeer-ai-python/compare) or [an issue](https://github.com/livepeer/livepeer-ai-python/issues) with a proof of concept and we'll do our best to include it in a future release.

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=livepeer-ai&utm_campaign=python)
