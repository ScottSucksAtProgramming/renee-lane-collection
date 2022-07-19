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
from scripts.helpful_scripts import get_account
from brownie import ReneeLaneCollection, ZERO_ADDRESS
from web3 import Web3
import random
import pytest

# * ------------------------------- Variables ------------------------------ #


@pytest.fixture
def contract_setup_with_open_minting():
    """Setup for the contract. Whitelists the Zero address."""
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy(
        {"from": deployer_account})
    contract.addToWhitelist(ZERO_ADDRESS)
    return contract
# * ------------------------ getContractBalance() Tests -------------------- #
# todo: test getContractBalance() can be called by owner.


def test_getContractBalance_returns_expected_result(contract_setup_with_open_minting):
    # Arrange
    contract = contract_setup_with_open_minting
    transactions = random.randint(0, 8)
    account = get_account()
    # Act
    for i in range(transactions):
        contract.purchaseArtwork(
            1, {"value": Web3.toWei(0.12, "ether"), "from": account}
        )
    expected_contract_balance = Web3.toWei(0.12, "ether") * transactions
    actual_contract_balance = contract.getContractBalance({"from": account})
    # Assert
    assert actual_contract_balance == expected_contract_balance
