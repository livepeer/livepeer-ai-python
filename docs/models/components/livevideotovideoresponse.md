# LiveVideoToVideoResponse

Response model for live video-to-video generation.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `subscribe_url`                                            | *str*                                                      | :heavy_check_mark:                                         | Source URL of the incoming stream to subscribe to          |
| `publish_url`                                              | *str*                                                      | :heavy_check_mark:                                         | Destination URL of the outgoing stream to publish to       |
| `control_url`                                              | *Optional[str]*                                            | :heavy_minus_sign:                                         | URL for updating the live video-to-video generation        |
| `events_url`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | URL for subscribing to events for pipeline status and logs |