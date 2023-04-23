#@title Import libraries
import os
import torch
import requests

from diffusers import DiffusionPipeline, StableDiffusionImg2ImgPipeline
from io import BytesIO
from PIL import Image


device = "cuda"
generator = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1", torch_dtype=torch.float16
    ).to(device)

# Let's download an initial image. Use the cell below if you have your own image
url = "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/assets/stable-samples/img2img/sketch-mountains-input.jpg"

response = requests.get(url)
init_image = Image.open(BytesIO(response.content)).convert("RGB")
 

# Check that your image has been uploaded correctly
os.listdir('./sample_data')

# Uncomment below to read image
init_image = Image.open('./sample_data/foo.png')
init_image.thumbnail((768, 768))

prompt = "wearing a hat"

images = pipe(
    prompt=prompt, # try changing prompt text
    image=init_image,
    strength=.7, # vary between 0.1-1.0
    guidance_scale=45, # vary between 1-100
    num_inference_steps=50
).images


#images[0].save("fantasy_landscape.png")

images[0]
