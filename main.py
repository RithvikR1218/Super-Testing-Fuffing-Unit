import requests
import argparse

# Taking flags
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist'")
parser.add_argument("-u", "--url", required=True, help="Target URL")
parser.add_argument("-X", "--method", help="Request method (GET/POST)", default="GET")
parser.add_argument("-d", "--data", help="Form data for POST request (e.g. key1=value1&key2=value2)")
parser.add_argument("-H", "--headers", help="Custom headers for request (e.g. 'User-Agent: Mozilla/5.0')")
args = parser.parse_args()

# Check if 'FUZZ' is present in the URL
if "FUZZ" not in args.url:
    print("Error: 'FUZZ' keyword is not present in the URL.")
    exit(1)

# Try to open wordlist file
try:
    with open(args.wordlist, 'r') as file:
        words = file.read().splitlines()
except FileNotFoundError:
    print(f"Error: The file '{args.wordlist}' was not found.")
    exit(1)
except Exception as e:
    print(f"Error opening file '{args.wordlist}': {e}")
    exit(1)

# Prepare headers if provided
headers = {}
if args.headers:
    try:
        # Split headers by comma and parse into a dictionary
        for header in args.headers.split(','):
            key, value = header.split(':', 1)
            headers[key.strip()] = value.strip()
    except ValueError:
        print("Error: Invalid header format. Use 'Key: Value' pairs separated by commas.")
        exit(1)

# Request method handling
try:
    if args.method.upper() == "GET":
        for word in words:
            target_url = args.url.replace("FUZZ", word)

            try:
                # Sending GET request
                response = requests.get(target_url, headers=headers)
                print(f"{target_url} => {response.status_code}")
            except requests.RequestException as e:
                print(f"Error sending GET request to {target_url}: {e}")

    elif args.method.upper() == "POST":
        for word in words:
            target_url = args.url.replace("FUZZ", word)

            # Prepare form data if provided
            data = {}
            if args.data:
                try:
                    # Convert form data string into a dictionary
                    for pair in args.data.split('&'):
                        key, value = pair.split('=', 1)
                        data[key] = value
                except ValueError:
                    print("Error: Invalid form data format. Use 'key1=value1&key2=value2'.")
                    exit(1)

            try:
                # Sending POST request with form data and headers
                response = requests.post(target_url, data=data, headers=headers)
                print(f"{target_url} => {response.status_code}")
            except requests.RequestException as e:
                print(f"Error sending POST request to {target_url}: {e}")
    else:
        print(f"Error: Unsupported HTTP method '{args.method}'")
        exit(1)

except Exception as e:
    print(f"Unexpected error occurred: {e}")
    exit(1)