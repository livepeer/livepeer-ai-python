<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from livepeer_ai import Livepeer

with Livepeer(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
) as livepeer:

    res = livepeer.generate.text_to_image(request={
        "prompt": "<value>",
    })

    if res.image_response is not None:
        # handle response
        pass
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

        if res.image_response is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->