# LiveVideoToVideoParams


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `subscribe_url`                                                  | *str*                                                            | :heavy_check_mark:                                               | Source URL of the incoming stream to subscribe to.               |
| `publish_url`                                                    | *str*                                                            | :heavy_check_mark:                                               | Destination URL of the outgoing stream to publish.               |
| `model_id`                                                       | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Hugging Face model ID used for image generation.                 |
| `params`                                                         | [Optional[components.Params]](../../models/components/params.md) | :heavy_minus_sign:                                               | Initial parameters for the model.                                |