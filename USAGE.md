<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from livepeer_ai import LivepeerAi

async def main():
    s = LivepeerAi(
        http_bearer="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.text_to_image_async(request={
        "prompt": "<value>",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->