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
# * ------------------------ printInvestorList() Tests --------------------- #
# Todo: Test printInvestorList() returns no investors when empty.


def test_printInvestorList_returns_no_investors_when_empty(contract_setup_with_open_minting):
    # Arrange
    contract = contract_setup_with_open_minting
    account = get_account()
    # Act
    expected_investorList = []
    actual_investorList = contract.printInvestorList()
    print(f"\nExpected investors list is: {expected_investorList}.")
    print(f"Returned investors list is: {actual_investorList}.\n")
    # Assert
    assert actual_investorList == expected_investorList


# Todo: Test printInvestorList() returns all investors.
def test_printInvestorList_returns_correct_investors(contract_setup_with_open_minting):
    # Arrange
    contract = contract_setup_with_open_minting

    account = get_account()
    random_account = get_account(random.randint(3, 9))
    contract.purchaseArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": get_account(1)}
    )
    contract.purchaseArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": get_account(2)}
    )
    # Act
    contract.purchaseArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": random_account}
    )
    expected_investorList = [
        str(get_account(1)),
        str(get_account(2)),
        str(random_account),
    ]
    actual_investorList = contract.printInvestorList()
    # Assert
    assert actual_investorList == expected_investorList
