# *
# * ------------------------------ Documentation ------------------------------ #
# * Module:  helpful_scripts.py
# * This module contains helpful functions for the smart contract tests and development.
# *
# *
# * Modification History
# * 06-15-2022 | SRK | Module created.

# * -------------------------------- Tasks ----------------------------------- #

# * ------------------------------- Resources -------------------------------- #
from brownie import (
    network,
    accounts,
    config,
    web3,
)
from scripts.helpful_data import letters
import time
import random


# * ------------------------------- Variables -------------------------------- #


NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "hardhat", "development", "ganache"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + [
    "mainnet-fork",
    "binance-fork",
    "matic-fork",
]

# Etherscan usually takes a few blocks to register the contract has been deployed
BLOCK_CONFIRMATIONS_FOR_VERIFICATION = (
    1 if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS else 6
)
DECIMALS = 18
INITIAL_VALUE = web3.toWei(2000, "ether")
BASE_FEE = 100000000000000000  # The premium
GAS_PRICE_LINK = 1e9  # Some value calculated depending on the Layer 1 cost and Link
# * ------------------------------ Functions --------------------------------- #


def is_verifiable_contract() -> bool:
    return config["networks"][network.show_active()].get("verify", False)


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])


# def get_contract(contract_name):
#     """If you want to use this function, go to the brownie config and add a new entry for
#     the contract that you want to be able to 'get'. Then add an entry in the variable 'contract_to_mock'.
#     You'll see examples like the 'link_token'.
#         This script will then either:
#             - Get a address from the config
#             - Or deploy a mock to use for a network that doesn't have it
#
#         Args:
#             contract_name (string): This is the name that is referred to in the
#             brownie config and 'contract_to_mock' variable.
#
#         Returns:
#             brownie.network.contract.ProjectContract: The most recently deployed
#             Contract of the type specified by the dictionary. This could be either
#             a mock or the 'real' contract on a live network.
#     """
#     contract_type = contract_to_mock[contract_name]
#     if network.show_active() in NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS:
#         if len(contract_type) <= 0:
#             deploy_mocks()
#         contract = contract_type[-1]
#     else:
#         try:
#             contract_address = config["networks"][network.show_active()][contract_name]
#             contract = Contract.from_abi(
#                 contract_type._name, contract_address, contract_type.abi
#             )
#         except KeyError:
#             print(
#                 f"{network.show_active()} address not found, perhaps you should add it to the config or deploy mocks?"
#             )
#             print(
#                 f"brownie run scripts/deploy_mocks.py --network {network.show_active()}"
#             )
#     return contract

#
# def deploy_mocks(decimals=DECIMALS, initial_value=INITIAL_VALUE):
#     """
#     Use this script if you want to deploy mocks to a testnet
#     """
#     print(f"The active network is {network.show_active()}")
#     print("Deploying Mocks...")
#     account = get_account()
#     print("Deploying Mock Link Token...")
#     link_token = LinkToken.deploy({"from": account})
#     print("Deploying Mock Price Feed...")
#     mock_price_feed = MockV3Aggregator.deploy(
#         decimals, initial_value, {"from": account}
#     )
#     print(f"Deployed to {mock_price_feed.address}")
#     print("Deploying Mock VRFCoordinator...")
#     mock_vrf_coordinator = VRFCoordinatorV2Mock.deploy(
#         BASE_FEE, GAS_PRICE_LINK, {"from": account}
#     )
#     print(f"Deployed to {mock_vrf_coordinator.address}")
#
#     print("Deploying Mock Oracle...")
#     mock_oracle = MockOracle.deploy(link_token.address, {"from": account})
#     print(f"Deployed to {mock_oracle.address}")
#     print("Mocks Deployed!")
#


def listen_for_event(brownie_contract, event, timeout=200, poll_interval=2):
    """Listen for an event to be fired from a contract.
    We are waiting for the event to return, so this function is blocking.

    Args:
        brownie_contract ([brownie.network.contract.ProjectContract]):
        A brownie contract of some kind.

        event ([string]): The event you'd like to listen for.

        timeout (int, optional): The max amount in seconds you'd like to
        wait for that event to fire. Defaults to 200 seconds.

        poll_interval ([int]): How often to call your node to check for events.
        Defaults to 2 seconds.
    """
    web3_contract = web3.eth.contract(
        address=brownie_contract.address, abi=brownie_contract.abi
    )
    start_time = time.time()
    current_time = time.time()
    event_filter = web3_contract.events[event].createFilter(fromBlock="latest")
    while current_time - start_time < timeout:
        for event_response in event_filter.get_new_entries():
            if event in event_response.event:
                print("Found event!")
                return event_response
        time.sleep(poll_interval)
        current_time = time.time()
    print("Timeout reached, no event found.")
    return {"event": None}


def function_exists(function_list, contract):
    """Checks to see if the contract has the functions in the provided list.

    Args:
        function_list (list): List of function names to check for.
        contract (Contract Object): The contract to evaluate.

    Returns:
        bool: True/False if the contract has the functions.
    """
    for function in function_list:
        if function not in dir(contract):
            print(f"\n{function} does no exist.\n")
            return False
    return True


def generate_random_string():
    _string = "".join(random.choice(letters) for i in range(1, 3))
    return _string


def check_address(address_list, contract):
    for i in range(len(address_list)):
        if address_list[i] != contract.artist(i+1):
            print(f"\nAddress of Artist {i+1} is not set correctly.\n")
            return False
    return True


def check_properties(property_list, contract):
    for image in range(1, 50):
        if property_list[image] != contract.artGallery(image):
            print(f"Properties for image {image} are not set correctly.")
            return False
    return True
