# MasksResponse

Response model for object segmentation.


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `masks`                                                   | *str*                                                     | :heavy_check_mark:                                        | The generated masks.                                      |
| `scores`                                                  | *str*                                                     | :heavy_check_mark:                                        | The model's confidence scores for each generated mask.    |
| `logits`                                                  | *str*                                                     | :heavy_check_mark:                                        | The raw, unnormalized predictions (logits) for the masks. |