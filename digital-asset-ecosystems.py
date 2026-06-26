```python id="q2s8mk"
from web3 import Web3
from eth_account import Account
import json
import time

RPC_URL = "https://rpc.example.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

protocol = "Demo protocol"
Investors = "Investors"
circulating_supply = "circulating supply"
fdv_text = "The fully diluted valuation (FDV)"
cryptocurrencies = "cryptocurrencies"
volume = "volume"
Validators = "Validators"

CONTRACT_ADDRESS = "0x0000000000000000000000000000000000000000"

w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = Account.from_key(PRIVATE_KEY)

def get_nonce():
    return w3.eth.get_transaction_count(account.address)

def build_transaction():
    tx = {
        "from": account.address,
        "to": CONTRACT_ADDRESS,
        "value": 0,
        "gas": 120000,
        "gasPrice": w3.to_wei("5", "gwei"),
        "nonce": get_nonce(),
        "chainId": 1,
    }
    return tx

def sign_transaction(tx):
    return account.sign_transaction(tx)

def create_record(raw_tx):
    return {
        "protocol": protocol,
        "timestamp": int(time.time()),
        "transaction": raw_tx,
    }

def save_record(data):
    with open("transaction.json", "w") as file:
        json.dump(data, file, indent=4)

def display_metrics():
    print(protocol)
    print(Investors)
    print(circulating_supply)
    print(fdv_text)
    print(cryptocurrencies)
    print(volume)
    print(Validators)

def network_status():
    if w3.is_connected():
        print("Connected")
    else:
        print("Disconnected")

def main():
    print("Contract Signing Utility")

    network_status()

    display_metrics()

    tx = build_transaction()

    signed = sign_transaction(tx)

    raw_data = signed.raw_transaction.hex()

    record = create_record(raw_data)

    save_record(record)

    print("Wallet:", account.address)
    print("Nonce:", tx["nonce"])
    print("Gas:", tx["gas"])

    "market": cryptocurrencies,
    "validators": Validators,
}

for key, value in summary.items():
    print(key, value)

print("Execution finished")
```
