import requests
import io
from PIL import Image
import matplotlib.pyplot as plt

# Define the API URL and headers with your Hugging Face token
API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face API
def query(payload):
    # makes a POST request to the API URL with the specified headers and JSON payload.
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Check for successful response
    if response.status_code == 200:
        return response.content
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Query the API
image_bytes = query({"inputs": " battery "})

# Check if we have valid image bytes
if image_bytes:
    try:
        # Try to open the image
        image = Image.open(io.BytesIO(image_bytes))
        
        # Display the image
        plt.imshow(image)
        plt.axis('off')  # Turn off axis numbers
        plt.show()
    except Image.UnidentifiedImageError:
        print("Cannot identify image file. The response might not be an image.")
else:
    print("No image bytes received.")
