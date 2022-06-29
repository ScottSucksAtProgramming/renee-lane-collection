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
from brownie import ReneeLaneCollection
from web3 import Web3
import random

# * ------------------------------- Variables ------------------------------ #

# * ------------------------ printInvestorList() Tests --------------------- #
# Todo: Test printInvestorList() returns no investors when empty.


def test_printInvestorList_returns_no_investors_when_empty():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": get_account()})
    # Act
    expected_investorList = []
    actual_investorList = reneeLaneCollection.printInvestorList()
    print(f"\nExpected investors list is: {expected_investorList}.")
    print(f"Returned investors list is: {actual_investorList}.\n")
    # Assert
    assert actual_investorList == expected_investorList


# Todo: Test printInvestorList() returns all investors.
def test_printInvestorList_returns_correct_investors():
    # Arrange
    account = get_account()
    random_account = get_account(random.randint(3, 9))
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": get_account()})
    reneeLaneCollection.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": get_account(1)}
    )
    reneeLaneCollection.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": get_account(2)}
    )
    # Act
    reneeLaneCollection.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": random_account}
    )
    expected_investorList = [
        str(get_account(1)),
        str(get_account(2)),
        str(random_account),
    ]
    actual_investorList = reneeLaneCollection.printInvestorList()
    print(f"\nExpected investors list is: {expected_investorList}.")
    print(f"Returned investors list is: {actual_investorList}.\n")
    # Assert
    assert actual_investorList == expected_investorList
