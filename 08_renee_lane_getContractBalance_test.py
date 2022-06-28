#
# * ------------------------------ Documentation --------------------------- #
# Module:  renee_lane_collection_token_test.py
# This module contains all the unit tests for tokens created by The Renee Lane
# collection.
#
#
# Modification History
# 06-17-22 | SRK | Module Created

# * -------------------------------- Tasks --------------------------------- #


# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account, characters
from brownie import accounts, config, network, ReneeLaneCollection, reverts
from brownie.test import given, strategy
from web3 import Web3
import gc, random, string, pytest

# * ------------------------------- Variables ------------------------------ #


def generate_random_string():
    _string = "".join(random.choice(characters) for i in range(1, 3))
    return _string


# * ------------------------ getContractBalance() Tests -------------------- #
# todo: test getContractBalance() can be called by owner.
def test_getContractBalance_returns_expected_result():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    transactions = random.randint(0, 8)
    # Act
    for i in range(transactions):
        reneeLaneCollection.mintArtwork(
            1, {"value": Web3.toWei(0.12, "ether"), "from": account}
        )
    expected_contract_balance = Web3.toWei(0.12, "ether") * transactions
    actual_contract_balance = reneeLaneCollection.getContractBalance({"from": account})
    print(f"\nExpected Contract Balance: {expected_contract_balance}.")
    print(f"Returned Contract Balance: {actual_contract_balance}.\n")
    # Assert
    assert actual_contract_balance == expected_contract_balance
