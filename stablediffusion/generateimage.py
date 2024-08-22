from diffusers import StableDiffusionPipeline
import torch
import random
# Load the Stable Diffusion model
model_id = "runwayml/stable-diffusion-v1-5"
device = "cuda" 

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if device == "cuda" else torch.float32)
pipe = pipe.to(device)

# Generate an image
prompt = "a beautiful bird, blue bird, small, 4k"
image = pipe(prompt).images[0]

# Save the image
filename = f"generated-image-{random.randrange(0, 1000)}.png"
image.save(filename)
