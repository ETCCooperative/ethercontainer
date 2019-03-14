import requests
import json

def main():
    url = "http://localhost:8545"
    headers = {'content-type': 'application/json'}

    payload = {
        "method": "parity_nodeStatus",
        "params": [],
        "jsonrpc": "2.0",
        "id": 1,
    }

    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    if response["result"]:
        return "", 200

if __name__ == "__main__":
    main()
