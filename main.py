import requests
import argparse

# Taking flags
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist'")
parser.add_argument("-u", "--url", required=True,help="Target URL")
parser.add_argument("-X", "--method", help="Target URL", default="GET")
args = parser.parse_args()

# Opening files based on word list paths
path = args.wordlist
words = open(path,'r').read().split('\n')
if args.method == "GET":
    for word in words:
        
        # Replacing key word in URL
        target_url = args.url.replace("FUZZ", word)

        # Sending requests to the URL
        response = requests.head(target_url)
        print(f"{target_url} => {response.status_code}")

elif args.method == "POST":
    for word in words:
        
        # Replacing key word in URL
        target_url = args.url.replace("FUZZ", word)

        # Sending requests to the URL
        response = requests.post(target_url)
        print(f"{target_url} => {response.status_code}")
