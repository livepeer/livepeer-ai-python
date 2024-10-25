# TextToImageParams


## Fields

| Field                                                                                                                                                                  | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `prompt`                                                                                                                                                               | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | Text prompt(s) to guide image generation. Separate multiple prompts with '\|' if supported by the model.                                                               |
| `model_id`                                                                                                                                                             | *Optional[str]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | Hugging Face model ID used for image generation.                                                                                                                       |
| `loras`                                                                                                                                                                | *Optional[str]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | A LoRA (Low-Rank Adaptation) model and its corresponding weight for image generation. Example: { "latent-consistency/lcm-lora-sdxl": 1.0, "nerijs/pixel-art-xl": 1.2}. |
| `height`                                                                                                                                                               | *Optional[int]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | The height in pixels of the generated image.                                                                                                                           |
| `width`                                                                                                                                                                | *Optional[int]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | The width in pixels of the generated image.                                                                                                                            |
| `guidance_scale`                                                                                                                                                       | *Optional[float]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                     | Encourages model to generate images closely linked to the text prompt (higher values may reduce image quality).                                                        |
| `negative_prompt`                                                                                                                                                      | *Optional[str]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | Text prompt(s) to guide what to exclude from image generation. Ignored if guidance_scale < 1.                                                                          |
| `safety_check`                                                                                                                                                         | *Optional[bool]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                     | Perform a safety check to estimate if generated images could be offensive or harmful.                                                                                  |
| `seed`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | Seed for random number generation.                                                                                                                                     |
| `num_inference_steps`                                                                                                                                                  | *Optional[int]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.                                               |
| `num_images_per_prompt`                                                                                                                                                | *Optional[int]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | Number of images to generate per prompt.                                                                                                                               |