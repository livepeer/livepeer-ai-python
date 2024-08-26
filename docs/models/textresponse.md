# TextResponse

Response model for text generation.


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `text`                                   | *str*                                    | :heavy_check_mark:                       | The generated text.                      |
| `chunks`                                 | List[[models.Chunk](../models/chunk.md)] | :heavy_check_mark:                       | The generated text chunks.               |