# LivepeerAi SDK


## Overview

Livepeer AI Runner: An application to run AI pipelines

### Available Operations

* [text_to_image](#text_to_image) - Text To Image
* [image_to_image](#image_to_image) - Image To Image
* [image_to_video](#image_to_video) - Image To Video
* [upscale](#upscale) - Upscale
* [audio_to_text](#audio_to_text) - Audio To Text

## text_to_image

Text To Image

### Example Usage

```python
from livepeer_ai import LivepeerAi

s = LivepeerAi(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.text_to_image(request={
    "prompt": "<value>",
})

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TextToImageParams](../../models/texttoimageparams.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ImageResponse](../../models/imageresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPError           | 400,401,500                | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## image_to_image

Image To Image

### Example Usage

```python
from livepeer_ai import LivepeerAi

s = LivepeerAi(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.image_to_image(request={
    "prompt": "<value>",
    "image": {
        "file_name": "your_file_here",
        "content": open("<file_path>", "rb"),
    },
})

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.BodyImageToImageImageToImagePost](../../models/bodyimagetoimageimagetoimagepost.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |


### Response

**[models.ImageResponse](../../models/imageresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPError           | 400,401,500                | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## image_to_video

Image To Video

### Example Usage

```python
from livepeer_ai import LivepeerAi

s = LivepeerAi(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.image_to_video(request={
    "image": {
        "file_name": "your_file_here",
        "content": open("<file_path>", "rb"),
    },
})

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.BodyImageToVideoImageToVideoPost](../../models/bodyimagetovideoimagetovideopost.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |


### Response

**[models.VideoResponse](../../models/videoresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPError           | 400,401,500                | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## upscale

Upscale

### Example Usage

```python
from livepeer_ai import LivepeerAi

s = LivepeerAi(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.upscale(request={
    "prompt": "<value>",
    "image": {
        "file_name": "your_file_here",
        "content": open("<file_path>", "rb"),
    },
})

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.BodyUpscaleUpscalePost](../../models/bodyupscaleupscalepost.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |


### Response

**[models.ImageResponse](../../models/imageresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPError           | 400,401,500                | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## audio_to_text

Audio To Text

### Example Usage

```python
from livepeer_ai import LivepeerAi

s = LivepeerAi(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.audio_to_text(request={
    "audio": {
        "file_name": "your_file_here",
        "content": open("<file_path>", "rb"),
    },
})

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.BodyAudioToTextAudioToTextPost](../../models/bodyaudiototextaudiototextpost.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |


### Response

**[models.TextResponse](../../models/textresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPError           | 400,401,413,500            | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
