import requests

def send_request(method, url, word, headers, data):

    # Replace FUZZ with Host as priority
    if headers.get('Host'):
        target_url = headers['Host'].replace("FUZZ", word)
        target_url = 'http://' + target_url
    else:
        # Replace FUZZ in URL and data
        target_url = url.replace("FUZZ", word)  # Replace FUZZ with full word in URL
        if data:
            data = {key: value.replace("FUZZ", word) for key, value in data.items()}  # Replace FUZZ in form data

    try:
        if method.upper() == "GET":
            response = requests.get(target_url, headers=headers)
        elif method.upper() == "POST":
            response = requests.post(target_url, headers=headers, data=data)
        else:
            print(f"Error: Unsupported HTTP method '{method}'")
            return

        print(f"{target_url} => {response.status_code}")
    except requests.RequestException as e:
        print(f"Error sending {method} request to {target_url}")