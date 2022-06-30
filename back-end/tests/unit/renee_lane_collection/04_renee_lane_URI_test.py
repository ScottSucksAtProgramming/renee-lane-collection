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
from brownie import ReneeLaneCollection, reverts
from web3 import Web3
import random


# * ------------------------------- Variables ------------------------------ #


# * ---------------------------- tokenURI() Tests -------------------------- #
#! For other token related tests check renee_lane_mintArtwork_test.py
# Todo: Test _baseURI() reverts if token does not exist.
def test_tokenURI_reverts_for_nonexistent_tokenID():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    bad_token_ID = random.randint(0, 999999)
    # Act and Assert
    print(f"\nNew contract deployed, no tokens minted.")
    print("If this transaction reverts due to non-existent token ID, test will pass.\n")
    with reverts("ERC721Metadata: URI query for nonexistent token"):
        reneeLaneCollection.tokenURI(bad_token_ID)


def test_tokenURI_returns_expected_string():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    reneeLaneCollection.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": account}
    )
    # Act
    expected_string = f"https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/1.json"
    actual_string = reneeLaneCollection.tokenURI(1)
    print(f"\nThe expected string is: {expected_string}.")
    print(f"The returned string is: {actual_string}.\n")
    # # Assert
    assert actual_string == expected_string