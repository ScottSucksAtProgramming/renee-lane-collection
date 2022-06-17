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


# * ---------------------------- tokenURI() Tests -------------------------- #
#! For other token related tests check renee_lane_mintImage_test.py
# Todo: Test _baseURI() reverts if token does not exist.
def test_tokenURI_reverts_for_nonexistent_tokenID():
    # Arrange
    gc.collect(generation=2)
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    bad_token_ID = random.randint(0, 999999)
    # Act and Assert
    print(f"\nNew contract deployed, no tokens minted.")
    print("If this transaction reverts due to non-existent token ID, test will pass.\n")
    with reverts("ERC721Metadata: URI query for nonexistent token"):
        reneeLaneCollection.tokenURI(bad_token_ID)
    gc.collect(generation=2)


def test_tokenURI_returns_expected_string():
    # Arrange
    gc.collect(generation=2)
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    reneeLaneCollection.mintImage(
        1, {"value": Web3.toWei(0.12, "ether"), "from": account}
    )
    # Act
    expected_string = f"https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/1.json"
    actual_string = reneeLaneCollection.tokenURI(1)
    print(f"\nThe expected string is: {expected_string}.")
    print(f"The returned string is: {actual_string}.\n")
    # # Assert
    assert actual_string == expected_string
    gc.collect(generation=2)


def test_baseURI_returns_expected_string():
    # Arrange
    gc.collect(generation=2)
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    reneeLaneCollection.mintImage(
        1, {"value": Web3.toWei(0.12, "ether"), "from": account}
    )
    # Act
    expected_string = f"https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/"
    actual_string = reneeLaneCollection._baseURI(
        1, {"from": reneeLaneCollection.address}
    )
    print(f"\nThe expected string is: {expected_string}.")
    print(f"The returned string is: {actual_string}.\n")
    # # Assert
    assert actual_string == expected_string
    gc.collect(generation=2)
