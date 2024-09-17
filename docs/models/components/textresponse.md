# TextResponse

Response model for text generation.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `text`                                                     | *str*                                                      | :heavy_check_mark:                                         | The generated text.                                        |
| `chunks`                                                   | List[[components.Chunk](../../models/components/chunk.md)] | :heavy_check_mark:                                         | The generated text chunks.                                 |