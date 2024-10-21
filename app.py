from paligemma import PaliGemma

# Initialize the PaliGemma model
model = PaliGemma()

import matplotlib.pyplot as plt
from PIL import Image
import requests

def show_image(image_url):
    raw_image = Image.open(requests.get(image_url, stream=True).raw)
    plt.imshow(raw_image)
    plt.axis('off')  # Hide axes
    plt.show()

def chat(text_prompt, image_url):
    return model.run(text_prompt, image_url)

# Define the text prompt and image URL
text_prompt = "What is in the image?"
image_url = "https://picsum.photos/200/300"


# # Run the PaliGemma model
# output = model.run(text_prompt, image_url)
# # Print the generated output
# print(output)


# Display the image first
image_url = "https://picsum.photos/200/300" # Randomly changes the image and the url works at the time of writing this code. Make sure to provide the right image url.

# Now enter a loop to ask questions about the image
while True:
    show_image(image_url)  # This shows the image in a non-blocking way
    text_prompt = input("Ask a question about the image: ")
    if text_prompt.lower() == "exit" or text_prompt.lower() == "no":
        break
    print(chat(text_prompt, image_url))