import json
import requests

# Replace YOUR_API_KEY with your actual API key



import json
import requests

def generate_image_from_prompt(prompt):
    # Replace YOUR_API_KEY with your actual API key
    api_key = 'your api key'

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
        'size': '512x512'
    })

    # Make the API request
    response = requests.post(url, headers=headers, data=data)

    # The image data is in the 'data' field of the response
    image_data = response.json()['data']

    return image_data
