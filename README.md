# Super-Testing-Fuzzing-Unit
## A fuzzing tool for all your needs

# Setup
## Setup Virtual Env
- python3 -m venv .venv
- source .venv/bin/activate

## Install Dependencies
- pip3 install -r requirements.txt

## Setup Worldlist
- touch wordlist.txt
- type words or use already existing applications

## Run the tool
- python3 main.py -w wordlist.txt -u "http://example.com/FUZZ" -X POST -d "{username=admin,password=FUZZ}" -H "Content-Type: application/x-www-form-urlencoded"