# LLMResponse


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `model`                                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `created`                                                            | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `usage`                                                              | [components.LLMTokenUsage](../../models/components/llmtokenusage.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `choices`                                                            | List[[components.LLMChoice](../../models/components/llmchoice.md)]   | :heavy_check_mark:                                                   | N/A                                                                  |