<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.text_to_image(request={
        "prompt": "<value>",
        "model_id": "",
        "loras": "",
        "height": 576,
        "width": 1024,
        "guidance_scale": 7.5,
        "negative_prompt": "",
        "safety_check": True,
        "num_inference_steps": 50,
        "num_images_per_prompt": 1,
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
            "model_id": "",
            "loras": "",
            "height": 576,
            "width": 1024,
            "guidance_scale": 7.5,
            "negative_prompt": "",
            "safety_check": True,
            "num_inference_steps": 50,
            "num_images_per_prompt": 1,
        })

        assert res.image_response is not None

        # Handle response
        print(res.image_response)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->