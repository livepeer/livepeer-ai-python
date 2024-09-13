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

## text_to_image

Generate images from text prompts.

### Example Usage

```python
from livepeer_ai import LivepeerAI

s = LivepeerAI(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generate.text_to_image(request={
    "prompt": "<value>",
})

if res.image_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TextToImageParams](../../models/texttoimageparams.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GenTextToImageResponse](../../models/gentexttoimageresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPError           | 400,401,500                | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## image_to_image

Apply image transformations to a provided image.

### Example Usage

```python
from livepeer_ai import LivepeerAI

s = LivepeerAI(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generate.image_to_image(request={
    "prompt": "<value>",
    "image": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res.image_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.BodyGenImageToImage](../../models/bodygenimagetoimage.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GenImageToImageResponse](../../models/genimagetoimageresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPError           | 400,401,500                | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## image_to_video

Generate a video from a provided image.

### Example Usage

```python
from livepeer_ai import LivepeerAI

s = LivepeerAI(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generate.image_to_video(request={
    "image": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res.video_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.BodyGenImageToVideo](../../models/bodygenimagetovideo.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GenImageToVideoResponse](../../models/genimagetovideoresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPError           | 400,401,500                | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## upscale

Upscale an image by increasing its resolution.

### Example Usage

```python
from livepeer_ai import LivepeerAI

s = LivepeerAI(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generate.upscale(request={
    "prompt": "<value>",
    "image": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res.image_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.BodyGenUpscale](../../models/bodygenupscale.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GenUpscaleResponse](../../models/genupscaleresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPError           | 400,401,500                | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## audio_to_text

Transcribe audio files to text.

### Example Usage

```python
from livepeer_ai import LivepeerAI

s = LivepeerAI(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generate.audio_to_text(request={
    "audio": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res.text_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.BodyGenAudioToText](../../models/bodygenaudiototext.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GenAudioToTextResponse](../../models/genaudiototextresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPError           | 400,401,413,500            | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## segment_anything2

Segment objects in an image.

### Example Usage

```python
from livepeer_ai import LivepeerAI

s = LivepeerAI(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generate.segment_anything2(request={
    "image": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res.masks_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.BodyGenSegmentAnything2](../../models/bodygensegmentanything2.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.GenSegmentAnything2Response](../../models/gensegmentanything2response.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPError           | 400,401,500                | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
