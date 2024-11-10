import requests

def send_request(method, url, words, headers, data):
    if method.upper() == "GET":
        for word in words:
            target_url = url.replace("FUZZ", word)  # Replace FUZZ in URL
            try:
                response = requests.get(target_url, headers=headers)
                print(f"{target_url} => {response.status_code}")
            except requests.RequestException as e:
                print(f"Error sending GET request to {target_url}: {e}")

    elif method.upper() == "POST":
        for word in words:
            # Replace FUZZ in the URL
            target_url = url.replace("FUZZ", word)

            # Replace FUZZ in form data
            modified_data = {key: value.replace("FUZZ", word) for key, value in data.items()}

            try:
                response = requests.post(target_url, data=modified_data, headers=headers)
                print(f"{target_url} => {response.status_code}, {modified_data}")
            except requests.RequestException as e:
                print(f"Error sending POST request to {target_url}: {e}")
    else:
        print(f"Error: Unsupported HTTP method '{method}'")
        exit(1)
