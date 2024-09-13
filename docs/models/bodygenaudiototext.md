# BodyGenAudioToText


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `audio`                                       | [models.Audio](../models/audio.md)            | :heavy_check_mark:                            | Uploaded audio file to be transcribed.        |
| `model_id`                                    | *Optional[str]*                               | :heavy_minus_sign:                            | Hugging Face model ID used for transcription. |