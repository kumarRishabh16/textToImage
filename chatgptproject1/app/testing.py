import json
import requests

# Replace YOUR_API_KEY with your actual API key
api_key = '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'

# The text you want to use to generate the image
prompt = input('A cat sitting on a windowsill')

# The API endpoint for the DALL-E API
url = 'https://api.openai.com/v1/images/generations'

# The headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# The data to send in the API request
data = json.dumps({
    'prompt': prompt,
    'model': 'image-alpha-001',
    'size': '1024x1024'
})

# Make the API request
response = requests.post(url, headers=headers, data=data)

# The image data is in the 'data' field of the response
image_data = response.json()['data']

# You can save the image data to a file, or do whatever you need to do with it
with open('image.jpg', 'wb') as f:
    f.write(image_data)
