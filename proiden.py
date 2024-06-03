from web3 import Web3
from web3.middleware import geth_poa_middleware
import json

def web3_sushiswap(private_key, gas_limit, to_address, token_symbol):
    # Provider
    w3 = Web3(Web3.HTTPProvider("https://www.example.com    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # Account
    account = w3.eth.account.privateKeyToAccount(private_key)

    # Contract
    with open("./abis/SushiSwap.json") as f:
        abi = json.load(f)
    contract_address = "0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997556"
    contract = w3.eth.contract(address=contract_address, abi=abi)

    # Get token address
    token_address = contract.functions.getTokenAddress(token_symbol).call()

    # Approve
    approve_tx = contract.functions.approve(
        to_address, 1000000000000000000000000000
    ).buildTransaction({
        'chainId': 137,
        'gas': gas_limit,
        'gasPrice': w3.toWei('120', 'gwei'),
        'nonce': w3.eth.get_transaction_count(account.address),
    })
    signed_approve_tx = w3.eth.account.sign_transaction(approve_tx, private_key=private_key)
    approve_tx_hash = w3.eth.send_raw_transaction(signed_approve_tx.rawTransaction)
    approve_receipt = w3.eth.wait_for_transaction_receipt(approve_tx_hash)

    # Swap
    swap_tx = contract.functions.swap(
        token_address, 1000000000000000000, 0
    ).buildTransaction({
        'chainId': 137,
        'gas': gas_limit,
        'gasPrice': w3.toWei('120', 'gwei'),
        'nonce': w3.eth.get_transaction_count(account.address),
    })
    signed_swap_tx = w3.eth.account.sign_transaction(swap_tx, private_key=private_key)
    swap_tx_hash = w3.eth.send_raw_transaction(signed_swap_tx.rawTransaction)
    swap_receipt = w3.eth.wait_for_transaction_receipt(swap_tx_hash)

    return approve_receipt, swap_receipt

