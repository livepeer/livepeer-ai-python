# Generate
(*generate*)

## Overview

### Available Operations

* [text_to_image](#text_to_image) - Text To Image
* [image_to_image](#image_to_image) - Image To Image
* [image_to_video](#image_to_video) - Image To Video
* [upscale](#upscale) - Upscale
* [audio_to_text](#audio_to_text) - Audio To Text
* [segment_anything2](#segment_anything2) - Segment Anything 2
* [llm](#llm) - LLM
* [image_to_text](#image_to_text) - Image To Text
* [live_video_to_video](#live_video_to_video) - Live Video To Video
* [text_to_speech](#text_to_speech) - Text To Speech

## text_to_image

Generate images from text prompts.

### Example Usage

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

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.TextToImageParams](../../models/components/texttoimageparams.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GenTextToImageResponse](../../models/operations/gentexttoimageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPError           | 400, 401, 500              | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## image_to_image

Apply image transformations to a provided image.

### Example Usage

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

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.BodyGenImageToImage](../../models/components/bodygenimagetoimage.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GenImageToImageResponse](../../models/operations/genimagetoimageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPError           | 400, 401, 500              | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## image_to_video

Generate a video from a provided image.

### Example Usage

```python
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.image_to_video(request={
        "image": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    assert res.video_response is not None

    # Handle response
    print(res.video_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.BodyGenImageToVideo](../../models/components/bodygenimagetovideo.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GenImageToVideoResponse](../../models/operations/genimagetovideoresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPError           | 400, 401, 500              | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## upscale

Upscale an image by increasing its resolution.

### Example Usage

```python
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.upscale(request={
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

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.BodyGenUpscale](../../models/components/bodygenupscale.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[operations.GenUpscaleResponse](../../models/operations/genupscaleresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPError           | 400, 401, 500              | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## audio_to_text

Transcribe audio files to text.

### Example Usage

```python
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.audio_to_text(request={
        "audio": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    assert res.text_response is not None

    # Handle response
    print(res.text_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.BodyGenAudioToText](../../models/components/bodygenaudiototext.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GenAudioToTextResponse](../../models/operations/genaudiototextresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPError           | 400, 401, 413, 415, 500    | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## segment_anything2

Segment objects in an image.

### Example Usage

```python
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.segment_anything2(request={
        "image": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    assert res.masks_response is not None

    # Handle response
    print(res.masks_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.BodyGenSegmentAnything2](../../models/components/bodygensegmentanything2.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GenSegmentAnything2Response](../../models/operations/gensegmentanything2response.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPError           | 400, 401, 500              | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## llm

Generate text using a language model.

### Example Usage

```python
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.llm(request={
        "messages": [
            {
                "role": "<value>",
                "content": "<value>",
            },
        ],
    })

    assert res.llm_response is not None

    # Handle response
    print(res.llm_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [components.LLMRequest](../../models/components/llmrequest.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GenLLMResponse](../../models/operations/genllmresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPError           | 400, 401, 500              | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## image_to_text

Transform image files to text.

### Example Usage

```python
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.image_to_text(request={
        "image": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    assert res.image_to_text_response is not None

    # Handle response
    print(res.image_to_text_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.BodyGenImageToText](../../models/components/bodygenimagetotext.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GenImageToTextResponse](../../models/operations/genimagetotextresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPError           | 400, 401, 413, 500         | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## live_video_to_video

Apply transformations to a live video streamed to the returned endpoints.

### Example Usage

```python
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.live_video_to_video(request={
        "subscribe_url": "https://soulful-lava.org/",
        "publish_url": "https://vain-tabletop.biz",
    })

    assert res.live_video_to_video_response is not None

    # Handle response
    print(res.live_video_to_video_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.LiveVideoToVideoParams](../../models/components/livevideotovideoparams.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GenLiveVideoToVideoResponse](../../models/operations/genlivevideotovideoresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPError           | 400, 401, 500              | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## text_to_speech

Generate a text-to-speech audio file based on the provided text input and speaker description.

### Example Usage

```python
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.text_to_speech(request={})

    assert res.audio_response is not None

    # Handle response
    print(res.audio_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.TextToSpeechParams](../../models/components/texttospeechparams.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GenTextToSpeechResponse](../../models/operations/gentexttospeechresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPError           | 400, 401, 500              | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |