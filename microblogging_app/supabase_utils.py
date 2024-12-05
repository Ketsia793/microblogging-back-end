import requests
from django.conf import settings

SUPABASE_URL = settings.SUPABASE_URL
SUPABASE_KEY = settings.SUPABASE_KEY
headers = {
    "apikey": SUPABASE_KEY,
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SUPABASE_KEY}",
}

def fetch_from_supabase(endpoint):
    url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
    response = requests.get(url, headers=headers)
    return response.json()

# def insert_to_supabase(endpoint, data):
#     url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
#     response = requests.post(url, json=data, headers=headers)
#     print(f"Response status: {response.status_code}")
#     print(f"Response text: {response.text}")
#     return response.json()

def insert_to_supabase(endpoint, data):
    try:
        url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return data  # Return the inserted data if successful
    except Exception as e:
        print(f"Supabase insertion error: {e}")
        raise 
    
def update_to_supabase(endpoint, data):
    url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
    response = requests.put(url, json=data, headers=headers)
    return response.json()

def delete_from_supabase(endpoint, data):
    url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
    response = requests.delete(url, headers=headers)
    return response.json()
