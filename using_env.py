import os
from dotenv import load_dotenv

# Load the .env
load_dotenv()

api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_NAME')

print(f"Using api_key: {api_key}")