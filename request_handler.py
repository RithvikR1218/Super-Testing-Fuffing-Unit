import requests

def send_request(method, url, words, headers, data):
    if method.upper() == "GET":
        for word in words:
            target_url = url.replace("FUZZ", word)
            try:
                response = requests.get(target_url, headers=headers)
                print(f"{target_url} => {response.status_code}")
            except requests.RequestException as e:
                print(f"Error sending GET request to {target_url}: {e}")

    elif method.upper() == "POST":
        for word in words:
            target_url = url.replace("FUZZ", word)
            try:
                response = requests.post(target_url, data=data, headers=headers)
                print(f"{target_url} => {response.status_code}")
            except requests.RequestException as e:
                print(f"Error sending POST request to {target_url}: {e}")
    else:
        print(f"Error: Unsupported HTTP method '{method}'")
        exit(1)